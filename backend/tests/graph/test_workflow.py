from app.graph.workflow import build_support_graph


def test_technical_case_hands_diagnostics_to_knowledge_then_response() -> None:
    calls: list[str] = []

    def triage(state):
        calls.append("triage")
        return {"triage_result": {"route": "technical"}}

    def diagnostics(state):
        calls.append("diagnostics")
        assert state["triage_result"]["route"] == "technical"
        return {"diagnostic_evidence": {"findings": ["BGP routes 1024/1024"]}}

    def knowledge(state):
        calls.append("knowledge")
        assert state["diagnostic_evidence"]["findings"]
        return {"knowledge_evidence": {"citations": ["kb:bgp-prefix-exhaustion"]}}

    def actions(state):
        calls.append("actions")
        return {"action_result": {"action": "ticket_update"}}

    def response(state):
        calls.append("response")
        assert state["knowledge_evidence"]["citations"]
        return {"final_response": {"message": "Cited support response"}}

    result = build_support_graph(
        triage=triage, diagnostics=diagnostics, knowledge=knowledge, actions=actions, response=response
    ).invoke({"conversation_id": "c-1", "customer_context": {}, "messages": []})

    assert calls == ["triage", "diagnostics", "knowledge", "actions", "response"]
    assert result["final_response"]["message"] == "Cited support response"


def test_direct_knowledge_case_skips_diagnostics() -> None:
    calls: list[str] = []

    def triage(state):
        calls.append("triage")
        return {"triage_result": {"route": "knowledge"}}

    def diagnostics(state):
        calls.append("diagnostics")
        return {}

    def knowledge(state):
        calls.append("knowledge")
        return {"knowledge_evidence": {}}

    def actions(state):
        calls.append("actions")
        return {"action_result": {"action": "none"}}

    def response(state):
        calls.append("response")
        return {"final_response": {"message": "answer"}}

    build_support_graph(
        triage=triage, diagnostics=diagnostics, knowledge=knowledge, actions=actions, response=response
    ).invoke({"conversation_id": "c-2", "customer_context": {}, "messages": []})

    assert calls == ["triage", "knowledge", "actions", "response"]
