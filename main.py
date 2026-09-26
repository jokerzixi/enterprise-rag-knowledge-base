import asyncio
import json
import time
from collections import defaultdict, deque
from typing import Any, AsyncIterator, Optional

from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, PlainTextResponse, StreamingResponse
from pydantic import BaseModel
from pymilvus import MilvusClient

from graph2.contextualize_chain import build_standalone_question
from graph2.graph_2 import graph
from utils.conversation_memory import memory_store
from utils.env_utils import COLLECTION_NAME, MILVUS_URI
from utils.log_utils import log

app = FastAPI(title="Semiconductor Adaptive RAG API", version="2.0.0")

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
    "rerank": "正在对检索文档进行精准语义重排…",
    "grade_documents": "正在评估文档相关性…",
    "transform_query": "正在优化查询并重试…",
    "web_search": "知识库未命中，正在联网搜索…",
    "generate": "正在生成回答…",
}


# ===================== 观测指标统计 (Prometheus 兼容) =====================
class MetricsCollector:
    def __init__(self):
        self.request_count = defaultdict(int)
        self.error_count = defaultdict(int)
        self.active_streams = 0
        self.total_first_token_latency = 0.0
        self.first_token_count = 0
        self.total_duration = 0.0
        self.duration_count = 0
        self.web_fallback_count = 0

    def inc_request(self, endpoint: str, status: int = 200):
        self.request_count[(endpoint, status)] += 1

    def inc_error(self, endpoint: str, error_type: str):
        self.error_count[(endpoint, error_type)] += 1

    def record_ttft(self, latency: float):
        self.total_first_token_latency += latency
        self.first_token_count += 1

    def record_duration(self, duration: float):
        self.total_duration += duration
        self.duration_count += 1

    def inc_web_fallback(self):
        self.web_fallback_count += 1

    def render_prometheus(self) -> str:
        lines = [
            "# HELP rag_requests_total Total number of HTTP requests processed.",
            "# TYPE rag_requests_total counter",
        ]
        for (ep, status), cnt in self.request_count.items():
            lines.append(f'rag_requests_total{{endpoint="{ep}",status="{status}"}} {cnt}')

        lines.extend([
            "# HELP rag_errors_total Total number of errors encountered.",
            "# TYPE rag_errors_total counter",
        ])
        for (ep, err), cnt in self.error_count.items():
            lines.append(f'rag_errors_total{{endpoint="{ep}",error="{err}"}} {cnt}')

        lines.extend([
            "# HELP rag_active_streaming_sessions Current active SSE stream sessions.",
            "# TYPE rag_active_streaming_sessions gauge",
            f"rag_active_streaming_sessions {self.active_streams}",
            "# HELP rag_ttft_seconds_total Total Time-to-First-Token in seconds.",
            "# TYPE rag_ttft_seconds_total counter",
            f"rag_ttft_seconds_total {self.total_first_token_latency:.4f}",
            "# HELP rag_ttft_count Total count of requests with TTFT recorded.",
            "# TYPE rag_ttft_count counter",
            f"rag_ttft_count {self.first_token_count}",
            "# HELP rag_request_duration_seconds_total Total request processing duration in seconds.",
            "# TYPE rag_request_duration_seconds_total counter",
            f"rag_request_duration_seconds_total {self.total_duration:.4f}",
            "# HELP rag_request_duration_count Total count of requests measured for duration.",
            "# TYPE rag_request_duration_count counter",
            f"rag_request_duration_count {self.duration_count}",
            "# HELP rag_web_fallback_total Total times web search fallback was triggered.",
            "# TYPE rag_web_fallback_total counter",
            f"rag_web_fallback_total {self.web_fallback_count}",
        ])
        return "\n".join(lines) + "\n"


metrics = MetricsCollector()

# ===================== 轻量滑动窗口限流与单会话并发防护 =====================
_IP_RATE_LIMITS = defaultdict(deque)
_ACTIVE_SESSIONS = set()
RATE_LIMIT_WINDOW = 60.0
RATE_LIMIT_MAX_REQ = 45


def _check_rate_limit(client_ip: str):
    now = time.time()
    q = _IP_RATE_LIMITS[client_ip]
    while q and q[0] <= now - RATE_LIMIT_WINDOW:
        q.popleft()
    if len(q) >= RATE_LIMIT_MAX_REQ:
        raise HTTPException(
            status_code=429,
            detail="请求过于频繁，请稍后再试（Rate limit exceeded）。"
        )
    q.append(now)


# ===================== 全局异常捕获处理 =====================
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    log.error(f"全局未捕获异常 [{request.method} {request.url.path}]: {exc}", exc_info=True)
    metrics.inc_error(request.url.path, type(exc).__name__)
    metrics.inc_request(request.url.path, 500)
    return JSONResponse(
        status_code=500,
        content={
            "error": "服务器内部错误，请稍后重试",
            "code": 500,
            "message": str(exc),
        },
    )


# ===================== 健康检查与可观测端点 =====================
@app.get("/health")
async def health_check():
    """生产级健康检查：探测 Milvus 向量库与会话存储组件状态"""
    status = {"status": "ok", "components": {}}

    # 1. 检查 Milvus 连通性与集合状态
    try:
        client = MilvusClient(uri=MILVUS_URI)
        collections = client.list_collections()
        has_col = COLLECTION_NAME in collections
        status["components"]["milvus"] = {
            "status": "healthy" if has_col else "warning",
            "uri": MILVUS_URI,
            "collection_exists": has_col,
            "collection_name": COLLECTION_NAME,
        }
    except Exception as exc:
        status["components"]["milvus"] = {
            "status": "unhealthy",
            "error": str(exc),
        }
        status["status"] = "degraded"

    # 2. 检查会话记忆存储
    status["components"]["session_memory"] = {
        "status": "healthy",
        "backend": getattr(memory_store, "backend_name", "unknown"),
    }

    metrics.inc_request("/health", 200)
    return status


@app.get("/metrics", response_class=PlainTextResponse)
async def get_metrics():
    """输出 Prometheus 兼容的运行时指标"""
    return metrics.render_prometheus()


# ===================== 内部辅助函数 =====================
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


# ===================== 业务端点 =====================
@app.post("/chat")
async def chat_endpoint(request: ChatRequest, req: Request):
    """兼容旧接口：一次性返回完整答案。"""
    client_ip = req.client.host if req.client else "unknown"
    _check_rate_limit(client_ip)

    start_time = time.time()
    sid, _, inputs = _prepare_inputs(request.question, request.session_id)
    final_response = "我没有找到答案，请稍后再试。"
    try:
        for output in graph.stream(inputs):
            for key, value in output.items():
                if key == "generate":
                    final_response = value["generation"]
        memory_store.add_turn(sid, request.question, final_response)
        metrics.inc_request("/chat", 200)
        metrics.record_duration(time.time() - start_time)
        return {"answer": final_response, "session_id": sid}
    except Exception as exc:
        metrics.inc_error("/chat", type(exc).__name__)
        metrics.inc_request("/chat", 500)
        raise


@app.delete("/chat/memory/{session_id}")
async def clear_memory(session_id: str):
    memory_store.clear(session_id)
    metrics.inc_request("/chat/memory", 200)
    return {"ok": True, "session_id": session_id}


@app.post("/chat/stream")
async def chat_stream(chat: ChatRequest, request: Request):
    """SSE 流式输出：带限流、并发防护、TTFT 测速与可观测性统计"""
    client_ip = request.client.host if request.client else "unknown"
    _check_rate_limit(client_ip)

    sid = memory_store.ensure_session(chat.session_id)

    # 单会话并发拦截：避免同一会话在未生成完毕时重复提交
    if sid in _ACTIVE_SESSIONS:
        raise HTTPException(
            status_code=409,
            detail="当前会话正在生成回答中，请等待上一轮完成或中止后再试。"
        )

    async def event_generator() -> AsyncIterator[str]:
        _ACTIVE_SESSIONS.add(sid)
        metrics.active_streams += 1
        start_time = time.time()
        first_token_recorded = False

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
                    if node == "web_search":
                        metrics.inc_web_fallback()
                    if node in ("transform_query", "web_search"):
                        yield _sse({"type": "reset"})
                    yield _sse({"type": "status", "message": NODE_STATUS[node]})
                    if node == "generate":
                        yield _sse({"type": "reset"})

                if kind == "on_chat_model_stream" and node == "generate":
                    chunk = (event.get("data") or {}).get("chunk")
                    text = _chunk_text(getattr(chunk, "content", None) if chunk is not None else None)
                    if text:
                        if not first_token_recorded:
                            ttft = time.time() - start_time
                            metrics.record_ttft(ttft)
                            first_token_recorded = True
                        yield _sse({"type": "token", "content": text})

                if kind == "on_chain_end" and node == "generate" and name == "generate":
                    output = (event.get("data") or {}).get("output")
                    if isinstance(output, dict) and output.get("generation"):
                        final_answer = output["generation"]

            if aborted or await request.is_disconnected():
                yield _sse({"type": "aborted"})
            else:
                memory_store.add_turn(sid, chat.question, final_answer)
                metrics.record_duration(time.time() - start_time)
                metrics.inc_request("/chat/stream", 200)
                yield _sse({"type": "done", "answer": final_answer, "session_id": sid})
        except asyncio.CancelledError:
            yield _sse({"type": "aborted"})
            raise
        except Exception as exc:
            metrics.inc_error("/chat/stream", type(exc).__name__)
            metrics.inc_request("/chat/stream", 500)
            yield _sse({"type": "error", "message": str(exc)})
        finally:
            _ACTIVE_SESSIONS.discard(sid)
            metrics.active_streams = max(0, metrics.active_streams - 1)

    return StreamingResponse(
        event_generator(),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "X-Accel-Buffering": "no",
        },
    )
