from app.agents.response import node as response_node_module
from app.agents.response.node import ResponseDraft, build_node
from app.agents.response.prompts import build_prompt


def test_response_prompt_contains_only_the_supplied_validated_evidence() -> None:
    prompt = build_prompt(evidence={"diagnostics": {"findings": []}})

    assert "customer-facing Response specialist" in prompt
    assert "Validated case evidence" in prompt
    assert '"findings": []' in prompt


def test_response_node_uses_only_validated_evidence_and_citation_ids() -> None:
    node = build_node(draft_writer=lambda state: ResponseDraft(message="The route limit caused the BGP instability."))
    result = node({
        "conversation_id": "c-1", "customer_context": {}, "messages": [],
        "triage_result": {"needs_customer_question": False},
        "diagnostic_evidence": {"findings": [{"evidence_id": "tool:client:a", "fact": "UDP is blocked."}]},
        "knowledge_evidence": {"status": "complete", "citations": [{"evidence_id": "kb:udp", "source": "https://knowledge.catonetworks.com/docs/example.md", "fact": "Example section"}]},
        "action_result": {"action": "none"},
    })

    assert result["final_response"]["message"] == "The route limit caused the BGP instability."
    assert result["final_response"]["citation_evidence_ids"] == ["kb:udp"]
    assert result["final_response"]["tool_evidence_ids"] == ["tool:client:a"]
    assert result["final_response"]["citations"][0]["evidence_id"] == "kb:udp"


def test_response_node_keeps_internal_policy_evidence_out_of_customer_citations() -> None:
    node = build_node(draft_writer=lambda state: ResponseDraft(message="Your request is under review."))

    result = node({
        "conversation_id": "c-1", "customer_context": {}, "messages": [],
        "knowledge_evidence": {"status": "complete", "citations": [
            {"evidence_id": "policy:credit", "source": "policy://POL-CREDIT", "fact": "Internal credit policy"},
            {"evidence_id": "kb:public", "source": "https://knowledge.catonetworks.com/docs/example.md", "fact": "Public article"},
        ]}, "action_result": {"action": "none"},
    })

    assert result["final_response"]["citation_evidence_ids"] == ["kb:public"]
    assert [citation["source"] for citation in result["final_response"]["citations"]] == ["https://knowledge.catonetworks.com/docs/example.md"]


def test_response_prompt_does_not_receive_internal_policy_sources(monkeypatch) -> None:
    captured: dict = {}

    class Writer:
        def with_structured_output(self, schema):
            return self

        def invoke(self, prompt: str) -> ResponseDraft:
            captured["prompt"] = prompt
            return ResponseDraft(message="Your request is under review.")

    monkeypatch.setattr(response_node_module, "ChatOpenAI", lambda **_: Writer())
    monkeypatch.setattr(response_node_module, "get_settings", lambda: type("Settings", (), {"openai_api_key": "key", "openai_model": "model"})())
    node = build_node()

    node({
        "conversation_id": "c-1", "customer_context": {}, "messages": [],
        "knowledge_evidence": {"status": "complete", "findings": [{"source": "policy://POL-CREDIT", "evidence_id": "policy:credit", "fact": "Internal wording"}], "citations": [{"source": "https://knowledge.catonetworks.com/docs/example.md", "evidence_id": "kb:public", "fact": "Public article"}]},
        "action_result": {"action": "none"},
    })

    assert "policy://" not in captured["prompt"]


def test_response_node_refuses_technical_guidance_without_a_knowledge_citation() -> None:
    node = build_node(draft_writer=lambda state: ResponseDraft(message="Unsupported technical instruction."))

    result = node({
        "conversation_id": "c-1", "customer_context": {}, "messages": [],
        "triage_result": {}, "diagnostic_evidence": {"findings": [{"evidence_id": "tool:site:a", "fact": "The link is degraded."}]},
        "knowledge_evidence": {"status": "no_coverage", "citations": []}, "action_result": {"action": "none"},
    })

    assert "cannot provide technical guidance" in result["final_response"]["message"]


def test_response_node_does_not_repeat_a_redacted_credential() -> None:
    node = build_node(draft_writer=lambda state: ResponseDraft(message="secret value"))
    result = node({"conversation_id": "c-1", "customer_context": {}, "messages": [{"role": "user", "content": "PSK: [REDACTED]"}], "diagnostic_evidence": {}, "knowledge_evidence": {"citations": []}, "action_result": {"action": "none"}})

    assert "removed the credential" in result["final_response"]["message"]
