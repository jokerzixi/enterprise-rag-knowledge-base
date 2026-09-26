# RAG 企业知识库 · 半导体 Adaptive RAG

面向**半导体工艺 / 设备 / 材料**场景的检索增强问答系统：  
云端 MinerU 解析 → Milvus 混合检索 →（可选）Laya System-1 快路由 → LangGraph Adaptive RAG（含 Cross-Encoder 精排与纠错熔断；本地不足时 Tavily 联网）→ FastAPI SSE + 多会话 Web UI。

> 定位为**可演示的工程原型**（持久会话、知识库引用、RAGAS 评测、可选 Laya 路由）。上生产前请补齐鉴权、限流与合规。

仓库：<https://github.com/jokerzixi/enterprise-rag-knowledge-base>

---

## 功能一览

| 能力 | 说明 |
|------|------|
| Adaptive RAG + CRAG | 路由 → 检索 → 精排 → 文档打分 → 生成 → 幻觉/答案评估 → 改写重试 / 联网 |
| 混合检索 | Milvus Dense（HNSW）+ BM25 Sparse，RRF 融合；查询扩展后多路合并去重 |
| Cross-Encoder 精排 | DashScope `gte-rerank` 对召回块重排取 Top-N（失败则截断降级） |
| 可选 Laya 意图路由 | 本地 System-1 `choice` 分流 `vectorstore` / `web_search`；低置信或不可用回退 DeepSeek |
| 多轮 / 多会话 | 指代消解 + Redis / SQLite 会话记忆；前端侧栏隔离 `session_id` |
| 流式输出 | SSE：`status` / `token` / `reset` / `done`，支持客户端断开中止 |
| 知识库引用 | 本地回答由系统按 `filename` / `title` 拼接引用，降低来源编造 |
| 语料建设 | MinerU 解析、主题抓取、本地 Markdown 入库；**语料文件不随仓库分发，需自行合规准备** |
| 评测 | RAGAS（faithfulness / answer_relevancy）+ `web_fallback_rate` 联网率 KPI |
| 健康检查 | `GET /health`、`GET /metrics`（Prometheus 文本） |

---

## 系统架构

```text
┌─────────────┐     SSE/HTTP      ┌──────────────┐
│  index.html │ ───────────────► │   main.py    │
│ 多会话前端   │ ◄─────────────── │   FastAPI    │
└─────────────┘                   └──────┬───────┘
                                         │
          ┌──────────────────────────────┼──────────────────────────────┐
          ▼                              ▼                              ▼
   ┌──────────────┐            ┌────────────────┐            ┌─────────────┐
   │ Redis/SQLite │            │ graph2/        │            │ DeepSeek    │
   │ 会话记忆      │            │ LangGraph RAG  │───────────►│ + DashScope │
   └──────────────┘            └────────┬───────┘            └─────────────┘
                                        │
          ┌─────────────────────────────┼─────────────────────────────┐
          ▼                             ▼                             ▼
    ┌──────────┐                 ┌──────────┐                  ┌──────────┐
    │  Milvus  │                 │  Tavily  │                  │  MinerU  │
    │ 混合检索  │                 │ 联网兜底  │                  │ 云端解析  │
    └──────────┘                 └──────────┘                  └──────────┘
          ▲
          │ 可选
    ┌──────────┐
    │   Laya   │  System-1 意图路由（默认关闭）
    └──────────┘
```

### LangGraph 主流程（`graph2/`）

```mermaid
flowchart TD
  START([START]) --> route{问题路由<br/>Laya 可选 / DeepSeek 降级}
  route -->|vectorstore| retrieve[检索+查询扩展]
  route -->|web_search| web[Tavily 联网]
  retrieve --> rerank[gte-rerank 精排]
  rerank --> gradeDocs[文档相关性打分]
  gradeDocs -->|有相关文档| generate[生成回答]
  gradeDocs -->|无相关且可重试| transform[查询改写]
  gradeDocs -->|无相关且达上限| web
  transform --> retrieve
  web --> generate
  generate --> gradeAns{幻觉+答案评估}
  gradeAns -->|useful| END([END])
  gradeAns -->|not useful 可重试| transform
  gradeAns -->|本地仍不足| web
  gradeAns -->|not supported| generate
```

---

## 技术栈

| 层级 | 选型 |
|------|------|
| 编排 | LangChain / LangGraph |
| LLM | DeepSeek Chat（OpenAI 兼容） |
| Embedding / 精排 | DashScope `text-embedding-v3` / `gte-rerank` |
| 可选路由 | Laya System-1（`laya[serve]`，HTTP `/v1/systemone`） |
| 向量库 | Milvus Standalone（Dense HNSW + BM25 Sparse，RRF） |
| 联网搜索 | Tavily |
| 文档解析 | MinerU 云端 API |
| API | FastAPI + SSE |
| 前端 | 原生 HTML/CSS/JS（`index.html`） |
| 会话 | Redis（推荐）/ SQLite / 内存降级 |
| 评测 | RAGAS |

Python 建议：**3.11**，Conda 环境示例：`rag_env`。

---

## 目录结构

```text
RAG_PROJECT/
├── main.py                 # FastAPI：/chat、/chat/stream、/health、/metrics
├── index.html              # 多会话 Web UI
├── requirements.txt
├── .env.example            # 环境变量模板（无密钥；勿提交 .env）
├── CONTEXT.md              # 领域术语表
├── docs/
│   ├── adr/
│   └── laya_integration_technical_doc.md
├── prd/
├── laya/
├── graph2/
├── documents/
├── tools/retriever_tools.py
├── eval/
├── datas/
│   ├── raw/README.md       # 本地原始语料目录说明（具体文件不入库）
│   └── md/README.md        # 本地 Markdown 目录说明（具体文件不入库）
├── graph/ · agent/
└── utils/
```

---

## 环境准备

### 1. 基础依赖

- Docker Desktop（Milvus）
- Redis（可选，多会话推荐）
- Conda / Python 3.11
- （可选）Laya serve

### 2. 启动 Milvus

```powershell
docker start milvus-standalone
```

### 3. Python 环境

```powershell
conda activate rag_env
cd <项目根目录>
pip install -r requirements.txt
pip install "ragas>=0.2.0" datasets redis
```

### 4. 配置环境变量

```powershell
copy .env.example .env
# 编辑 .env，填入真实 Key（切勿提交到 Git）
```

| 变量 | 说明 |
|------|------|
| `DEEPSEEK_API_KEY` | 对话 / 路由降级 / 打分 / RAGAS |
| `DASHSCOPE_API_KEY` | Embedding + `gte-rerank` |
| `TAVILY_API_KEY` | 联网搜索 |
| `MINERU_API_TOKEN` | 云端解析 |
| `MILVUS_URI` / `COLLECTION_NAME` | 向量库 |
| `SESSION_BACKEND` / `REDIS_URL` | 会话持久化 |
| `LAYA_ENABLED` | 默认 `false` |
| `LAYA_SERVER_URL` / `LAYA_MODEL` / `LAYA_CONFIDENCE_MIN` | Laya 路由 |

---

## 快速启动

```powershell
conda activate rag_env
uvicorn main:app --host 127.0.0.1 --port 8001
# 另开终端
python -m http.server 8080
```

- Web：http://127.0.0.1:8080/index.html  
- API：http://127.0.0.1:8001 · Health：http://127.0.0.1:8001/health  

公网部署请修改 `index.html` 的 `API_BASE`，或 Nginx 同域反代（SSE 关闭 `proxy_buffering`）。

可选 Laya：`pip install "laya[serve]"` → `laya-serve`，`.env` 设 `LAYA_ENABLED=true`。

---

## API 说明

- `POST /chat` · `POST /chat/stream`：问答（SSE）  
- `DELETE /chat/memory/{session_id}`：清空会话记忆  
- `GET /health` · `GET /metrics`：探活与指标  

---

## 语料与入库

**本地语料目录**（`datas/raw/`、`datas/md/`）：仓库内**仅保留目录说明 README**，不包含具体语料文件。示例与业务文档需**自行合规准备**（内部编写或已获授权）；请勿将来源不明或受限知识资产提交到公开仓库。

| 路径 | 用途 |
|------|------|
| `datas/raw/` | 待解析原始件（本地自备） |
| `datas/md/` | 解析后的 Markdown（本地自备） |
| Milvus 集合 | 切块向量 + BM25（集合名见 `.env`） |

```powershell
# 将合规原始件放入 datas/raw 后：解析并追加入库
python documents/mineru_batch.py --ingest

# 远程 URL（请确认授权）
python documents/mineru_batch.py --url "https://example.com/your.pdf" --name "doc.pdf" --ingest

# 主题抓取（演示管线，生产请自备合规源）
python documents/topic_crawl.py --limit 5 --ingest

# 对 datas/md 下已有 Markdown 追加入库
python -c "from pathlib import Path; from documents.mineru_batch import ingest_markdown_files; print(ingest_markdown_files(sorted(Path('datas/md').glob('*.md'))))"
```

建表：日常幂等创建；清库重建须 `force=True`。详见 `CONTEXT.md` 与 `docs/adr/`。

---

## RAGAS 评测

```powershell
python eval/run_ragas.py --metrics fast --out eval/ragas_report.json
```

金标：`eval/gold_set.json`。报告含 faithfulness、answer_relevancy、`web_fallback_rate`。

---

## 上传 / 同步 GitHub 注意

- **禁止提交 `.env`**；只用 `.env.example`
- **`datas/` 具体语料文件已忽略**，仅保留 `datas/*/README.md`
- `eval/ragas_report.json`、本地 db 勿入库
- 语料版权与授权自负

---

## 企业化差距（已知）

1. API 鉴权、CORS 白名单、限流与配额  
2. 入库作业化与审计；分区检索主路径接线  
3. 语料版权合规闸门  
4. 多租户 / ACL、CI + RAGAS 门禁  
5. Laya 路由专项评测与领域微调（可选）  

---

## 许可证与声明

- 代码：学习 / 演示 / 二次开发底座  
- 第三方服务遵循各自条款  
- 知识库内容版权由语料方负责  

---

## 致谢

LangChain / LangGraph · Milvus · MinerU · RAGAS · Laya（可选）· DeepSeek / 阿里云百炼 / Tavily  
