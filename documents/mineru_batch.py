"""
使用云端 MinerU 批量解析 datas/raw 下的 PDF/Office/图片，输出到 datas/md。

用法（在项目根目录、rag_env 下）：
  python documents/mineru_batch.py
  python documents/mineru_batch.py --raw datas/raw --out datas/md
  python documents/mineru_batch.py --url "https://xxx/demo.pdf" --name demo.pdf
  python documents/mineru_batch.py --ingest   # 解析后追加写入 Milvus（不重建整个库）
"""

from __future__ import annotations

import argparse
import hashlib
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from documents.markdown_parser import MarkdownParser
from documents.milvus_db import MilvusVectorSave
from documents.mineru_client import MinerUCloudClient, list_supported_files
from utils.log_utils import log


def _md_name_for(raw_file: Path) -> str:
    digest = hashlib.md5(str(raw_file.resolve()).encode("utf-8")).hexdigest()[:8]
    return f"mineru_{raw_file.stem}_{digest}.md"


def parse_raw_dir(raw_dir: Path, out_dir: Path, client: MinerUCloudClient, skip_existing: bool = True) -> list[Path]:
    files = list_supported_files(raw_dir)
    if not files:
        log.warning(f"目录中没有可解析文件: {raw_dir}")
        return []

    out_dir.mkdir(parents=True, exist_ok=True)
    outputs: list[Path] = []
    for fp in files:
        md_path = out_dir / _md_name_for(fp)
        if skip_existing and md_path.exists() and md_path.stat().st_size > 0:
            log.info(f"已存在，跳过: {md_path.name}")
            outputs.append(md_path)
            continue
        try:
            client.parse_local_file(fp, md_path)
            outputs.append(md_path)
        except Exception as exc:
            log.error(f"解析失败 {fp}: {exc}")
            log.exception(exc)
    return outputs


def parse_remote_url(url: str, out_dir: Path, client: MinerUCloudClient, name: str = "") -> Path:
    out_dir.mkdir(parents=True, exist_ok=True)
    stem = Path(name).stem if name else "remote_doc"
    digest = hashlib.md5(url.encode("utf-8")).hexdigest()[:8]
    md_path = out_dir / f"mineru_{stem}_{digest}.md"
    return client.parse_remote_url(url, md_path, file_name=name or stem)


def ingest_markdown_files(md_files: list[Path]) -> int:
    if not md_files:
        return 0
    parser = MarkdownParser()
    mv = MilvusVectorSave()
    mv.create_connection()
    total = 0
    for md in md_files:
        try:
            docs = parser.parse_markdown_to_documents(str(md))
            if not docs:
                continue
            for d in docs:
                d.metadata["source"] = d.metadata.get("source") or "mineru"
                d.metadata["filename"] = d.metadata.get("filename") or md.name
                d.metadata.setdefault("filetype", "md")
            mv.add_documents(docs)
            total += len(docs)
            log.info(f"已入库 {md.name}: {len(docs)} 块，累计 {total}")
        except Exception as exc:
            log.error(f"入库失败 {md}: {exc}")
            log.exception(exc)
    return total


def main():
    parser = argparse.ArgumentParser(description="云端 MinerU 批量解析")
    parser.add_argument("--raw", default=str(ROOT / "datas" / "raw"), help="原始文件目录")
    parser.add_argument("--out", default=str(ROOT / "datas" / "md"), help="Markdown 输出目录")
    parser.add_argument("--url", default="", help="可选：直接解析一个远程文件 URL")
    parser.add_argument("--name", default="", help="远程 URL 对应文件名（可选）")
    parser.add_argument("--model", default="vlm", choices=["vlm", "pipeline"], help="MinerU 模型版本")
    parser.add_argument("--ocr", action="store_true", help="开启 OCR")
    parser.add_argument("--force", action="store_true", help="已存在 md 也重新解析")
    parser.add_argument("--ingest", action="store_true", help="解析后追加写入 Milvus")
    args = parser.parse_args()

    client = MinerUCloudClient(
        model_version=args.model,
        language="ch",
        is_ocr=args.ocr,
    )

    raw_dir = Path(args.raw)
    out_dir = Path(args.out)
    raw_dir.mkdir(parents=True, exist_ok=True)

    produced: list[Path] = []
    if args.url:
        produced.append(parse_remote_url(args.url, out_dir, client, name=args.name))
    else:
        produced = parse_raw_dir(
            raw_dir, out_dir, client, skip_existing=not args.force
        )

    log.info(f"本次产出 Markdown {len(produced)} 个")
    if args.ingest:
        n = ingest_markdown_files(produced)
        log.info(f"追加写入 Milvus 完成，共 {n} 个文档块")
    else:
        log.info("如需入库，可执行: python documents/write_milvus.py 或加 --ingest")


if __name__ == "__main__":
    main()
