from uuid import UUID

import pytest
from fastapi import HTTPException

from app import main
from app.schemas.conversations import ChatTurn, ConversationView, CreateConversation, SendMessage


CONVERSATION_ID = UUID("6f41632c-992f-46fd-8df1-d1c57e5505b5")


def _conversation() -> ConversationView:
    return ConversationView(
        conversation_id=CONVERSATION_ID, customer_id="ACC-1001",
        requester_email="netops@northwind-logistics.com", title="New support request", messages=[],
    )


def test_create_conversation_endpoint_returns_created_conversation(monkeypatch) -> None:
    monkeypatch.setattr(main.conversations, "create", lambda email, title: _conversation())

    assert main.create_conversation(CreateConversation(requester_email="netops@northwind-logistics.com")).conversation_id == CONVERSATION_ID


def test_create_conversation_rejects_unknown_requester(monkeypatch) -> None:
    monkeypatch.setattr(main.conversations, "create", lambda email, title: None)

    with pytest.raises(HTTPException) as error:
        main.create_conversation(CreateConversation(requester_email="unknown@example.com"))

    assert error.value.status_code == 404


def test_list_conversations_is_scoped_to_the_requester(monkeypatch) -> None:
    monkeypatch.setattr(main.conversations, "list_for_requester", lambda email: [_conversation()])

    assert main.list_conversations("netops@northwind-logistics.com")[0].conversation_id == CONVERSATION_ID


def test_post_message_endpoint_returns_graph_turn(monkeypatch) -> None:
    turn = ChatTurn(conversation=_conversation(), response={"message": "reply"}, state={})
    monkeypatch.setattr(main, "send_message", lambda conversation_id, content: turn)

    assert main.post_message(CONVERSATION_ID, SendMessage(content="hello")).response["message"] == "reply"


def test_delete_conversation_endpoint_delegates_to_store(monkeypatch) -> None:
    monkeypatch.setattr(main.conversations, "delete", lambda conversation_id: True)

    assert main.delete_conversation(CONVERSATION_ID) is None
