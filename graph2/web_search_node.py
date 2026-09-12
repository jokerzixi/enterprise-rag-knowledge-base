from langchain_core.documents import Document

from llm_models.all_llm import web_search_tool
from utils.log_utils import log


def web_search(state):
    """
    基于问题进行网络搜索，并保留源链接便于溯源。
    """
    log.info("---WEB SEARCH---")
    question = state["question"]
    prev_generation = state.get("generation", "")

    docs = web_search_tool.invoke({"query": question})
    if not isinstance(docs, list):
        docs = [docs] if docs else []

    blocks = []
    for i, item in enumerate(docs, start=1):
        if isinstance(item, dict):
            title = item.get("title") or item.get("url") or f"来源{i}"
            url = item.get("url") or ""
            content = item.get("content") or item.get("snippet") or ""
            block = f"[{i}] {title}\n来源链接: {url}\n内容: {content}".strip()
        else:
            block = f"[{i}] {item}"
        blocks.append(block)

    web_results = Document(
        page_content="\n\n".join(blocks) if blocks else "未检索到有效的网络结果。",
        metadata={"source": "web_search"},
    )

    return {
        "documents": [web_results],
        "question": question,
        "local_best_answer": prev_generation,
        "searched_web": True,
    }
