"""
云端 MinerU（mineru.net）精准解析客户端。

支持：
1. 本地文件上传解析（/api/v4/file-urls/batch → PUT → 轮询 batch 结果）
2. 远程 URL 解析（/api/v4/extract/task → 轮询 task 结果）

解析成功后下载 zip，提取 full.md。
"""

from __future__ import annotations

import io
import re
import time
import zipfile
from pathlib import Path
from typing import Any, Dict, List, Optional

import requests

from utils.env_utils import MINERU_API_TOKEN
from utils.log_utils import log

BASE_URL = "https://mineru.net"
SUPPORTED_SUFFIXES = {
    ".pdf", ".doc", ".docx", ".ppt", ".pptx", ".xls", ".xlsx",
    ".png", ".jpg", ".jpeg", ".jp2", ".webp", ".gif", ".bmp",
    ".html", ".htm",
}


class MinerUCloudError(RuntimeError):
    pass


class MinerUCloudClient:
    def __init__(
        self,
        token: Optional[str] = None,
        *,
        model_version: str = "vlm",
        language: str = "ch",
        enable_table: bool = True,
        enable_formula: bool = True,
        is_ocr: bool = False,
        poll_interval: float = 5.0,
        timeout: float = 900.0,
        request_timeout: float = 120.0,
    ):
        self.token = (token or MINERU_API_TOKEN or "").strip().strip('"').strip("'")
        if self.token.lower().startswith("bearer "):
            self.token = self.token[7:].strip()
        if not self.token:
            raise MinerUCloudError(
                "未配置 MINERU_API_TOKEN，请在 .env 中填写云端 MinerU Token"
            )
        self.model_version = model_version
        self.language = language
        self.enable_table = enable_table
        self.enable_formula = enable_formula
        self.is_ocr = is_ocr
        self.poll_interval = poll_interval
        self.timeout = timeout
        self.request_timeout = request_timeout

    def _headers(self) -> Dict[str, str]:
        return {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json",
            "Accept": "*/*",
        }

    def _raise_if_error(self, payload: Dict[str, Any], action: str) -> None:
        code = payload.get("code")
        if code not in (0, "0", None) and code != 0:
            raise MinerUCloudError(f"{action} 失败: code={code}, msg={payload.get('msg')}")

    @staticmethod
    def _safe_stem(name: str) -> str:
        stem = Path(name).stem
        stem = re.sub(r"[^\w\u4e00-\u9fff\-]+", "_", stem).strip("_")
        return stem or "mineru_doc"

    def parse_local_file(self, file_path: str | Path, output_md_path: str | Path) -> Path:
        """上传本地文件并解析为 Markdown。"""
        path = Path(file_path)
        if not path.exists():
            raise FileNotFoundError(f"文件不存在: {path}")
        if path.suffix.lower() not in SUPPORTED_SUFFIXES:
            raise MinerUCloudError(f"不支持的文件类型: {path.suffix}")

        model_version = "MinerU-HTML" if path.suffix.lower() in {".html", ".htm"} else self.model_version
        data_id = self._safe_stem(path.name)[:120]

        apply_url = f"{BASE_URL}/api/v4/file-urls/batch"
        body = {
            "enable_formula": self.enable_formula,
            "enable_table": self.enable_table,
            "language": self.language,
            "model_version": model_version,
            "files": [
                {
                    "name": path.name,
                    "data_id": data_id,
                    "is_ocr": self.is_ocr,
                }
            ],
        }
        log.info(f"MinerU 申请上传链接: {path.name}")
        resp = requests.post(
            apply_url, headers=self._headers(), json=body, timeout=self.request_timeout
        )
        if resp.status_code == 401:
            raise MinerUCloudError(
                "MinerU Token 认证失败(401/A0202)。请到 https://mineru.net/apiManage/docs "
                "重新创建 Token，并更新 .env 中的 MINERU_API_TOKEN"
            )
        resp.raise_for_status()
        payload = resp.json()
        self._raise_if_error(payload, "申请上传链接")

        batch_id = payload["data"]["batch_id"]
        upload_urls = payload["data"]["file_urls"]
        if not upload_urls:
            raise MinerUCloudError("未返回文件上传链接")

        log.info(f"MinerU 上传文件中: {path.name}")
        with path.open("rb") as f:
            # 官方要求：上传时不要手动设置 Content-Type
            up = requests.put(upload_urls[0], data=f, timeout=max(self.request_timeout, 300))
        if up.status_code not in (200, 201):
            raise MinerUCloudError(f"文件上传失败: status={up.status_code}, body={up.text[:300]}")

        zip_url = self._poll_batch_result(batch_id, prefer_name=path.name, prefer_data_id=data_id)
        return self._download_zip_and_save_md(zip_url, output_md_path)

    def parse_remote_url(self, file_url: str, output_md_path: str | Path, file_name: str = "") -> Path:
        """提交远程文件 URL 并解析为 Markdown。"""
        submit_url = f"{BASE_URL}/api/v4/extract/task"
        body = {
            "url": file_url,
            "model_version": self.model_version,
            "enable_formula": self.enable_formula,
            "enable_table": self.enable_table,
            "language": self.language,
            "is_ocr": self.is_ocr,
        }
        if file_name:
            body["data_id"] = self._safe_stem(file_name)[:120]

        log.info(f"MinerU 提交远程解析: {file_url}")
        resp = requests.post(
            submit_url, headers=self._headers(), json=body, timeout=self.request_timeout
        )
        if resp.status_code == 401:
            raise MinerUCloudError(
                "MinerU Token 认证失败(401/A0202)。请到 https://mineru.net/apiManage/docs "
                "重新创建 Token，并更新 .env 中的 MINERU_API_TOKEN"
            )
        resp.raise_for_status()
        payload = resp.json()
        self._raise_if_error(payload, "提交远程解析任务")
        task_id = payload["data"]["task_id"]

        zip_url = self._poll_task_result(task_id)
        return self._download_zip_and_save_md(zip_url, output_md_path)

    def _poll_batch_result(self, batch_id: str, prefer_name: str = "", prefer_data_id: str = "") -> str:
        poll_url = f"{BASE_URL}/api/v4/extract-results/batch/{batch_id}"
        deadline = time.time() + self.timeout
        while time.time() < deadline:
            resp = requests.get(poll_url, headers=self._headers(), timeout=self.request_timeout)
            resp.raise_for_status()
            payload = resp.json()
            self._raise_if_error(payload, "轮询批量解析结果")

            results = payload.get("data", {}).get("extract_result") or []
            if isinstance(results, dict):
                results = [results]

            selected = None
            for item in results:
                if prefer_data_id and item.get("data_id") == prefer_data_id:
                    selected = item
                    break
                if prefer_name and item.get("file_name") == prefer_name:
                    selected = item
                    break
            if selected is None and results:
                selected = results[0]
            if not selected:
                time.sleep(self.poll_interval)
                continue

            state = str(selected.get("state") or "").lower()
            log.info(f"MinerU batch={batch_id} state={state}")
            if state == "done":
                zip_url = selected.get("full_zip_url") or ""
                if not zip_url:
                    raise MinerUCloudError(f"解析完成但无 full_zip_url: {selected}")
                return zip_url
            if state == "failed":
                raise MinerUCloudError(f"解析失败: {selected.get('err_msg') or selected}")
            time.sleep(self.poll_interval)

        raise MinerUCloudError(f"轮询超时({self.timeout}s): batch_id={batch_id}")

    def _poll_task_result(self, task_id: str) -> str:
        poll_url = f"{BASE_URL}/api/v4/extract/task/{task_id}"
        deadline = time.time() + self.timeout
        while time.time() < deadline:
            resp = requests.get(poll_url, headers=self._headers(), timeout=self.request_timeout)
            resp.raise_for_status()
            payload = resp.json()
            self._raise_if_error(payload, "轮询单任务解析结果")
            data = payload.get("data") or {}
            state = str(data.get("state") or "").lower()
            log.info(f"MinerU task={task_id} state={state}")
            if state == "done":
                zip_url = data.get("full_zip_url") or ""
                if not zip_url:
                    raise MinerUCloudError(f"解析完成但无 full_zip_url: {data}")
                return zip_url
            if state == "failed":
                raise MinerUCloudError(f"解析失败: {data.get('err_msg') or data}")
            time.sleep(self.poll_interval)
        raise MinerUCloudError(f"轮询超时({self.timeout}s): task_id={task_id}")

    def _download_zip_and_save_md(self, zip_url: str, output_md_path: str | Path) -> Path:
        log.info(f"MinerU 下载结果包: {zip_url}")
        resp = requests.get(zip_url, timeout=max(self.request_timeout, 300))
        resp.raise_for_status()

        md_text = self._extract_full_md(resp.content)
        out = Path(output_md_path)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(md_text, encoding="utf-8")
        log.info(f"已保存 Markdown: {out}")
        return out

    @staticmethod
    def _extract_full_md(zip_bytes: bytes) -> str:
        with zipfile.ZipFile(io.BytesIO(zip_bytes)) as zf:
            names = zf.namelist()
            # 优先 full.md，其次任意 .md
            candidates = [n for n in names if n.replace("\\", "/").endswith("full.md")]
            if not candidates:
                candidates = [n for n in names if n.lower().endswith(".md")]
            if not candidates:
                raise MinerUCloudError(f"结果包中未找到 Markdown 文件，包含: {names[:20]}")
            # 取路径最短的那个，通常是根目录 full.md
            target = sorted(candidates, key=lambda x: (x.count("/"), len(x)))[0]
            raw = zf.read(target)
            for enc in ("utf-8", "utf-8-sig", "gb18030"):
                try:
                    return raw.decode(enc)
                except UnicodeDecodeError:
                    continue
            return raw.decode("utf-8", errors="ignore")


def list_supported_files(raw_dir: str | Path) -> List[Path]:
    root = Path(raw_dir)
    if not root.exists():
        return []
    files = []
    for p in sorted(root.rglob("*")):
        if p.is_file() and p.suffix.lower() in SUPPORTED_SUFFIXES:
            files.append(p)
    return files
