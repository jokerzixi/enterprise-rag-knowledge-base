"""
Laya System-1 HTTP 客户端。

协议对齐官方 `POST /v1/systemone`（与 Jev 兼容）：
  state + questions{ id: {type, instructions, criteria?} } → answers
"""

from __future__ import annotations

from typing import Any, Dict, Optional

import requests

from utils.env_utils import (
    LAYA_API_KEY,
    LAYA_MODEL,
    LAYA_SERVER_URL,
    LAYA_TIMEOUT_SECONDS,
)


def _resolve_systemone_url(endpoint: str) -> str:
    ep = (endpoint or "").rstrip("/")
    if ep.endswith("/systemone"):
        return ep
    if ep.endswith("/v1"):
        return f"{ep}/systemone"
    return f"{ep}/v1/systemone"


class LayaClient:
    """调用本地 / 远程 Laya serve 的轻量客户端。"""

    def __init__(
        self,
        endpoint: Optional[str] = None,
        timeout: Optional[float] = None,
        api_key: Optional[str] = None,
        model: Optional[str] = None,
    ):
        self.endpoint = endpoint or LAYA_SERVER_URL
        self.timeout = float(timeout if timeout is not None else LAYA_TIMEOUT_SECONDS)
        self.api_key = (api_key if api_key is not None else LAYA_API_KEY) or ""
        # multilingual 对中文更稳；可通过 env LAYA_MODEL 覆盖
        self.model = model if model is not None else (LAYA_MODEL or "convaiinnovations/laya-multilingual")

    def _headers(self) -> Dict[str, str]:
        headers = {"Content-Type": "application/json"}
        if self.api_key:
            headers["Authorization"] = f"Bearer {self.api_key}"
        return headers

    def system_one(
        self,
        state: str,
        questions: Dict[str, Dict[str, Any]],
        model: Optional[str] = None,
    ) -> Dict[str, Any]:
        """调用 POST /v1/systemone，返回完整 JSON。"""
        payload: Dict[str, Any] = {
            "state": state,
            "questions": questions,
        }
        use_model = model or self.model
        if use_model:
            payload["model"] = use_model

        url = _resolve_systemone_url(self.endpoint)
        resp = requests.post(
            url,
            json=payload,
            headers=self._headers(),
            timeout=self.timeout,
        )
        resp.raise_for_status()
        data = resp.json()
        if not isinstance(data, dict):
            raise ValueError(f"Laya 返回非 JSON 对象: {type(data)}")
        return data

    def choice(
        self,
        state: str,
        instructions: str,
        criteria: Dict[str, str],
        question_id: str = "route",
        model: Optional[str] = None,
    ) -> Dict[str, Any]:
        """
        Choice 原语封装。

        Returns:
            choice / confidence / probabilities / raw
        """
        questions = {
            question_id: {
                "type": "choice",
                "instructions": instructions,
                "criteria": criteria,
            }
        }
        data = self.system_one(state=state, questions=questions, model=model)
        answers = data.get("answers") or {}
        ans = answers.get(question_id) or {}
        if not ans:
            raise ValueError(f"Laya answers 缺少 {question_id}: {data}")

        choice = ans.get("choice")
        if not choice:
            raise ValueError(f"Laya choice 为空: {ans}")

        conf = ans.get("confidence")
        try:
            confidence = float(conf) if conf is not None else 0.0
        except (TypeError, ValueError):
            confidence = 0.0

        probs = ans.get("probabilities") or {}
        return {
            "choice": str(choice),
            "confidence": confidence,
            "probabilities": probs if isinstance(probs, dict) else {},
            "raw": ans,
        }


laya_client = LayaClient()
