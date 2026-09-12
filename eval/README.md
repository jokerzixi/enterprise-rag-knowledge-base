# RAGAS 评测

## 作用

对 Adaptive RAG（检索上下文 + 生成答案）做量化打分，常用指标：

| 指标 | 含义 |
|------|------|
| faithfulness | 答案是否忠于检索上下文（防胡编） |
| answer_relevancy | 答案是否切题 |
| context_recall | 检索内容是否覆盖标准答案要点 |
| context_precision | 检索到的上下文是否精炼相关 |

## 准备

```powershell
conda activate rag_env
pip install "ragas>=0.2.0" datasets
```

确保 Milvus 已启动、知识库有数据；`.env` 中 DeepSeek / DashScope 可用。

## 运行

```powershell
cd 项目根目录
python eval/run_ragas.py --limit 2 --metrics fast   # 先小样本试跑
python eval/run_ragas.py                            # 全量默认指标
```

报告输出：`eval/ragas_report.json`

## 扩充金标

编辑 `eval/gold_set.json`，每条至少：

```json
{
  "question": "用户问题",
  "ground_truth": "标准参考答案（用于 context_recall 等）"
}
```

建议按业务场景持续补充 20～50 条，并在改检索/切块/Prompt 后回归跑分。
