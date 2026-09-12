"""
按前道工艺主题包从 arXiv 检索论文，优先经 MinerU 远程 URL 解析并可选入库。

用法（项目根目录、rag_env）：
  python documents/topic_crawl.py --limit 5 --ingest
  python documents/topic_crawl.py --limit 15 --dry-run
  python documents/topic_crawl.py --query "EUV lithography" --limit 5 --ingest

约定见 CONTEXT.md / docs/adr/0001-semiconductor-corpus-acquisition.md
"""

from __future__ import annotations

import argparse
import hashlib
import re
import sys
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable
from urllib.parse import quote_plus

import requests

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from documents.mineru_batch import ingest_markdown_files, parse_remote_url
from documents.mineru_client import MinerUCloudClient
from utils.env_utils import COLLECTION_NAME, MILVUS_URI
from utils.log_utils import log

# 前道工艺主题包（FEOL Topic Pack）
DEFAULT_QUERIES = [
    'all:"lithography" AND (all:"semiconductor" OR all:"EUV" OR all:"photoresist")',
    'all:"plasma etch" AND all:semiconductor',
    'all:"atomic layer deposition" OR all:"chemical vapor deposition" semiconductor',
    'all:"chemical mechanical polishing" OR all:CMP semiconductor',
    'all:metrology AND (all:semiconductor OR all:lithography OR all:overlay)',
]

ARXIV_API = "https://export.arxiv.org/api/query"
ATOM_NS = {"atom": "http://www.w3.org/2005/Atom"}


@dataclass(frozen=True)
class ArxivPaper:
    arxiv_id: str
    title: str
    pdf_url: str

    @property
    def file_name(self) -> str:
        return f"arxiv_{self.arxiv_id}.pdf"

    @property
    def md_stem(self) -> str:
        return f"arxiv_{self.arxiv_id}"


def _normalize_arxiv_id(raw: str) -> str:
    # http://arxiv.org/abs/2609.11459v1 -> 2609.11459
    m = re.search(r"(\d{4}\.\d{4,5})(v\d+)?$", raw.strip())
    if m:
        return m.group(1)
    return raw.rsplit("/", 1)[-1].split("v")[0]


def search_arxiv(query: str, *, max_results: int = 20, timeout: float = 60.0) -> list[ArxivPaper]:
    url = (
        f"{ARXIV_API}?search_query={quote_plus(query)}"
        f"&start=0&max_results={max_results}&sortBy=submittedDate&sortOrder=descending"
    )
    resp = requests.get(url, timeout=timeout, headers={"User-Agent": "RAG_PROJECT-topic-crawl/1.0"})
    resp.raise_for_status()
    root = ET.fromstring(resp.text)
    papers: list[ArxivPaper] = []
    for entry in root.findall("atom:entry", ATOM_NS):
        id_text = (entry.findtext("atom:id", default="", namespaces=ATOM_NS) or "").strip()
        title = " ".join((entry.findtext("atom:title", default="", namespaces=ATOM_NS) or "").split())
        arxiv_id = _normalize_arxiv_id(id_text)
        if not arxiv_id:
            continue
        papers.append(
            ArxivPaper(
                arxiv_id=arxiv_id,
                title=title or arxiv_id,
                pdf_url=f"https://arxiv.org/pdf/{arxiv_id}.pdf",
            )
        )
    return papers


def existing_md_arxiv_ids(md_dir: Path) -> set[str]:
    ids: set[str] = set()
    if not md_dir.exists():
        return ids
    for p in md_dir.glob("*.md"):
        m = re.search(r"arxiv[_-](\d{4}\.\d{4,5})", p.name, re.I)
        if m:
            ids.add(m.group(1))
    return ids


def milvus_existing_filenames(names: Iterable[str]) -> set[str]:
    """查询 Milvus 中已存在的 filename（md 名或 pdf 名）。"""
    wanted = {n for n in names if n}
    if not wanted:
        return set()
    try:
        from pymilvus import MilvusClient
    except ImportError:
        log.warning("未安装 pymilvus，跳过 Milvus 去重检查")
        return set()

    found: set[str] = set()
    try:
        client = MilvusClient(uri=MILVUS_URI)
        if COLLECTION_NAME not in client.list_collections():
            return set()
        # 分批 filter，避免过长表达式
        batch: list[str] = []
        for name in sorted(wanted):
            batch.append(name)
            if len(batch) >= 20:
                found |= _query_filenames(client, batch)
                batch = []
        if batch:
            found |= _query_filenames(client, batch)
    except Exception as exc:
        log.warning(f"Milvus 去重检查失败（将仅按本地 md 去重）: {exc}")
    return found


def _query_filenames(client, names: list[str]) -> set[str]:
    # filename in ["a", "b"]
    quoted = ", ".join(f'"{n}"' for n in names)
    filter_expr = f"filename in [{quoted}]"
    rows = client.query(
        collection_name=COLLECTION_NAME,
        filter=filter_expr,
        output_fields=["filename"],
        limit=len(names) * 5,
    )
    return {r.get("filename") for r in rows if r.get("filename")}


def md_name_for_url(stem: str, url: str) -> str:
    digest = hashlib.md5(url.encode("utf-8")).hexdigest()[:8]
    return f"mineru_{stem}_{digest}.md"


def collect_candidates(
    queries: list[str],
    *,
    per_query: int,
    limit: int,
    md_dir: Path,
) -> list[ArxivPaper]:
    seen_ids = existing_md_arxiv_ids(md_dir)
    log.info(f"本地 md 已有 arXiv id: {len(seen_ids)}")

    pooled: list[ArxivPaper] = []
    pooled_ids: set[str] = set()
    for q in queries:
        try:
            hit = search_arxiv(q, max_results=per_query)
            log.info(f"检索到 {len(hit)} 篇 | query={q[:80]}")
        except Exception as exc:
            log.error(f"arXiv 检索失败: {exc} | query={q}")
            continue
        for p in hit:
            if p.arxiv_id in seen_ids or p.arxiv_id in pooled_ids:
                continue
            pooled_ids.add(p.arxiv_id)
            pooled.append(p)

    # Milvus：检查计划产出的 md 文件名与 pdf 名
    planned_names: list[str] = []
    for p in pooled[: max(limit * 3, limit)]:
        planned_names.append(md_name_for_url(p.md_stem, p.pdf_url))
        planned_names.append(p.file_name)

    milvus_hit = milvus_existing_filenames(planned_names)
    # 也用本地 md 文件名全集对一下
    local_md_names = {p.name for p in md_dir.glob("*.md")} if md_dir.exists() else set()

    selected: list[ArxivPaper] = []
    for p in pooled:
        md_name = md_name_for_url(p.md_stem, p.pdf_url)
        if md_name in local_md_names or md_name in milvus_hit or p.file_name in milvus_hit:
            log.info(f"去重跳过: {p.arxiv_id} ({p.title[:60]})")
            continue
        # 任意已有 mineru_arxiv_{id}_*.md
        if any(md_dir.glob(f"mineru_arxiv_{p.arxiv_id}_*.md")) if md_dir.exists() else False:
            log.info(f"去重跳过(本地通配): {p.arxiv_id}")
            continue
        selected.append(p)
        if len(selected) >= limit:
            break
    return selected


def main() -> None:
    parser = argparse.ArgumentParser(description="半导体前道工艺主题抓取 → MinerU → 可选入库")
    parser.add_argument("--limit", type=int, default=5, help="本次最多处理篇数（建议先 5，稳定后 15）")
    parser.add_argument("--per-query", type=int, default=10, help="每个检索式最多取回篇数")
    parser.add_argument("--query", action="append", default=[], help="自定义检索式，可多次；默认用 FEOL 主题包")
    parser.add_argument("--out", default=str(ROOT / "datas" / "md"), help="Markdown 输出目录")
    parser.add_argument("--ingest", action="store_true", help="解析后追加写入 Milvus")
    parser.add_argument("--dry-run", action="store_true", help="只打印候选，不调用 MinerU")
    parser.add_argument("--model", default="vlm", choices=["vlm", "pipeline"])
    parser.add_argument("--ocr", action="store_true")
    args = parser.parse_args()

    if args.limit < 1:
        raise SystemExit("--limit 必须 >= 1")

    queries = args.query or DEFAULT_QUERIES
    md_dir = Path(args.out)
    md_dir.mkdir(parents=True, exist_ok=True)

    candidates = collect_candidates(
        queries, per_query=args.per_query, limit=args.limit, md_dir=md_dir
    )
    if not candidates:
        log.warning("没有新的候选论文（检索失败或全部被去重）")
        return

    log.info(f"本次将处理 {len(candidates)} 篇:")
    for i, p in enumerate(candidates, 1):
        log.info(f"  [{i}] {p.arxiv_id} | {p.title[:100]}")
        log.info(f"      {p.pdf_url}")

    if args.dry_run:
        log.info("dry-run：到此结束")
        return

    client = MinerUCloudClient(model_version=args.model, language="ch", is_ocr=args.ocr)
    produced: list[Path] = []
    for p in candidates:
        try:
            md_path = parse_remote_url(p.pdf_url, md_dir, client, name=p.file_name)
            produced.append(md_path)
            log.info(f"解析完成: {p.arxiv_id} -> {md_path.name}")
        except Exception as exc:
            log.error(f"解析失败 {p.arxiv_id}: {exc}")
            log.exception(exc)

    log.info(f"成功解析 {len(produced)}/{len(candidates)}")
    if args.ingest and produced:
        n = ingest_markdown_files(produced)
        log.info(f"追加写入 Milvus 完成，共 {n} 个文档块")
    elif not args.ingest:
        log.info("未加 --ingest；需要入库时请重新加该参数或对已有 md 单独入库")


if __name__ == "__main__":
    main()
