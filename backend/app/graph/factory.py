"""Application graph composition: one concrete node per specialist agent."""

from app.agents.actions.node import build_node as build_action_node
from app.agents.diagnostics.node import build_node as build_diagnostics_node
from app.agents.knowledge.node import build_node as build_knowledge_node
from app.agents.response.node import build_node as build_response_node
from app.agents.triage.node import build_node as build_triage_node
from app.graph.workflow import build_support_graph


def build_application_graph(*, checkpointer=None):
    return build_support_graph(
        triage=build_triage_node(),
        diagnostics=build_diagnostics_node(),
        knowledge=build_knowledge_node(),
        # Protected actions deliberately stop the graph at a durable interrupt.
        # The approval endpoint resumes this same thread after a reviewer decides.
        actions=build_action_node(pause_for_review=True),
        response=build_response_node(),
        checkpointer=checkpointer,
    )
