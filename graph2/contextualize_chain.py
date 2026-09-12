from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

from llm_models.all_llm import llm

contextualize_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "你会把用户的追问改写成独立、完整、可检索的问题。\n"
            "依据聊天历史补全省略的主语/对象，但不要回答问题，只输出改写后的问题本身。\n"
            "如果追问已经完整，可基本保持原意，仅做轻微润色。",
        ),
        (
            "human",
            "聊天历史：\n{chat_history}\n\n最新用户问题：{question}\n\n请输出改写后的独立问题：",
        ),
    ]
)

contextualize_chain = contextualize_prompt | llm | StrOutputParser()


def build_standalone_question(question: str, chat_history: str) -> str:
    """有历史时将追问改写成独立问题；无历史则原样返回。"""
    history = (chat_history or "").strip()
    if not history:
        return question
    rewritten = contextualize_chain.invoke(
        {"question": question, "chat_history": history}
    ).strip()
    return rewritten or question
