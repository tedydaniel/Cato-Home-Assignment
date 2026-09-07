"""Create a polite, reproducible local snapshot of Cato KB Markdown articles."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import time
from datetime import UTC, datetime
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urlparse
from urllib.request import Request, urlopen
from urllib.robotparser import RobotFileParser

from scripts.download_llms_index import (
    DEFAULT_OUTPUT as DEFAULT_INDEX_PATH,
    USER_AGENT,
    _atomic_write,
    download_llms_index,
)
from scripts.paths import project_root

PROJECT_ROOT = project_root(__file__)
DEFAULT_SNAPSHOT_DIR = PROJECT_ROOT / "knowledge_base" / "snapshot"
ROBOTS_URL = "https://knowledge.catonetworks.com/robots.txt"
ARTICLE_LINK_PATTERN = re.compile(r"\[[^\]]+\]\((https://[^)]+\.md)\)")


class CrawlError(RuntimeError):
    """Raised when a safe, complete KB snapshot cannot be created."""


def extract_article_urls(index_text: str) -> list[str]:
    """Return unique English KB Markdown URLs from the trusted LLM index."""
    urls: list[str] = []
    for candidate in ARTICLE_LINK_PATTERN.findall(index_text):
        parsed = urlparse(candidate)
        if (
            parsed.scheme == "https"
            and parsed.netloc == "knowledge.catonetworks.com"
            and parsed.path.startswith("/docs/")
            and parsed.path.endswith(".md")
            and candidate not in urls
        ):
            urls.append(candidate)
    return urls


def load_robots() -> RobotFileParser:
    """Fetch robots.txt and fail closed if it is unavailable."""
    request = Request(ROBOTS_URL, headers={"User-Agent": USER_AGENT})
    try:
        with urlopen(request, timeout=20.0) as response:
            robots_text = response.read().decode("utf-8")
    except (HTTPError, URLError, TimeoutError) as error:
        raise CrawlError(f"Unable to verify robots.txt: {error}") from error

    robots = RobotFileParser()
    robots.set_url(ROBOTS_URL)
    robots.parse(robots_text.splitlines())
    return robots


def fetch_article(url: str) -> bytes:
    request = Request(url, headers={"User-Agent": USER_AGENT})
    for attempt in range(3):
        try:
            with urlopen(request, timeout=30.0) as response:
                content = response.read()
            if not content.strip():
                raise CrawlError(f"Downloaded an empty article: {url}")
            return content
        except (HTTPError, URLError, TimeoutError) as error:
            if attempt == 2:
                raise CrawlError(f"Unable to fetch {url}: {error}") from error
            time.sleep(2**attempt)
    raise AssertionError("unreachable")


def article_path(snapshot_dir: Path, url: str) -> Path:
    """Map a validated article URL to a safe, stable local filename."""
    filename = Path(urlparse(url).path).name
    return snapshot_dir / "articles" / filename


def crawl_articles(
    index_text: str,
    snapshot_dir: Path,
    *,
    robots: RobotFileParser,
    minimum_interval_seconds: float,
    refresh_existing: bool = False,
    fetcher=fetch_article,
    sleep=time.sleep,
) -> list[dict[str, str | int]]:
    """Download all allowed articles and return manifest entries."""
    if minimum_interval_seconds < 0:
        raise ValueError("minimum_interval_seconds must be non-negative")

    urls = extract_article_urls(index_text)
    if not urls:
        raise CrawlError("No eligible KB Markdown URLs were found in llms.txt.")

    entries: list[dict[str, str | int]] = []
    for position, url in enumerate(urls):
        if not robots.can_fetch(USER_AGENT, url):
            raise CrawlError(f"robots.txt does not allow downloading {url}")

        destination = article_path(snapshot_dir, url)
        was_cached = destination.exists() and not refresh_existing
        try:
            content = destination.read_bytes() if was_cached else fetcher(url)
            if not was_cached:
                _atomic_write(destination, content)
        except CrawlError as error:
            entries.append({"url": url, "status": "failed", "error": str(error)})
            continue
        entries.append(
            {
                "url": url,
                "path": destination.relative_to(snapshot_dir).as_posix(),
                "sha256": hashlib.sha256(content).hexdigest(),
                "bytes": len(content),
                "fetched_at": datetime.now(UTC).isoformat(),
            }
        )
        if position < len(urls) - 1 and not was_cached:
            sleep(minimum_interval_seconds)
    return entries


def write_manifest(snapshot_dir: Path, entries: list[dict[str, str | int]]) -> Path:
    manifest = {
        "source_index": "https://knowledge.catonetworks.com/llms.txt",
        "crawl_completed_at": datetime.now(UTC).isoformat(),
        "article_count": sum(entry.get("status") != "failed" for entry in entries),
        "failure_count": sum(entry.get("status") == "failed" for entry in entries),
        "articles": entries,
    }
    destination = snapshot_dir / "manifest.json"
    _atomic_write(destination, json.dumps(manifest, indent=2).encode("utf-8"))
    return destination


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--snapshot-dir", type=Path, default=DEFAULT_SNAPSHOT_DIR)
    parser.add_argument("--min-interval-seconds", type=float, default=0.25)
    arguments = parser.parse_args()

    index_path = download_llms_index(DEFAULT_INDEX_PATH)
    robots = load_robots()
    entries = crawl_articles(
        index_path.read_text(encoding="utf-8"),
        arguments.snapshot_dir,
        robots=robots,
        minimum_interval_seconds=arguments.min_interval_seconds,
    )
    manifest_path = write_manifest(arguments.snapshot_dir, entries)
    failures = sum(entry.get("status") == "failed" for entry in entries)
    print(
        f"Downloaded {len(entries) - failures} KB articles; "
        f"failures: {failures}; manifest: {manifest_path.resolve()}"
    )


if __name__ == "__main__":
    main()
