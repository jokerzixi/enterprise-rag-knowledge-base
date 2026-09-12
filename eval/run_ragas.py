"""
使用 RAGAS 评估本项目 Adaptive RAG 的检索与生成质量。

前置：
  1. Milvus 已启动且知识库有数据
  2. conda activate rag_env
  3. pip install ragas datasets

用法（项目根目录）：
  python eval/run_ragas.py
  python eval/run_ragas.py --limit 3
  python eval/run_ragas.py --gold eval/gold_set.json --out eval/ragas_report.json

指标说明（默认）：
  - faithfulness      答案是否忠实于检索上下文（防幻觉）
  - answer_relevancy  答案与问题的相关性
  - context_recall    检索上下文是否覆盖标准答案要点（需 ground_truth）
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


def _strip_answer_header(text: str) -> str:
    """去掉系统追加的来源头/引用，减少对评分噪声。"""
    if not text:
        return ""
    lines = text.splitlines()
    # 去掉开头的【回答来源：...】块
    while lines and (lines[0].startswith("【回答来源") or not lines[0].strip()):
        lines.pop(0)
    if lines and "知识库检索结果" in lines[0]:
        lines.pop(0)
    body = "\n".join(lines).strip()
    # 去掉文末系统引用
    marker = "【知识库引用】"
    if marker in body:
        body = body.split(marker, 1)[0].strip()
    marker2 = "参考来源"
    # 仅当作为小节标题出现时截断
    for sep in ("\n参考来源\n", "\n【参考来源】", "\n参考来源："):
        if sep in body:
            body = body.split(sep, 1)[0].strip()
    return body


def run_one(question: str) -> dict[str, Any]:
    from graph2.graph_2 import graph

    state = graph.invoke(
        {
            "question": question,
            "transform_count": 0,
            "searched_web": False,
            "chat_history": "",
        }
    )
    docs = state.get("documents") or []
    if not isinstance(docs, list):
        docs = [docs]
    contexts = []
    for d in docs:
        content = getattr(d, "page_content", None) or str(d)
        if content:
            contexts.append(content)
    answer = _strip_answer_header(state.get("generation") or "")
    return {
        "user_input": question,
        "retrieved_contexts": contexts,
        "response": answer,
        "searched_web": bool(state.get("searched_web")),
    }


def build_dataset(gold_path: Path, limit: int | None):
    from datasets import Dataset

    items = json.loads(gold_path.read_text(encoding="utf-8"))
    if limit is not None:
        items = items[: max(0, limit)]

    rows = {
        "user_input": [],
        "retrieved_contexts": [],
        "response": [],
        "reference": [],
    }
    meta = []

    print(f"共 {len(items)} 条金标，开始跑图取答案…")
    for i, item in enumerate(items, 1):
        q = item["question"]
        gt = item.get("ground_truth") or item.get("reference") or ""
        print(f"  [{i}/{len(items)}] {q}")
        try:
            one = run_one(q)
        except Exception as exc:
            print(f"    ! 跑图失败: {exc}")
            one = {
                "user_input": q,
                "retrieved_contexts": [],
                "response": "",
                "searched_web": False,
            }
        rows["user_input"].append(one["user_input"])
        rows["retrieved_contexts"].append(one["retrieved_contexts"] or [""])
        rows["response"].append(one["response"] or "")
        rows["reference"].append(gt)
        meta.append({"searched_web": one.get("searched_web", False)})
        print(
            f"    contexts={len(one['retrieved_contexts'])}, "
            f"web={one.get('searched_web')}, "
            f"answer_len={len(one['response'])}"
        )

    return Dataset.from_dict(rows), meta


def evaluate_ragas(dataset, metrics_mode: str = "default"):
    from langchain_openai import ChatOpenAI
    from ragas import evaluate
    from ragas.embeddings import LangchainEmbeddingsWrapper
    from ragas.llms import LangchainLLMWrapper
    from ragas.metrics import (
        Faithfulness,
        AnswerRelevancy,
        ContextRecall,
        ContextPrecision,
    )

    from llm_models.embeddings_model import bge_embedding
    from utils.env_utils import DEEPSEEK_API_KEY

    # RAGAS 评判模型建议 temperature=0
    # DeepSeek 仅支持 n=1，AnswerRelevancy 默认 strictness=3 会触发 n>1 报错
    judge = ChatOpenAI(
        temperature=0,
        model="deepseek-chat",
        api_key=DEEPSEEK_API_KEY,
        base_url="https://api.deepseek.com",
        n=1,
    )
    ragas_llm = LangchainLLMWrapper(judge)
    ragas_emb = LangchainEmbeddingsWrapper(bge_embedding)

    faithfulness = Faithfulness()
    answer_relevancy = AnswerRelevancy(strictness=1)
    context_recall = ContextRecall()
    context_precision = ContextPrecision()

    if metrics_mode == "fast":
        metrics = [faithfulness, answer_relevancy]
    else:
        metrics = [faithfulness, answer_relevancy, context_recall, context_precision]

    print(f"开始 RAGAS 评分（metrics={metrics_mode}）…")
    result = evaluate(
        dataset=dataset,
        metrics=metrics,
        llm=ragas_llm,
        embeddings=ragas_emb,
    )
    return result


def main():
    parser = argparse.ArgumentParser(description="RAGAS 评估 Adaptive RAG")
    parser.add_argument("--gold", default=str(ROOT / "eval" / "gold_set.json"))
    parser.add_argument("--out", default=str(ROOT / "eval" / "ragas_report.json"))
    parser.add_argument("--limit", type=int, default=None, help="只跑前 N 条（调试用）")
    parser.add_argument(
        "--metrics",
        choices=["default", "fast"],
        default="default",
        help="fast=仅 faithfulness+relevancy；default 含 context_recall/precision",
    )
    args = parser.parse_args()

    gold_path = Path(args.gold)
    if not gold_path.exists():
        raise SystemExit(f"金标文件不存在: {gold_path}")

    dataset, meta = build_dataset(gold_path, args.limit)
    result = evaluate_ragas(dataset, metrics_mode=args.metrics)

    # 汇总
    try:
        df = result.to_pandas()
        summary = {c: float(df[c].mean()) for c in df.columns if c not in (
            "user_input", "retrieved_contexts", "response", "reference"
        )}
    except Exception:
        summary = {}
        df = None

    print("\n======== RAGAS 平均分 ========")
    for k, v in summary.items():
        print(f"  {k}: {v:.4f}")

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "summary": summary,
        "meta": meta,
        "rows": df.to_dict(orient="records") if df is not None else None,
    }
    out_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\n报告已写入: {out_path}")


if __name__ == "__main__":
    main()
