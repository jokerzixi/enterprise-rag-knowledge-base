from typing import List

from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field

from llm_models.all_llm import llm


class ExpandedQueries(BaseModel):
    """相关问题 / 检索词扩展结果"""

    queries: List[str] = Field(
        description="2到4条与原问题相关、更利于向量库检索的查询语句，可包含同义改写、上下位概念与领域相关扩展"
    )


structured_expander = llm.with_structured_output(ExpandedQueries, method="function_calling")

expand_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "你是半导体/芯片制造领域的查询扩展助手。"
            "用户问题可能比较宽泛，你需要生成2到4条相关检索查询，帮助在知识库中召回更多相关文档。\n"
            "要求：\n"
            "1. 保留原问题核心意图，不要跑题。\n"
            "2. 可扩展同义词、上下位概念、常见关联技术词。"
            "例如「光刻机」可扩展为「EUV光刻机」「DUV光刻」「光刻技术原理」「光刻胶与光刻工艺」等。\n"
            "3. 每条查询简短、适合检索，不要解释。\n"
            "4. 不要重复原问题原文；原问题会由系统另行检索。",
        ),
        ("human", "原问题：{question}"),
    ]
)

query_expand_chain = expand_prompt | structured_expander
