import os
from typing import List

from langchain_core.documents import Document

from utils.env_utils import DASHSCOPE_API_KEY
from utils.log_utils import log


def rerank(state: dict) -> dict:
    """
    使用 Cross-Encoder (DashScope gte-rerank) 对多路召回的初筛文档进行深度语义重排。
    筛选出最具相关性的 Top 4 篇高质量文档送入后续评估与生成流程。
    """
    log.info("---CROSS-ENCODER RERANKING---")
    question = state.get("question", "")
    documents: List[Document] = state.get("documents", [])
    top_n = min(4, len(documents))

    if not documents or len(documents) <= 1:
        log.info("---文档数量 <= 1，跳过重排---")
        return {"documents": documents, "question": question}

    # 1. 优先尝试 DashScope gte-rerank
    api_key = (os.getenv("DASHSCOPE_API_KEY") or DASHSCOPE_API_KEY or "").strip()
    if api_key:
        try:
            import dashscope
            from dashscope import TextReRank

            dashscope.api_key = api_key
            doc_texts = [d.page_content[:2000] for d in documents]

            resp = TextReRank.call(
                model="gte-rerank",
                query=question,
                documents=doc_texts,
                top_n=top_n,
                return_documents=False,
            )

            if resp.status_code == 200 and resp.output and hasattr(resp.output, "results"):
                results = resp.output.results
                reranked_docs: List[Document] = []
                for item in results:
                    idx = getattr(item, "index", None)
                    score = getattr(item, "relevance_score", 0.0)
                    if idx is not None and 0 <= idx < len(documents):
                        doc = documents[idx]
                        doc.metadata["rerank_score"] = round(float(score), 4)
                        reranked_docs.append(doc)

                if reranked_docs:
                    log.info(f"---DashScope Rerank 完成，从 {len(documents)} 篇筛选保留 Top {len(reranked_docs)} 篇---")
                    return {"documents": reranked_docs, "question": question}
            else:
                log.warning(f"---DashScope Rerank 调用非200: {resp.message if hasattr(resp, 'message') else resp}，执行平滑降级---")
        except Exception as exc:
            log.warning(f"---DashScope Rerank 异常: {exc}，执行平滑降级---")

    # 2. 降级方案：保留前 top_n 篇，保障后续流程不中断
    log.info(f"---使用默认截断降级策略，保留前 {top_n} 篇文档---")
    for doc in documents[:top_n]:
        doc.metadata.setdefault("rerank_score", 1.0)

    return {"documents": documents[:top_n], "question": question}
