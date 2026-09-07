"""Measure hybrid retrieval against scenario citation labels without invoking an LLM."""

from __future__ import annotations

import argparse
import json
import time
from pathlib import Path

from app.config import get_settings
from app.tools.knowledge import retrieve_knowledge


def _matches(expected: str, url: str) -> bool:
    return expected.startswith("telemetry:") or expected in url


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=Path(__file__).resolve().parents[2] / "reports" / "retrieval_eval.json")
    parser.add_argument("--limit", type=int, default=5)
    args = parser.parse_args()
    scenarios = [json.loads(line) for line in (get_settings().data_path / "eval" / "scenarios.jsonl").read_text(encoding="utf-8").splitlines()]
    cases = []
    reciprocal_ranks = []
    recalls = []
    for scenario in scenarios:
        expected = [source for source in scenario["expected"]["must_cite"] if not source.startswith("telemetry:")]
        started = time.perf_counter(); hits = retrieve_knowledge(scenario["opening_message"], args.limit); latency_ms = round((time.perf_counter() - started) * 1000, 1)
        first_rank = next((index for index, hit in enumerate(hits, 1) if any(_matches(source, hit.article_url) for source in expected)), None)
        reciprocal_ranks.append(1 / first_rank if first_rank else 0)
        recalls.append(bool(first_rank))
        cases.append({"scenario_id": scenario["scenario_id"], "expected_sources": expected, "hits": [{"url": hit.article_url, "section": hit.section_title, "score": hit.score} for hit in hits], "first_relevant_rank": first_rank, "latency_ms": latency_ms})
    report = {"metric_scope": "scenario opening messages with public-KB citation labels only", "recall_at_k": sum(recalls) / len(recalls), "mrr": sum(reciprocal_ranks) / len(reciprocal_ranks), "cases": cases}
    args.output.parent.mkdir(parents=True, exist_ok=True); args.output.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(json.dumps({key: report[key] for key in ("recall_at_k", "mrr")}))


if __name__ == "__main__":
    main()
