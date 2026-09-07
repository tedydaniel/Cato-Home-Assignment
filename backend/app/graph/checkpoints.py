"""PostgreSQL-backed LangGraph checkpoint lifecycle."""

from contextlib import contextmanager
from collections.abc import Iterator

from langgraph.checkpoint.postgres import PostgresSaver

from app.config import get_settings
from app.graph.factory import build_application_graph


def _url() -> str:
    return get_settings().postgres_url.replace("postgresql+psycopg://", "postgresql://", 1)


@contextmanager
def application_graph() -> Iterator[object]:
    """Yield a graph whose checkpoints survive backend restarts."""
    with PostgresSaver.from_conn_string(_url()) as saver:
        saver.setup()
        yield build_application_graph(checkpointer=saver)
