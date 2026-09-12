from typing import TypedDict, List

from langchain_core.documents import Document


class GraphState(TypedDict):
    """
    表示图处理流程的状态信息

    属性说明：
        question: 用于检索/生成的问题（可为上下文改写后的独立问题）
        generation: 语言模型生成的回答文本
        transform_count: 传换查询的次数
        documents: 检索到的相关文档列表
        local_best_answer: 转联网前本地库的最佳回答
        searched_web: 是否已经执行过联网搜索（防止死循环）
        chat_history: 多轮对话历史文本
    """

    question: str
    transform_count: int
    generation: str
    documents: List[Document]
    local_best_answer: str
    searched_web: bool
    chat_history: str
