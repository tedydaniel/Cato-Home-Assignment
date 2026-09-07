from decimal import Decimal
import json
from types import SimpleNamespace
from uuid import UUID

from scripts import generate_answers
from scripts.generate_answers import format_cost, langsmith_usage_for_tag


def test_langsmith_usage_sums_the_llm_runs_for_one_evaluation_tag() -> None:
    calls: list[dict] = []

    class Client:
        def list_runs(self, **kwargs):
            calls.append(kwargs)
            return [
                SimpleNamespace(total_cost=Decimal("0.001"), prompt_tokens=100, completion_tokens=10, total_tokens=110),
                SimpleNamespace(total_cost=Decimal("0.002"), prompt_tokens=200, completion_tokens=20, total_tokens=220),
            ]

    usage = langsmith_usage_for_tag(Client(), "cato-support-engineer", "eval:Q01", attempts=1)

    assert usage == {"total_cost": Decimal("0.003"), "prompt_tokens": 300, "completion_tokens": 30, "total_tokens": 330}
    assert calls[0]["filter"] == 'has(tags, "eval:Q01")'


def test_format_cost_is_explicit_when_langsmith_is_unavailable() -> None:
    assert format_cost(None) == "Token cost: unavailable (LangSmith trace was not available)."


def test_generate_answers_loads_settings_once_and_forwards_the_question_tag(monkeypatch, tmp_path) -> None:
    data = tmp_path / "data"
    (data / "eval").mkdir(parents=True)
    (data / "eval" / "questions.jsonl").write_text(json.dumps({"question_id": "Q01", "question": "What is MTU?"}) + "\n", encoding="utf-8")
    settings = SimpleNamespace(data_path=data, langsmith_api_key="", langsmith_project="project", langsmith_endpoint="")
    output = tmp_path / "answers.md"
    tags: list[list[str]] = []
    monkeypatch.setattr(generate_answers, "get_settings", lambda: settings)
    monkeypatch.setattr(generate_answers.conversations, "create", lambda *_: SimpleNamespace(conversation_id=UUID("6f41632c-992f-46fd-8df1-d1c57e5505b5")))
    monkeypatch.setattr(generate_answers, "send_message", lambda *_args, trace_tags: tags.append(trace_tags) or SimpleNamespace(response={"message": "MTU answer", "citations": []}, state={"knowledge_evidence": {"retrievals": []}}))

    generate_answers.generate_answers(output=output)

    assert tags == [["eval:Q01"]]
    assert "Token cost: unavailable" in output.read_text(encoding="utf-8")
