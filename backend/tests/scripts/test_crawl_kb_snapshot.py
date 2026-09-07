import hashlib
import json
from pathlib import Path
from urllib.robotparser import RobotFileParser

import pytest

from scripts.crawl_kb_snapshot import CrawlError, crawl_articles, extract_article_urls, write_manifest


def _robots(allowed: bool = True) -> RobotFileParser:
    robots = RobotFileParser()
    robots.parse(["User-agent: *", "Allow: /" if allowed else "Disallow: /"])
    return robots


def test_extract_article_urls_keeps_only_unique_cato_docs_markdown_links() -> None:
    index = "\n".join(
        [
            "[Good](https://knowledge.catonetworks.com/docs/good.md)",
            "[Duplicate](https://knowledge.catonetworks.com/docs/good.md)",
            "[Other host](https://example.com/docs/no.md)",
            "[HTML](https://knowledge.catonetworks.com/docs/no)",
            "[Versioned API](https://knowledge.catonetworks.com/v1/docs/no.md)",
        ]
    )

    assert extract_article_urls(index) == ["https://knowledge.catonetworks.com/docs/good.md"]


def test_crawl_writes_articles_hashes_and_respects_the_interval(tmp_path: Path) -> None:
    index = "[One](https://knowledge.catonetworks.com/docs/one.md)\n[Two](https://knowledge.catonetworks.com/docs/two.md)"
    pauses: list[float] = []

    entries = crawl_articles(
        index,
        tmp_path,
        robots=_robots(),
        minimum_interval_seconds=0.5,
        fetcher=lambda url: f"# {url}".encode(),
        sleep=pauses.append,
    )

    assert [entry["path"] for entry in entries] == ["articles/one.md", "articles/two.md"]
    assert (tmp_path / "articles" / "one.md").exists()
    assert entries[0]["sha256"] == hashlib.sha256(
        b"# https://knowledge.catonetworks.com/docs/one.md"
    ).hexdigest()
    assert pauses == [0.5]


def test_crawl_refuses_urls_disallowed_by_robots(tmp_path: Path) -> None:
    index = "[One](https://knowledge.catonetworks.com/docs/one.md)"

    with pytest.raises(CrawlError, match="robots.txt"):
        crawl_articles(
            index,
            tmp_path,
            robots=_robots(allowed=False),
            minimum_interval_seconds=0,
            fetcher=lambda url: pytest.fail("disallowed article must not be fetched"),
        )


def test_crawl_records_a_failed_article_and_continues(tmp_path: Path) -> None:
    index = "[One](https://knowledge.catonetworks.com/docs/one.md)\n[Two](https://knowledge.catonetworks.com/docs/two.md)"

    def fetcher(url: str) -> bytes:
        if url.endswith("two.md"):
            raise CrawlError("source returned 404")
        return b"# One"

    entries = crawl_articles(
        index,
        tmp_path,
        robots=_robots(),
        minimum_interval_seconds=0,
        fetcher=fetcher,
    )

    assert (tmp_path / "articles" / "one.md").read_bytes() == b"# One"
    assert entries[1]["status"] == "failed"
    assert "404" in entries[1]["error"]


def test_write_manifest_records_article_entries(tmp_path: Path) -> None:
    entries = [{"url": "https://knowledge.catonetworks.com/docs/one.md", "bytes": 10}]

    manifest_path = write_manifest(tmp_path, entries)

    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    assert manifest["article_count"] == 1
    assert manifest["articles"] == entries
