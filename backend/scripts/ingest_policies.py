"""Index the supplied internal policy and SLA documents as citable local sources."""

from __future__ import annotations

import hashlib
from collections import defaultdict
from pathlib import Path

import psycopg
import tiktoken

from app.config import get_settings
from scripts.analyze_kb_sections import split_h2_sections
from scripts.build_kb_chunks import EMBEDDING_MODEL, article_title
from scripts.ingest_kb import database_url, sync_article


def build_policy_records(data_path: Path) -> tuple[list[dict], dict[str, list[dict]]]:
    """Build title-and-section chunks compatible with the public KB index."""
    paths = sorted((data_path / "policies").glob("*.md")) + [data_path / "sla_policy.md"]
    encoding = tiktoken.encoding_for_model(EMBEDDING_MODEL)
    articles: list[dict] = []; chunks: dict[str, list[dict]] = defaultdict(list)
    for path in paths:
        markdown = path.read_text(encoding="utf-8"); sha256 = hashlib.sha256(markdown.encode()).hexdigest()
        url = f"policy://{path.stem}"; title = article_title(markdown, path.stem)
        article = {"url": url, "sha256": sha256, "path": path.name, "status": "ok"}; articles.append(article)
        sections = split_h2_sections(markdown) or [("Overview", f"## Overview\n{markdown}")]
        for section_index, (section_title, section) in enumerate(sections):
            body = section.split("\n", 1)[-1].strip(); text = f"Article title: {title}\nSection: {section_title}\n\n{body}"
            chunks[url].append({"chunk_id": f"policy-{path.stem}:s{section_index}:c0", "text": text, "token_count": len(encoding.encode(text)), "article_title": title, "article_url": url, "article_path": path.name, "article_sha256": sha256, "section_title": section_title, "section_index": section_index, "chunk_index": 0, "embedding_model": EMBEDDING_MODEL, "target_tokens": 600})
    return articles, chunks


def sync_policies() -> int:
    articles, chunks = build_policy_records(get_settings().data_path); updated = 0
    with psycopg.connect(database_url()) as connection:
        for article in articles:
            updated += int(sync_article(connection, article, chunks[article["url"]]))
    return updated


if __name__ == "__main__":
    print(f"Policy ingestion complete: {sync_policies()} updated documents.")
