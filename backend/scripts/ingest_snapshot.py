"""Index the committed KB snapshot without performing another web crawl."""

from __future__ import annotations

import argparse
import json
from collections import defaultdict

import psycopg

from scripts.build_kb_chunks import build_chunks
from scripts.ingest_kb import DEFAULT_SNAPSHOT_DIR, database_url, sync_article
from scripts.ingest_policies import sync_policies


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int)
    args = parser.parse_args()
    articles = [article for article in json.loads((DEFAULT_SNAPSHOT_DIR / "manifest.json").read_text(encoding="utf-8"))["articles"] if article.get("status") != "failed"]
    if args.limit: articles = articles[:args.limit]
    chunks_by_url = defaultdict(list)
    for chunk in build_chunks(DEFAULT_SNAPSHOT_DIR): chunks_by_url[chunk["article_url"]].append(chunk)
    updated = 0
    with psycopg.connect(database_url()) as connection:
        for index, article in enumerate(articles, 1):
            updated += int(sync_article(connection, article, chunks_by_url[article["url"]]))
            if index % 10 == 0 or index == len(articles): print(f"Indexed {index}/{len(articles)} articles ({updated} updated)", flush=True)
    print(f"Policy documents updated: {sync_policies()}", flush=True)


if __name__ == "__main__": main()
