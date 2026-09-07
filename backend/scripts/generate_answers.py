"""Run the real chat path for each evaluator question and write answers.md."""

from __future__ import annotations

import json
from pathlib import Path
import time

from app.config import get_settings
from app.repositories import conversations
from app.services.chat import send_message


def main() -> None:
    output = Path(__file__).resolve().parents[2] / "answers.md"
    questions = [json.loads(line) for line in (get_settings().data_path / "eval" / "questions.jsonl").read_text(encoding="utf-8").splitlines()]
    email = "netops@northwind-logistics.com"
    sections = ["# Evaluation answers\n", "Generated through the same conversation and graph path as the chat UI.\n"]
    for question in questions:
        conversation = conversations.create(email, f"Evaluation {question['question_id']}")
        if conversation is None:
            raise RuntimeError("Seed data is missing the evaluation requester account.")
        started = time.perf_counter(); turn = send_message(conversation.conversation_id, question["question"]); latency_ms = round((time.perf_counter() - started) * 1000, 1)
        if turn is None:
            raise RuntimeError("Conversation disappeared during evaluation.")
        citations = turn.response.get("citations", [])
        retrievals = turn.state.get("knowledge_evidence", {}).get("retrievals", [])
        sections.extend([f"## {question['question_id']}", question["question"], "", turn.response["message"], "", "### Citations"])
        sections.extend([f"- {citation['source']} — {citation['fact']}" for citation in citations] or ["- None"])
        sections.extend(["", "### Top retrieved chunks", *[f"- {item.get('source')} — {item.get('section')} (score: {item.get('score')})" for item in retrievals], "", f"Latency: {latency_ms} ms", "Token cost: recorded by LangSmith when configured", "KB snapshot date: see `knowledge_base/snapshot/manifest.json`", ""])
    output.write_text("\n".join(sections), encoding="utf-8")


if __name__ == "__main__":
    main()
