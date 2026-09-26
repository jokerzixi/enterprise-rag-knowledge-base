"""
用 Laya Choice 做意图路由（vectorstore / web_search），失败或低置信度时返回 None 供调用方降级。
"""

from __future__ import annotations

from typing import Optional

from laya.laya_client import laya_client
from utils.env_utils import LAYA_CONFIDENCE_MIN, LAYA_ENABLED
from utils.log_utils import log

ROUTE_INSTRUCTIONS = (
    "将用户问题路由到最合适的数据源。"
    "半导体工艺、设备、材料、光刻、刻蚀、沉积、CMP、EUV、芯片制造等相关问题选择知识库；"
    "天气、新闻、闲聊、时事、明显与半导体知识库无关的问题选择联网搜索。"
)

ROUTE_CRITERIA = {
    "vectorstore": (
        "半导体 / 芯片制造相关：光刻机、EUV、DUV、刻蚀、等离子体、CVD、PVD、ALD、"
        "CMP、掩模、光刻胶、离子注入、STI、HKMG、良率、封装、工艺流程等知识问答"
    ),
    "web_search": (
        "与本地半导体知识库无关：天气、时事新闻、闲聊寒暄、通用百科、"
        "需要实时信息或明显超出半导体制造知识范围的问题"
    ),
}

VALID_ROUTES = frozenset({"vectorstore", "web_search"})


def route_with_laya(question: str) -> Optional[str]:
    """
    尝试用 Laya 路由。

    Returns:
        "vectorstore" | "web_search"；不可用 / 低置信 / 非法标签时返回 None。
    """
    if not LAYA_ENABLED:
        return None

    q = (question or "").strip()
    if not q:
        return None

    try:
        result = laya_client.choice(
            state=q,
            instructions=ROUTE_INSTRUCTIONS,
            criteria=ROUTE_CRITERIA,
            question_id="route",
        )
    except Exception as exc:
        log.warning(f"---Laya 路由失败，将降级 LLM: {exc}---")
        return None

    choice = (result.get("choice") or "").strip().lower()
    confidence = float(result.get("confidence") or 0.0)
    probs = result.get("probabilities") or {}

    log.info(
        f"---Laya 路由结果: choice={choice}, confidence={confidence:.4f}, "
        f"probs={probs}---"
    )

    if choice not in VALID_ROUTES:
        log.warning(f"---Laya 返回非法路由标签 [{choice}]，降级 LLM---")
        return None

    if confidence < LAYA_CONFIDENCE_MIN:
        log.warning(
            f"---Laya 置信度 {confidence:.4f} < {LAYA_CONFIDENCE_MIN}，降级 LLM---"
        )
        return None

    return choice
