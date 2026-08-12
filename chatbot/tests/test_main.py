"""Smoke tests for the two entry points: the rendered page and the socket."""

import pytest
from fastapi.testclient import TestClient

from main import server


@pytest.fixture
def client():
    return TestClient(server)


def test_chatbot_page_renders(client):
    response = client.get("/chatbot")

    assert response.status_code == 200
    assert "chatbot/static" in response.text


def test_socket_replies_with_a_bot_message(client):
    with client.websocket_connect("/communicate?client_id=test-client") as socket:
        socket.send_json({"type": "user", "intent": "greeting", "context": {}})
        response = socket.receive_json()

    assert response["type"] == "bot"
    assert response["message"]["template_type"] == "text"


def test_table_intent_returns_the_table_template(client):
    with client.websocket_connect("/communicate?client_id=test-client") as socket:
        socket.send_json({"type": "user", "intent": "table", "context": {}})
        response = socket.receive_json()

    assert response["message"]["template_type"] == "table"
    assert len(response["message"]["msg_payload"]) == 6
