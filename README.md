# Enterprise RAG Knowledge Base (企业级双路混合检索 RAG 问答系统)

基于 LangGraph、Milvus 和 FastAPI 构建的企业级高级 RAG（检索增强生成）系统。本项目采用 Agentic Workflow 设计，具备高精度的稠密与稀疏双路混合检索能力，内置严格的防幻觉裁判机制与动态网络搜索兜底策略。

由于采用标准化的 FastAPI 前后端分离架构，该系统的后端服务可无缝接入 Web 网页端、微信小程序等多端应用。

## 核心特性 (Core Features)

* **Agentic RAG 工作流 (基于 LangGraph)：**
  * 摒弃传统的线性 RAG，采用图状态机（StateGraph）管理对话流。
  * 包含查询重写（Query Transform）、文档相关性评分（Grade Documents）、生成结果幻觉校验（Grade Hallucinations）以及答案匹配度评估（Grade Answer）。
* **高精度双路混合检索 (Milvus Hybrid Search)：**
  * **稠密向量 (Dense)：** 捕获深层语义关联，实现跨语言、跨表述的意图匹配。
  * **稀疏向量 (Sparse/BM25)：** 锁定精准的行业术语和专有型号。
  * **RRF 排序融合：** 采用 $RRF\_Score = \frac{1}{k + Rank_{dense}} + \frac{1}{k + Rank_{sparse}}$ 算法对双路召回结果进行重排，输出最高质量上下文。
* **智能熔断与网络搜索兜底 (Circuit Breaker & Web Search)：**
  * 自动路由识别问题类型（本地知识库 vs 公网开放问题）。
  * 在知识库检索失败或多次生成引发“幻觉”时，触发熔断机制，自动引入外部 Web 搜索（Web Search Node）获取最新信息。
* **高效文档解析与入库：**
  * 使用 `SemanticChunker` 结合百分位数阈值进行细粒度语义切片。
  * 自动补全缺失的元数据（如 `title`, `category_depth`），确保多格式 Markdown 文件的稳定向量化入库。

## 🛠️ 技术栈 (Tech Stack)

* **应用层与工作流:** LangChain, LangGraph, LangSmith (可观测性)
* **后端 Web 框架:** FastAPI, Uvicorn
* **向量数据库:** Milvus (Docker 部署, 配合 Attu 可视化)
* **大语言模型与嵌入:** 兼容 DeepSeek / OpenAI API
* **前端展示:** Vanilla HTML/CSS/JS (原生 Fetch API 与 DOM 渲染)

## 项目结构 (Project Structure)

```text
RAG_PROJECT/
├── datas/
│   └── md/                     # 存放待入库的 Markdown 格式企业文档
├── documents/
│   ├── markdown_parser.py      # Markdown 解析与 Semantic 切块逻辑
│   ├── milvus_db.py            # Milvus 双路混合检索与 RRF 配置
│   └── write_milvus.py         # 向量化与多进程数据写入脚本
├── graph2/
│   ├── graph_2.py              # LangGraph 核心工作流定义与编译
│   ├── graph_state2.py         # 图状态 (GraphState) 定义
│   ├── retrieve_node.py        # 检索节点
│   ├── generate_node2.py       # 生成节点
│   ├── web_search_node.py      # 网络搜索兜底节点
│   └── grade_*.py              # 各种 LLM 裁判打分链 (幻觉/相关性等)
├── main.py                     # FastAPI 后端服务入口
├── index.html                  # 交互式问答前端页面
├── .env                        # 环境变量 (API Keys, 数据库连接等)
└── .gitignore                  # Git 忽略配置
