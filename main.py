import asyncio
import json
from typing import Any, AsyncIterator, Optional

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from pydantic import BaseModel

from graph2.contextualize_chain import build_standalone_question
from graph2.graph_2 import graph
from utils.conversation_memory import memory_store

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ChatRequest(BaseModel):
    question: str
    session_id: Optional[str] = None


NODE_STATUS = {
    "retrieve": "正在扩展相关问题并检索知识库…",
    "grade_documents": "正在评估文档相关性…",
    "transform_query": "正在优化查询并重试…",
    "web_search": "知识库未命中，正在联网搜索…",
    "generate": "正在生成回答…",
}


def _chunk_text(content: Any) -> str:
    if content is None:
        return ""
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        parts = []
        for item in content:
            if isinstance(item, str):
                parts.append(item)
            elif isinstance(item, dict) and item.get("type") == "text":
                parts.append(item.get("text", ""))
            elif hasattr(item, "text"):
                parts.append(getattr(item, "text") or "")
        return "".join(parts)
    return str(content)


def _sse(payload: dict) -> str:
    return f"data: {json.dumps(payload, ensure_ascii=False)}\n\n"


def _prepare_inputs(question: str, session_id: Optional[str]) -> tuple[str, str, dict]:
    sid = memory_store.ensure_session(session_id)
    history = memory_store.format_history(sid)
    standalone = build_standalone_question(question, history)
    inputs = {
        "question": standalone,
        "transform_count": 0,
        "searched_web": False,
        "chat_history": history,
    }
    return sid, standalone, inputs


@app.post("/chat")
async def chat_endpoint(request: ChatRequest):
    """兼容旧接口：一次性返回完整答案。"""
    sid, _, inputs = _prepare_inputs(request.question, request.session_id)
    final_response = "我没有找到答案，请稍后再试。"
    for output in graph.stream(inputs):
        for key, value in output.items():
            if key == "generate":
                final_response = value["generation"]
    memory_store.add_turn(sid, request.question, final_response)
    return {"answer": final_response, "session_id": sid}


@app.delete("/chat/memory/{session_id}")
async def clear_memory(session_id: str):
    memory_store.clear(session_id)
    return {"ok": True, "session_id": session_id}


@app.post("/chat/stream")
async def chat_stream(chat: ChatRequest, request: Request):
    """SSE 流式输出：带会话记忆；客户端断开时中止。"""

    async def event_generator() -> AsyncIterator[str]:
        sid = memory_store.ensure_session(chat.session_id)
        yield _sse({"type": "session", "session_id": sid})

        history = memory_store.format_history(sid)
        if history:
            yield _sse({"type": "status", "message": "正在结合上下文理解问题…"})
        standalone = build_standalone_question(chat.question, history)
        inputs = {
            "question": standalone,
            "transform_count": 0,
            "searched_web": False,
            "chat_history": history,
        }

        final_answer = "我没有找到答案，请稍后再试。"
        aborted = False

        try:
            yield _sse({"type": "status", "message": "开始处理问题…"})

            async for event in graph.astream_events(inputs, version="v2"):
                if await request.is_disconnected():
                    aborted = True
                    break

                kind = event.get("event")
                name = event.get("name") or ""
                meta = event.get("metadata") or {}
                node = meta.get("langgraph_node")

                if kind == "on_chain_start" and node in NODE_STATUS and name == node:
                    # 进入改写/联网时清空上一轮本地中间稿，避免「无法回答」残留
                    if node in ("transform_query", "web_search"):
                        yield _sse({"type": "reset"})
                    yield _sse({"type": "status", "message": NODE_STATUS[node]})
                    if node == "generate":
                        yield _sse({"type": "reset"})

                if kind == "on_chat_model_stream" and node == "generate":
                    chunk = (event.get("data") or {}).get("chunk")
                    text = _chunk_text(getattr(chunk, "content", None) if chunk is not None else None)
                    if text:
                        yield _sse({"type": "token", "content": text})

                if kind == "on_chain_end" and node == "generate" and name == "generate":
                    output = (event.get("data") or {}).get("output")
                    if isinstance(output, dict) and output.get("generation"):
                        final_answer = output["generation"]

            if aborted or await request.is_disconnected():
                yield _sse({"type": "aborted"})
            else:
                memory_store.add_turn(sid, chat.question, final_answer)
                yield _sse({"type": "done", "answer": final_answer, "session_id": sid})
        except asyncio.CancelledError:
            yield _sse({"type": "aborted"})
            raise
        except Exception as exc:
            yield _sse({"type": "error", "message": str(exc)})

    return StreamingResponse(
        event_generator(),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "X-Accel-Buffering": "no",
        },
    )
