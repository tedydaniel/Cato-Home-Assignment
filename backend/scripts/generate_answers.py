"""Run the real chat path for each evaluator question and write answers.md."""

from __future__ import annotations

import json
from pathlib import Path
import time
from decimal import Decimal
from typing import Any

from langsmith import Client

from app.config import get_settings
from app.repositories import conversations
from app.services.chat import send_message


def langsmith_usage_for_tag(
    client: Client, project_name: str, tag: str, *, attempts: int = 5, sleep=time.sleep,
) -> dict[str, int | Decimal] | None:
    """Return summed LLM usage after LangSmith's asynchronous trace upload."""
    for attempt in range(attempts):
        runs = list(client.list_runs(
            project_name=project_name,
            run_type="llm",
            filter=f'has(tags, "{tag}")',
            select=["total_cost", "prompt_tokens", "completion_tokens", "total_tokens"],
            limit=20,
        ))
        if runs:
            return {
                "total_cost": sum((run.total_cost or Decimal("0")) for run in runs),
                "prompt_tokens": sum(run.prompt_tokens or 0 for run in runs),
                "completion_tokens": sum(run.completion_tokens or 0 for run in runs),
                "total_tokens": sum(run.total_tokens or 0 for run in runs),
            }
        if attempt < attempts - 1:
            sleep(1)
    return None


def format_cost(usage: dict[str, int | Decimal] | None) -> str:
    if usage is None:
        return "Token cost: unavailable (LangSmith trace was not available)."
    cost = usage["total_cost"]
    assert isinstance(cost, Decimal)
    return (
        f"Token cost: ${cost:.6f} USD (LangSmith LLM traces; "
        f"{usage['prompt_tokens']} input, {usage['completion_tokens']} output tokens)."
    )


def generate_answers(*, output: Path | None = None) -> None:
    settings = get_settings()
    output = output or Path(__file__).resolve().parents[2] / "answers.md"
    questions = [json.loads(line) for line in (settings.data_path / "eval" / "questions.jsonl").read_text(encoding="utf-8").splitlines()]
    email = "netops@northwind-logistics.com"
    client = Client(api_key=settings.langsmith_api_key, api_url=settings.langsmith_endpoint or None) if settings.langsmith_api_key else None
    sections = ["# Evaluation answers\n", "Generated through the same conversation and graph path as the chat UI.\n"]
    for question in questions:
        conversation = conversations.create(email, f"Evaluation {question['question_id']}")
        if conversation is None:
            raise RuntimeError("Seed data is missing the evaluation requester account.")
        trace_tag = f"eval:{question['question_id']}"
        started = time.perf_counter(); turn = send_message(conversation.conversation_id, question["question"], trace_tags=[trace_tag]); latency_ms = round((time.perf_counter() - started) * 1000, 1)
        if turn is None:
            raise RuntimeError("Conversation disappeared during evaluation.")
        citations = turn.response.get("citations", [])
        retrievals = turn.state.get("knowledge_evidence", {}).get("retrievals", [])
        sections.extend([f"## {question['question_id']}", question["question"], "", turn.response["message"], "", "### Citations"])
        sections.extend([f"- {citation['source']} — {citation['fact']}" for citation in citations] or ["- None"])
        usage = langsmith_usage_for_tag(client, settings.langsmith_project, trace_tag) if client else None
        sections.extend(["", "### Top retrieved chunks", *[f"- {item.get('source')} — {item.get('section')} (score: {item.get('score')})" for item in retrievals], "", f"Latency: {latency_ms} ms", format_cost(usage), "KB snapshot date: see `knowledge_base/snapshot/manifest.json`", ""])
    output.write_text("\n".join(sections), encoding="utf-8")


def main() -> None:
    generate_answers()


if __name__ == "__main__":
    main()
