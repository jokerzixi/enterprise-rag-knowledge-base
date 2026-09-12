from typing import List

from langchain_core.documents import Document

from graph2.query_expand_chain import query_expand_chain
from tools.retriever_tools import retriever
from utils.log_utils import log


def _doc_key(doc: Document) -> str:
    meta = doc.metadata or {}
    for k in ("pk", "id", "element_id"):
        if meta.get(k) is not None:
            return f"{k}:{meta.get(k)}"
    return doc.page_content[:240]


def _merge_documents(doc_lists: List[List[Document]], limit: int = 8) -> List[Document]:
    merged: List[Document] = []
    seen = set()
    for docs in doc_lists:
        for doc in docs or []:
            key = _doc_key(doc)
            if key in seen:
                continue
            seen.add(key)
            merged.append(doc)
            if len(merged) >= limit:
                return merged
    return merged


def retrieve(state):
    """
    检索相关文档：先对问题做相关扩展，再多路检索并去重合并。
    不改写用于回答的 question，仅扩展检索词。
    """
    log.info("---去知识库中检索文档（含相关问题扩展）---")
    question = state["question"]

    queries = [question]
    try:
        expanded = query_expand_chain.invoke({"question": question})
        extra = [q.strip() for q in (expanded.queries or []) if q and q.strip()]
        for q in extra:
            if q not in queries:
                queries.append(q)
        log.info(f"---查询扩展结果: {queries}---")
    except Exception as exc:
        log.warning(f"---查询扩展失败，回退单查询检索: {exc}---")

    doc_lists = []
    for q in queries:
        try:
            docs = retriever.invoke(q)
            doc_lists.append(docs if isinstance(docs, list) else [docs])
            log.info(f"---子查询「{q}」召回 {len(doc_lists[-1])} 条---")
        except Exception as exc:
            log.warning(f"---子查询「{q}」检索失败: {exc}---")

    documents = _merge_documents(doc_lists, limit=8)
    log.info(f"---合并去重后文档数: {len(documents)}---")
    return {"documents": documents, "question": question}
