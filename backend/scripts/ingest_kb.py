"""Refresh the Cato KB snapshot and incrementally index changed chunks in pgvector."""

from __future__ import annotations

import argparse
import json
from collections import defaultdict
from pathlib import Path
from typing import Any

import psycopg
from openai import OpenAI

from app.config import get_settings
from scripts.build_kb_chunks import EMBEDDING_MODEL, build_chunks
from scripts.crawl_kb_snapshot import (
    DEFAULT_SNAPSHOT_DIR,
    crawl_articles,
    load_robots,
    write_manifest,
)
from scripts.download_llms_index import DEFAULT_OUTPUT, download_llms_index

EMBEDDING_DIMENSIONS = 1536
EMBEDDING_BATCH_SIZE = 64


def database_url() -> str:
    url = get_settings().postgres_url
    if not url:
        raise RuntimeError("POSTGRES_URL is required.")
    return url.replace("postgresql+psycopg://", "postgresql://", 1)


def vector_literal(vector: list[float]) -> str:
    return "[" + ",".join(str(value) for value in vector) + "]"


def changed(remote_sha256: str, stored_sha256: str | None) -> bool:
    return remote_sha256 != stored_sha256


def embed(texts: list[str]) -> list[list[float]]:
    api_key = get_settings().openai_api_key
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY is required.")
    client = OpenAI(api_key=api_key)
    vectors: list[list[float]] = []
    for start in range(0, len(texts), EMBEDDING_BATCH_SIZE):
        response = client.embeddings.create(
            model=EMBEDDING_MODEL,
            dimensions=EMBEDDING_DIMENSIONS,
            input=texts[start : start + EMBEDDING_BATCH_SIZE],
        )
        vectors.extend(item.embedding for item in response.data)
    return vectors


def sync_article(
    connection: psycopg.Connection[Any], article: dict[str, Any], chunks: list[dict[str, Any]]
) -> bool:
    with connection.cursor() as cursor:
        cursor.execute("SELECT content_sha256 FROM kb_articles WHERE article_url = %s", (article["url"],))
        existing = cursor.fetchone()
    if not changed(article["sha256"], existing[0] if existing else None):
        return False

    vectors = embed([chunk["text"] for chunk in chunks])
    with connection.cursor() as cursor:
        cursor.execute(
            """INSERT INTO kb_articles (article_url, article_title, content_sha256)
               VALUES (%s, %s, %s)
               ON CONFLICT (article_url) DO UPDATE SET article_title = EXCLUDED.article_title,
               content_sha256 = EXCLUDED.content_sha256, snapshot_at = now()""",
            (article["url"], chunks[0]["article_title"], article["sha256"]),
        )
        cursor.execute("DELETE FROM kb_chunks WHERE article_url = %s", (article["url"],))
        for chunk, vector in zip(chunks, vectors, strict=True):
            cursor.execute(
                """INSERT INTO kb_chunks
                   (chunk_id, article_url, article_sha256, section_title, chunk_index, token_count, chunk_text, metadata, embedding)
                   VALUES (%s,%s,%s,%s,%s,%s,%s,%s::jsonb,%s::vector)""",
                (chunk["chunk_id"], article["url"], article["sha256"], chunk["section_title"],
                 chunk["chunk_index"], chunk["token_count"], chunk["text"], json.dumps(chunk), vector_literal(vector)),
            )
    connection.commit()
    return True


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--min-interval-seconds", type=float, default=0.25)
    parser.add_argument("--snapshot-dir", type=Path, default=DEFAULT_SNAPSHOT_DIR)
    arguments = parser.parse_args()

    index_path = download_llms_index(DEFAULT_OUTPUT)
    entries = crawl_articles(
        index_path.read_text(encoding="utf-8"), arguments.snapshot_dir,
        robots=load_robots(), minimum_interval_seconds=arguments.min_interval_seconds,
        refresh_existing=True,
    )
    write_manifest(arguments.snapshot_dir, entries)
    chunks_by_url: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for chunk in build_chunks(arguments.snapshot_dir):
        chunks_by_url[chunk["article_url"]].append(chunk)
    updated = 0
    with psycopg.connect(database_url()) as connection:
        for article in entries:
            if article.get("status") != "failed" and sync_article(connection, article, chunks_by_url[article["url"]]):
                updated += 1
    print(f"KB ingestion complete: {updated} updated articles, {len(entries) - updated} unchanged or failed.")


if __name__ == "__main__":
    main()
