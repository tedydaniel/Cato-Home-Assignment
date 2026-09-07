"""Replay supplied scripted conversations through the real chat service and score basics."""

from __future__ import annotations

import json
from pathlib import Path

from app.config import get_settings
from app.repositories import conversations
from app.services.chat import send_message


def score(expected: dict, response: dict, state: dict) -> dict[str, bool]:
    citations = [citation.get("source", "") for citation in response.get("citations", [])]
    telemetry_sources = [
        call.get("output", {}).get("source", "")
        for call in state.get("diagnostic_tool_calls", [])
    ]
    required_sources = expected.get("must_cite", [])
    cited = all(any(source in citation for citation in citations + telemetry_sources) for source in required_sources)
    required_tools = set(expected.get("must_use_tools", []))
    observed_tools = {call.get("tool_name") for call in state.get("diagnostic_tool_calls", [])}
    # These capabilities are trusted triage/action operations rather than model
    # callable telemetry tools; score them from their durable graph outputs.
    if state.get("ticket_history"):
        observed_tools.add("get_ticket_history")
    if state.get("customer_context", {}).get("sites"):
        observed_tools.add("list_sites")
    if state.get("customer_context", {}).get("customer_id"):
        observed_tools.add("lookup_account")
    action = state.get("action_result", {}).get("action", "none")
    if action == "approval_request":
        observed_tools.add("request_human_approval")
    if action == "escalate_sev1":
        observed_tools.add("escalate_sev1")
    if "[REDACTED]" in " ".join(message.get("content", "") for message in state.get("messages", [])):
        observed_tools.add("redact_credentials")
    expected_action = expected["action"]
    action_ok = {
        "auto_resolve": action == "none",
        "needs_info": state.get("triage_result", {}).get("needs_customer_question") is True,
        "human_approval": action == "approval_request",
        "escalate_human": action in {"approval_request", "ticket_create", "escalate_sev1"},
        "escalate_sev1": action == "escalate_sev1",
    }.get(expected_action, False)
    return {"citations": cited, "tools": required_tools.issubset(observed_tools), "action": action_ok}


def main() -> None:
    output = Path(__file__).resolve().parents[2] / "reports" / "scenario_eval.json"; output.parent.mkdir(exist_ok=True)
    scenarios = [json.loads(line) for line in (get_settings().data_path / "eval" / "scenarios.jsonl").read_text(encoding="utf-8").splitlines()]
    results = []
    for scenario in scenarios:
        try:
            conversation = conversations.create(scenario["requester_email"], f"Scenario {scenario['scenario_id']}")
            if conversation is None:
                results.append({"scenario_id": scenario["scenario_id"], "score": {"account_guardrail": True}, "response": {"message": "Requester account was rejected before graph execution."}})
                continue
            turns = [scenario["opening_message"]] + [item["customer"] for item in scenario["simulated_customer_followups"]]
            final = None
            for message in turns:
                final = send_message(conversation.conversation_id, message)
                if final is None: raise RuntimeError("Conversation was not persisted")
            assert final is not None
            results.append({"scenario_id": scenario["scenario_id"], "score": score(scenario["expected"], final.response, final.state), "response": final.response, "state": final.state})
        except Exception as error:
            results.append({"scenario_id": scenario["scenario_id"], "error": str(error)})
    output.write_text(json.dumps(results, indent=2, default=str), encoding="utf-8")


if __name__ == "__main__": main()
