"""Parent LangGraph workflow that coordinates specialised support agents."""

from collections.abc import Callable
from typing import Any, Literal

from langgraph.graph import END, START, StateGraph

from app.graph.state import SupportState

AgentNode = Callable[[SupportState], dict[str, Any]]


def _next_after_triage(state: SupportState) -> Literal["diagnostics", "knowledge", "actions"]:
    route = state["triage_result"]["route"]
    return {
        "technical": "diagnostics",
        "knowledge": "knowledge",
        "action": "actions",
    }[route]


def build_support_graph(
    *,
    triage: AgentNode,
    diagnostics: AgentNode,
    knowledge: AgentNode,
    actions: AgentNode,
    response: AgentNode,
):
    """Build the parent graph; concrete agents are injected for easy testing."""
    graph = StateGraph(SupportState)
    graph.add_node("triage", triage)
    graph.add_node("diagnostics", diagnostics)
    graph.add_node("knowledge", knowledge)
    graph.add_node("actions", actions)
    graph.add_node("response", response)
    graph.add_edge(START, "triage")
    graph.add_conditional_edges("triage", _next_after_triage)
    graph.add_edge("diagnostics", "knowledge")
    graph.add_edge("knowledge", "actions")
    graph.add_edge("actions", "response")
    graph.add_edge("response", END)
    return graph.compile()
