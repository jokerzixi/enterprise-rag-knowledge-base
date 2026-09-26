# 基于 Laya (System-1) 决策模型的企业知识库与智能记忆系统改造方案

> **文档版本**：v1.0.0  
> **编写日期**：2026-09-25  
> **技术栈**：Laya (421M ModernBERT-large) / LangGraph / Milvus / Redis / DeepSeek-Chat / FastAPI  
> **关联理论**：UT Dallas《Jev-Mem: System-One-Controlled Agentic Memory for Efficient AI Agents》

---

## 1. 项目背景与技术定位

### 1.1 现有系统痛点分析
当前半导体企业知识库（`RAG_PROJECT`）采用基于生成式大模型（`deepseek-chat`）的 Adaptive RAG 架构。尽管该架构在问答质量上表现优异，但在工程性能与多轮记忆层面存在显著瓶颈：
1. **意图路由过重（高时延与成本）**：首节点意图识别采用大模型 Function Calling，单次推理耗时 800ms~1500ms，显著拖慢首字延迟（TTFT）；
2. **检索初筛与打分冗余**：初筛阶段调用 DashScope `gte-rerank` 结合大模型 `grade_documents` 对候选切片逐一评判，多轮网络往返与大模型计算带来了 500ms~1200ms 的额外开销；
3. **长期记忆机制缺失与噪音污染**：当前会话历史（`conversation_memory.py`）仅保存简单的最近几轮对话，缺乏“用户画像/偏好记忆（Profile/History）”，且“好的”、“收到”等无效交互无差别存入，导致记忆库膨胀与上下文污染。

### 1.2 Laya 模型的核心优势
**Laya** 是 Convai Innovations 开源的本地化“系统一（System-1）”快思考决策模型（基于 421M ModernBERT-large 架构，开源 Apache 2.0 协议，作为商用 Jev 服务的本地化平替）：
* **非自回归单步决策**：不生成冗长文本，专注在单次前向传播中输出结构化分类、评分与布尔判定；
* **极速响应与超低开销**：单次推理时延稳定在 **30ms~40ms**，显存占用仅约 **500MB (INT8) ~ 1GB (FP16)**；
* **天然契合 Agentic Memory 架构**：正如 UT Dallas 提出的 **Jev-Mem** 论文所述，通过将记忆层与检索层的感知/分类/打分下放给 System-1 模型，将高推理成本的 System-2 生成模型（LLM）解放出来，系统吞吐量与时延提升数倍。

---

## 2. Laya 原语与系统核心卡点映射

根据业务框架图，Laya 原语与系统核心卡点的对应关系如下：

| 卡点环节 | 业务痛点 | Laya 核心原语 | 原方案耗时 | Laya 方案耗时 |
| :--- | :--- | :--- | :--- | :--- |
| **卡点 1：记忆路由分发<br/>(Memory Routing)** | 每次都查向量库浪费算力，且不知该查通用知识、用户记忆、专业库还是复合查询 | **`Choice` 原语**：在 30ms 内完成意图 4 分流（`general` / `user_memory` / `doc_rag` / `hybrid`） | 1000ms+ (LLM) | **~30ms** |
| **卡点 2：上下文相关性初筛<br/>(Context Pruning)** | 向量库 Top-K 召回包含很多无关切片，强行拼入 Prompt 会引发模型幻觉与上下文挤占 | **`Score` 原语**：对 (Query, Document) 快速语义打分，快速剔除 $< 0.75$ 的低分噪声切片 | 500ms+ (Rerank+LLM) | **~35ms (单批并发)** |
| **卡点 3：记忆写入守门<br/>(Memory Write Filter)** | 对话中充斥大量客套话（“谢谢”、“知道了”），直接持久化会导致长期记忆库被污染与膨胀 | **`Noul (Boolean)` + `Score` 原语**：异步判断新对话是否包含重要事实/用户偏好并赋权 | 800ms+ 或无过滤 | **~30ms (异步无感知)** |

---

## 3. Laya 部署与领域微调方案 (Deployment & Domain Adaptation)

### 3.1 部署架构：Sidecar 伴随容器模式
为确保纯模型推理时延死守在 30ms 级别，采用 **Sidecar 容器 / 同机独立常驻服务** 模式：

```mermaid
flowchart LR
    subgraph Host["宿主机 / K8s Pod (局域网 IPC / Localhost)"]
        RAGApp["FastAPI 主服务 (Python 3.11)<br/>RAG_PROJECT (main.py)"]
        LayaSidecar["Laya System-1 服务 (ONNX / TensorRT / laya[serve])<br/>常驻 GPU 显存 (1GB FP16)"]
        RAGApp <-->|HTTP / gRPC (网络耗时 < 2ms)| LayaSidecar
    end
```

* **显存与硬件开销**：421M 参数常驻 GPU 显存仅需约 **1GB**（INT8 量化后约 **500MB**），可与本地 Milvus 或 Embedding 模型平稳共存；
* **服务暴露接口**：使用 `laya[serve]` 暴露极简 HTTP/gRPC 端点（默认端口 `http://127.0.0.1:8005/v1/systemone`）。

### 3.2 领域微调与自适应训练 (Domain Adaptation)
Laya 预训练通用权重在半导体垂直专业场景的初始意图识别率约为 40%~50%，需通过领域自适应微调将其快速提升至 **90%+**：

```text
微调策略要点：
1. 样本构建：整理 200 ~ 500 条半导体典型交互样本：
   - 标注不同意图类别（通用闲聊、个人偏好、工艺技术问题、复合问题）；
   - 标注切片相关性得分（0.0 ~ 1.0）；
   - 标注对话是否具有长期记忆沉淀价值（True/False）。
2. 参数高效微调 (PEFT)：
   - 采用 LoRA 对 ModernBERT 主干注意力权重进行轻量微调（Rank=8, Alpha=16）；
   - 或仅冻结主干、微调顶层分类/打分 Head 层；
3. 训练成本：200~500 条样本在单张消费级 GPU（如 RTX 3060/4090）上仅需 10~15 分钟即可完成收敛。
```

---

## 4. 系统目标架构蓝图（三卡点闭环）

改造后的整体数据与状态机流程图如下：

```mermaid
flowchart TD
  UserQuery([用户输入 User Query]) --> Step0[指代消解: 还原独立问题]
  Step0 --> Gate1{卡点 1: 记忆路由 (Laya Choice)}
  
  Gate1 -->|闲聊/通用知识| GenGeneral[直接 LLM 生成 (无需检索)]
  Gate1 -->|用户个性偏好| RetProfile[检索用户偏好记忆库 (Profile/History)]
  Gate1 -->|专业业务问题| RetKB[检索半导体企业知识库 (Milvus RAG)]
  Gate1 -->|复合问题| RetHybrid[双路联合检索 (Profile + Milvus)]
  
  RetProfile --> Gate2
  RetKB --> Gate2
  RetHybrid --> Gate2
  
  subgraph Pruning["卡点 2: 上下文初筛与剪枝 (Laya Score)"]
    Gate2{相关性打分与剪枝}
    Gate2 -->|高相关 (Score >= 0.75)| Assemble[组装优质精炼上下文]
    Gate2 -->|低相关噪声 (< 0.75)| DropNoise[直接剪枝丢弃 (防上下文污染)]
  end

  Assemble --> LLMGen[交付大模型生成 (DeepSeek-Chat)]
  GenGeneral --> ReturnAns([返回用户回答 / SSE Stream])
  LLMGen --> ReturnAns

  ReturnAns -.->|异步解耦执行| Gate3{卡点 3: 记忆写入守门 (Laya Noul & Score)}
  
  subgraph MemoryGate["卡点 3: 记忆沉淀机制"]
    Gate3 -->|Noul=True 且含高价值偏好| WriteLongTerm[提取事实写入长期画像库 (Redis/SQLite)]
    Gate3 -->|Noul=False 无长期价值会话| DiscardMem[直接丢弃 (防止记忆库膨胀)]
  end
```

---

## 5. 项目源码具体修改方案

### 5.1 目录结构调整
在 `RAG_PROJECT` 中新增 `laya/` 适配目录与长期记忆存储模块：

```text
RAG_PROJECT/
├── laya/                      # ★ 新增：Laya System-1 客户端与决策封装
│   ├── __init__.py
│   ├── laya_client.py         # Laya HTTP/SDK 通信客户端
│   ├── laya_router.py         # 卡点 1：Choice 路由分发器
│   ├── laya_pruner.py         # 卡点 2：Score 上下文剪枝器
│   └── laya_memory_filter.py  # 卡点 3：Noul+Score 记忆守门器
├── utils/
│   ├── conversation_memory.py # 现有短期多轮历史
│   └── user_profile_memory.py # ★ 新增：用户长期偏好/事实画像库
├── graph2/
│   ├── graph_state2.py        # 状态对象扩充（增加 user_profile 等字段）
│   ├── graph_laya.py          # ★ 新增：基于 Laya 三卡点的全新状态图
│   └── retriever_node.py      # 适配双路检索与初筛节点
└── main.py                    # 接入卡点 3 异步记忆写入任务
```

---

### 5.2 核心代码设计与实现细节

#### 模块 1：Laya 基础客户端封装（`laya/laya_client.py`）
负责向 Laya Sidecar 服务发送结构化决策请求，内置超时与平滑降级机制：

```python
import os
import requests
from typing import Dict, Any, List, Optional
from utils.log_utils import log

LAYA_SERVER_URL = os.getenv("LAYA_SERVER_URL", "http://127.0.0.1:8005/v1/systemone")

class LayaClient:
    """与 Laya 伴随服务通信的高性能客户端"""

    def __init__(self, endpoint: str = LAYA_SERVER_URL, timeout: float = 0.2):
        self.endpoint = endpoint
        self.timeout = timeout  # 200ms 超时保护

    def choice(self, state: str, instructions: str, options: List[str]) -> str:
        """Laya Choice 原语：单选路由"""
        payload = {
            "state": state,
            "type": "choice",
            "instructions": instructions,
            "options": options
        }
        resp = requests.post(f"{self.endpoint}/choice", json=payload, timeout=self.timeout)
        resp.raise_for_status()
        return resp.json().get("selected")

    def score(self, query: str, context: str) -> float:
        """Laya Score 原语：相关性打分 (0.0 ~ 1.0)"""
        payload = {"query": query, "context": context}
        resp = requests.post(f"{self.endpoint}/score", json=payload, timeout=self.timeout)
        resp.raise_for_status()
        return float(resp.json().get("score", 0.0))

    def noul(self, state: str, question: str) -> bool:
        """Laya Noul 原语：布尔真假判定"""
        payload = {"state": state, "question": question}
        resp = requests.post(f"{self.endpoint}/noul", json=payload, timeout=self.timeout)
        resp.raise_for_status()
        return bool(resp.json().get("noul", False))

laya_client = LayaClient()
```

---

#### 模块 2：卡点 1——四路记忆路由分发（`laya/laya_router.py`）
代替原先的 `query_route_chain.py`，实现 30ms 内精准四路分流：

```python
from laya.laya_client import laya_client
from utils.log_utils import log

ROUTE_OPTIONS = [
    "general_chat",      # 闲聊 / 通用常识 / 天气（无需检索）
    "user_preference",  # 用户个人偏好 / 习惯 / 历史背景（查用户记忆库）
    "domain_knowledge",  # 半导体工艺、材料、设备技术问题（查知识库）
    "hybrid_composite"   # 既涉及用户背景又涉及工艺规格的复合问题（双路检索）
]

ROUTE_INSTRUCTIONS = """
请准确识别用户提问的核心意图类别：
- general_chat: 问候、闲聊、编写代码通用语法、天气等非半导体通用问题；
- user_preference: 询问用户之前提到的偏好、身份、项目背景、角色定位等个人记忆；
- domain_knowledge: 光刻、刻蚀、CMP、薄膜沉积、量测等半导体专业技术问题；
- hybrid_composite: 结合用户上下文偏好与半导体专业工艺的复合问题（例如：按照我负责的制程分析该故障）。
"""

def route_user_query(question: str) -> str:
    """卡点 1：基于 Laya Choice 的毫秒级记忆意图路由"""
    try:
        decision = laya_client.choice(
            state=f"用户提问：{question}",
            instructions=ROUTE_INSTRUCTIONS,
            options=ROUTE_OPTIONS
        )
        log.info(f"---卡点 1 [Laya Choice] 决策结果: {decision}---")
        return decision
    except Exception as exc:
        log.warning(f"---Laya 路由异常，平滑降级至 domain_knowledge: {exc}---")
        return "domain_knowledge"
```

---

#### 模块 3：卡点 2——上下文初筛与剪枝（`laya/laya_pruner.py`）
替代高耗时的 `gte-rerank` 与大模型 `grade_documents_node.py`，在 35ms 内剔除无关碎片：

```python
from typing import List
from langchain_core.documents import Document
from laya.laya_client import laya_client
from utils.log_utils import log

SCORE_THRESHOLD = 0.75  # 架构图设定的高相关判定阈值

def prune_contexts(question: str, documents: List[Document]) -> List[Document]:
    """卡点 2：基于 Laya Score 对候选切片进行快速打分与噪声剪枝"""
    if not documents:
        return []

    log.info(f"---卡点 2 [Laya Score] 开始对 {len(documents)} 篇文档进行打分初筛---")
    high_relevance_docs = []

    for doc in documents:
        try:
            score = laya_client.score(query=question, context=doc.page_content[:1500])
            doc.metadata["laya_score"] = score
            if score >= SCORE_THRESHOLD:
                high_relevance_docs.append(doc)
            else:
                log.info(f"---[Laya Prune] 剪枝低分切片 (score={score:.2f} < {SCORE_THRESHOLD})---")
        except Exception as exc:
            # 异常情况下保守保留，防止误伤有效信息
            doc.metadata["laya_score"] = 1.0
            high_relevance_docs.append(doc)

    log.info(f"---初筛完成：保留 {len(high_relevance_docs)} / {len(documents)} 篇高质切片---")
    return high_relevance_docs
```

---

#### 模块 4：卡点 3——记忆写入守门与长期用户画像库（`laya/laya_memory_filter.py`）
在用户收到流式响应后，后台**异步解耦**执行记忆守门，防止无效废话污染长期画像：

```python
from laya.laya_client import laya_client
from utils.user_profile_memory import user_profile_store
from utils.log_utils import log

MEMORY_GATE_QUESTION = "该轮对话是否包含用户的个人背景、工艺职责、机台偏好或具有长期参考价值的事实信息？"

async def memory_write_gatekeeper_task(session_id: str, user_id: str, question: str, answer: str):
    """卡点 3：基于 Laya Noul & Score 的异步记忆沉淀任务"""
    dialogue_state = f"用户提问：{question}\n助手回答：{answer}"

    try:
        # 1. 使用 Noul 进行布尔过滤（是否具有长期保存价值）
        has_valuable_memory = laya_client.noul(state=dialogue_state, question=MEMORY_GATE_QUESTION)

        if not has_valuable_memory:
            log.info(f"---卡点 3 [Laya Memory Gate]：无长期保存价值，直接丢弃避免记忆库膨胀---")
            return

        # 2. 对记忆重要度打分并沉淀至长期记忆库
        importance_score = laya_client.score(query="用户长期特征与工艺偏好", context=dialogue_state)
        log.info(f"---卡点 3 [Laya Memory Gate]：发现重要个人事实 (Score={importance_score:.2f})，写入长期记忆库---")

        user_profile_store.add_memory(
            user_id=user_id,
            fact_summary=f"Q: {question} | A: {answer}",
            weight=importance_score
        )
    except Exception as exc:
        log.error(f"---卡点 3 异步执行异常: {exc}---")
```

---

#### 模块 5：修改 FastAPI 服务主流程（`main.py`）
在 `main.py` 的 SSE 生成完毕事件触发后，加入异步后台任务：

```python
# main.py 片段
from fastapi import BackgroundTasks
from laya.laya_memory_filter import memory_write_gatekeeper_task

@app.post("/chat/stream")
async def chat_stream(chat: ChatRequest, request: Request, background_tasks: BackgroundTasks):
    # ... 原有流式生成逻辑 ...
    
    # 当流式传输完毕 (done) 之后，投递异步守门任务，完全不增加用户感知的响应耗时
    background_tasks.add_task(
        memory_write_gatekeeper_task,
        session_id=sid,
        user_id=getattr(chat, "user_id", "default_user"),
        question=chat.question,
        answer=final_answer
    )
    # ...
```

---

## 6. 改造前后性能与质量全维度对比

| 指标维度 | 原方案（DeepSeek Router + gte-rerank） | Laya 改造方案（三卡点闭环） | 预期优化成效 |
| :--- | :--- | :--- | :--- |
| **首字时间 (TTFT)** | $2.5\text{s} \sim 4.2\text{s}$ | **$0.8\text{s} \sim 1.5\text{s}$** | ⚡ **降低 60% 以上** |
| **意图路由耗时** | $\approx 1000\text{ms}$（大模型调用） | **$\approx 30\text{ms}$**（Laya Choice） | ⚡ **提速 30 倍** |
| **切片初筛耗时** | $\approx 600\text{ms}$（重排 + 逐个打分） | **$\approx 35\text{ms}$**（Laya Score） | ⚡ **提速 15 倍** |
| **上下文噪声率** | 中等（易将弱相关切片输入 LLM） | **极低（$<0.75$ 刚性剪枝）** | 🛡️ **有效抑制生成幻觉** |
| **记忆存储质量** | 简单滑动窗口（充满废话噪音） | **结构化高价值沉淀（守门过滤）** | 🧠 **长期记忆纯净度达 95%+** |
| **Token 运营成本** | 高（全流程多次调用大模型） | **低（System-1 分担决策负载）** | 💰 **降低 45%~60% Token 开销** |

---

## 7. 实施路线图建议

1. **阶段 1：部署与基准测试（Day 1~2）**：在本地/服务器拉起 Laya Sidecar 容器，验证 `Choice`、`Score`、`Noul` 接口延迟与 GPU 显存占用情况；
2. **阶段 2：数据准备与领域微调（Day 3~4）**：抽取本项目的 `gold_set.json` 及历史半导体问答生成 300 条标注样本，完成针对半导体业务的 LoRA 微调；
3. **阶段 3：卡点 1 & 卡点 2 接入状态机（Day 5~6）**：在 `graph_laya.py` 中替换路由节点与初筛剪枝节点，进行单测与 RAGAS 回归；
4. **阶段 4：卡点 3 长期记忆库上线（Day 7）**：接入 Redis 用户画像库与后台异步守门任务，完成整体验收。
