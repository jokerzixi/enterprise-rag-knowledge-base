# 把待解析的 PDF / Word / PPT / 图片放到此目录
# 然后运行：
#   conda activate rag_env
#   python documents/mineru_batch.py
# 可选追加入库：
#   python documents/mineru_batch.py --ingest
#
# 主题抓取（前道工艺包 → MinerU 远程 URL → 可选入库）：
#   python documents/topic_crawl.py --limit 5 --dry-run
#   python documents/topic_crawl.py --limit 5 --ingest
#   python documents/topic_crawl.py --limit 15 --ingest
