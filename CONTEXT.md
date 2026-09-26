# RAG 半导体知识库

面向半导体领域问答的企业知识库：把原始资料解析入库后，通过 Adaptive RAG 检索与生成回答。

## Language

**语料获取（Corpus Acquisition）**：
从合法来源得到原始文件（PDF/Office/图片），经解析与入库后成为可检索知识的过程。默认指端到端：下载 → 解析 → 追加入库 → 可问答。
_Avoid_: 仅指聊天里“查到一段答案”、仅指下载而未入库

**半导体语料范围（Semiconductor Corpus Scope）**：
知识库优先收录工艺与设备类资料（光刻、刻蚀、薄膜、量测等）；材料/器件论文作补充；产品与运维 FAQ 为辅。
_Avoid_: 只堆 arXiv、只堆通用运维 FAQ

**原始件（Raw Document）**：
尚未解析、放在 `datas/raw` 的源文件。
_Avoid_: 原始文档（口语混用）、未入库 Markdown

**知识块（Chunk）**：
解析后切分并写入向量库、可被检索的最小文本单元。
_Avoid_: 文档（整份文件）、段落（未入库的自然段）

**主题抓取（Topic Crawl）**：
按预设关键词从开放源检索并下载原始件到 `datas/raw`，再自动解析入库的获取方式。第一期以本地盘投放 + 少量公开论文为主，抓取脚本用于规模化补量。
_Avoid_: 持续同步、全网爬虫、不定时任务扩库

**前道工艺主题包（FEOL Topic Pack）**：
第一批抓取关键词范围：光刻（lithography）、刻蚀（etch）、薄膜沉积（deposition）、CMP、量测（metrology）。
_Avoid_: 仅 EUV、仅 2D/材料论文包

**演示获取策略（Demo Acquisition Policy）**：
当前阶段以演示扩库为先，下载范围可放宽；不作为生产环境的版权合规标准。
_Avoid_: 生产合规、企业法务已批准语料

**远程解析优先（Remote Parse First）**：
公开 PDF 优先用 MinerU 远程 URL 拉取解析；本机下载失败时再人工放入 `datas/raw`。
_Avoid_: 仅本机下载、双通道自动回退（已否决为默认）

**抓取批量（Crawl Batch Size）**：
单次主题抓取先以 5 篇验证链路，稳定后默认 15 篇。
_Avoid_: 单次 50 篇默认

**语料去重（Corpus Dedup）**：
以文件名 / arXiv id 与已有 `datas/md` 对齐为主，入库前再检查 Milvus 中是否已有同名 `filename`。
_Avoid_: 仅内容 hash 去重

**会话记忆（Conversation Memory）**：
按 `session_id` 保存的多轮问答历史，供指代消解与追问。默认持久化到 SQLite（或 Redis）。
_Avoid_: 仅进程内存（重启即丢）

**知识库引用（KB Citation）**：
本地回答文末由系统根据检索块 `filename`/`title` 去重列出的溯源列表。
_Avoid_: 模型自行编造的文件名或外链

**改进目标（Improvement Goal）**：
当前迭代优先提升检索与回答质量：提高本地命中、降低不必要联网与幻觉，并用 RAGAS 等指标回归验证。
_Avoid_: 生产级企业控制面（鉴权/多租户）作为本迭代主目标

**质量杠杆（Quality Lever）**：
为提升回答质量可动的手段，主要包括语料覆盖、切块策略、检索/路由策略三类。
_Avoid_: 笼统说「优化 RAG」而不指明杠杆

**本周质量冲刺（Quality Sprint）**：
约一周内以补语料（覆盖弱项工艺概念）为主，并以扩充金标 + RAGAS 回归为验收；检索/路由大改放到后续迭代。
_Avoid_: 本周同时铺开企业化鉴权与大规模路由重构

**验收标准（Acceptance Bar）**：
金标集扩到足够条数，弱项题（如 CMP、刻蚀定义类）更多走本地库，且 faithfulness / answer_relevancy 相对基线不滑坡或有提升。
_Avoid_: 仅凭主观「感觉更好」作为唯一验收

**基础工艺百科（Process Primer）**：
面向「什么是 X」类问题的短文语料（CMP、刻蚀、沉积、光刻入门等），用于补齐概念空洞；本周语料以百科/FAQ 为主、论文抓取为辅。
_Avoid_: 仅用 arXiv 长文充当入门定义

**联网率（Web Fallback Rate）**：
评测集中走 Tavily 联网路径的题目占比；作为本周质量 KPI 之一，与 RAGAS 分数一并观察。
_Avoid_: 把联网次数当成唯一成功率指标

**Laya 意图路由（Laya Intent Route）**：
用本地 System-1 模型（Laya Choice）在入口将问题分到 `vectorstore` 或 `web_search`；低置信度或服务不可用时回退 DeepSeek 结构化路由。
_Avoid_: 用 Laya 直接生成最终答案；未启用不等于路由失效（有 LLM 降级）
