"""Download Cato's published LLM-friendly KB index into the local snapshot folder."""

from __future__ import annotations

import argparse
import os
import tempfile
from pathlib import Path
from typing import Protocol
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

LLMS_INDEX_URL = "https://knowledge.catonetworks.com/llms.txt"
PROJECT_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_OUTPUT = PROJECT_ROOT / "knowledge_base" / "raw" / "llms.txt"
USER_AGENT = "CatoSupportEngineerHomeTask/0.1 (KB snapshot downloader)"


class DownloadError(RuntimeError):
    """Raised when the KB index cannot be safely downloaded."""


class Response(Protocol):
    def read(self) -> bytes: ...

    def __enter__(self) -> Response: ...

    def __exit__(self, *args: object) -> None: ...


def _fetch(url: str, timeout_seconds: float) -> bytes:
    request = Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urlopen(request, timeout=timeout_seconds) as response:
            body = response.read()
    except (HTTPError, URLError, TimeoutError) as error:
        raise DownloadError(f"Could not download KB index: {error}") from error

    if not body.strip():
        raise DownloadError("KB index download was empty.")
    return body


def _atomic_write(destination: Path, content: bytes) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary_name = tempfile.mkstemp(
        prefix=f".{destination.name}.", dir=destination.parent
    )
    try:
        with os.fdopen(descriptor, "wb") as temporary_file:
            temporary_file.write(content)
        Path(temporary_name).replace(destination)
    except Exception:
        Path(temporary_name).unlink(missing_ok=True)
        raise


def download_llms_index(
    destination: Path = DEFAULT_OUTPUT, *, timeout_seconds: float = 20.0
) -> Path:
    """Fetch and atomically save the LLM index, returning its absolute path."""
    content = _fetch(LLMS_INDEX_URL, timeout_seconds)
    _atomic_write(destination, content)
    return destination.resolve()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--timeout-seconds", type=float, default=20.0)
    arguments = parser.parse_args()

    output = download_llms_index(arguments.output, timeout_seconds=arguments.timeout_seconds)
    print(f"Downloaded {LLMS_INDEX_URL} to {output}")


if __name__ == "__main__":
    main()
