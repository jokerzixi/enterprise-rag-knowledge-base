from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

from llm_models.all_llm import llm


def _local_citations(docs) -> str:
    """根据检索文档 metadata 去重生成知识库引用列表（系统拼接，不依赖模型编造）。"""
    if not docs:
        return ""
    if not isinstance(docs, list):
        docs = [docs]

    seen = set()
    lines = []
    for i, doc in enumerate(docs, 1):
        meta = getattr(doc, "metadata", None) or {}
        filename = (meta.get("filename") or "").strip()
        source = (meta.get("source") or "").strip()
        title = (meta.get("title") or "").strip()
        name = filename or source or f"chunk-{i}"
        if name in seen:
            continue
        seen.add(name)
        idx = len(lines) + 1
        if title and title != name:
            lines.append(f"- [{idx}] {title}（文件：{name}）")
        else:
            lines.append(f"- [{idx}] {name}")

    if not lines:
        return ""
    return "\n\n【知识库引用】\n" + "\n".join(lines)


def _format_docs_for_prompt(docs) -> str:
    """给上下文加编号，便于模型在正文中写「据 [1]」，引用列表仍由系统追加。"""
    if not docs:
        return ""
    if not isinstance(docs, list):
        docs = [docs]

    blocks = []
    for i, doc in enumerate(docs, 1):
        meta = getattr(doc, "metadata", None) or {}
        filename = (meta.get("filename") or meta.get("source") or "").strip()
        title = (meta.get("title") or "").strip()
        head_parts = [f"[{i}]"]
        if filename:
            head_parts.append(f"文件: {filename}")
        if title:
            head_parts.append(f"标题: {title}")
        head = " | ".join(head_parts)
        blocks.append(f"{head}\n{doc.page_content}")
    return "\n\n".join(blocks)


def generate(state):
    """
    生成回答：
    - 知识库：开头标明来自知识库；文末由系统追加【知识库引用】（filename/title）
    - 联网：开头标明本地未检索到足够内容、为联网总结，并附参考来源链接
    - 若有多轮历史，结合上下文理解指代与追问
    """
    question = state["question"]
    documents = state["documents"]
    searched_web = state.get("searched_web", False)
    chat_history = (state.get("chat_history") or "").strip() or "无"

    if searched_web:
        template = (
            "你是一个问答任务助手。请根据以下联网检索到的上下文回答问题。\n"
            "要求：\n"
            "1. 结合聊天历史理解指代（如“它/这个/上面说的”），给出完整、有用的直接回答；"
            "不要在正文开头写来源说明（来源说明由系统另加）。\n"
            "2. 必须在回答末尾增加「参考来源」小节，逐条列出标题与完整 URL，便于溯源。\n"
            "3. 不要编造上下文中不存在的链接。\n"
            "聊天历史：\n{chat_history}\n"
            "当前问题：{question}\n"
            "检索上下文：{context}\n"
            "回答："
        )
    else:
        template = (
            "你是一个问答任务助手。请根据以下知识库检索到的上下文回答问题。\n"
            "要求：\n"
            "1. 结合聊天历史理解指代与追问，根据检索上下文给出简洁、有用的回答；"
            "不要在正文开头写来源说明（来源说明由系统另加）。\n"
            "2. 如果上下文不足以回答，请直接说明，不要编造。\n"
            "3. 正文中可使用 [1]、[2] 指代检索片段；不要自行编造文件名或外链。"
            "知识库引用列表由系统自动追加，你不要输出「参考来源」小节。\n"
            "聊天历史：\n{chat_history}\n"
            "当前问题：{question}\n"
            "检索上下文：{context}\n"
            "回答："
        )

    prompt = PromptTemplate(
        template=template,
        input_variables=["question", "context", "chat_history"],
    )

    rag_chain = prompt | llm | StrOutputParser()

    if searched_web:
        def format_docs(docs):
            if isinstance(docs, list):
                return "\n\n".join(doc.page_content for doc in docs)
            return "\n\n" + docs.page_content

        context = format_docs(documents)
    else:
        context = _format_docs_for_prompt(documents)

    generation = rag_chain.invoke(
        {
            "context": context,
            "question": question,
            "chat_history": chat_history,
        }
    )

    if searched_web:
        header = (
            "【回答来源：联网搜索】\n"
            "本地知识库未检索到足够相关内容，以下为联网搜索总结，并附参考来源便于溯源。\n\n"
        )
        body = f"{header}{generation}"
        return {"documents": documents, "question": question, "generation": body}

    header = (
        "【回答来源：本地知识库】\n"
        "以下内容基于知识库检索结果生成。\n\n"
    )
    body = header + generation + _local_citations(documents)
    return {"documents": documents, "question": question, "generation": body}
