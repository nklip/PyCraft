"""Smoke tests for the two entry points: the rendered page and the socket."""

import pytest
from fastapi.testclient import TestClient

from app.main import server


@pytest.fixture
def client():
    return TestClient(server)


def test_chatbot_page_renders(client):
    response = client.get("/chatbot")

    assert response.status_code == 200
    assert "chatbot/static" in response.text


def test_socket_replies_with_a_bot_message(client):
    with client.websocket_connect("/communicate?client_id=test-client") as socket:
        socket.send_json({"type": "user", "text": "help"})
        response = socket.receive_json()

    assert response["type"] == "bot"
    assert response["message"]["template_type"] == "text"


def test_socket_renders_a_table(client):
    with client.websocket_connect("/communicate?client_id=test-client") as socket:
        socket.send_json({"type": "user", "text": "type: table"})
        response = socket.receive_json()

    assert response["message"]["template_type"] == "table"
    assert len(response["message"]["msg_payload"]) == 6


def test_socket_echoes(client):
    with client.websocket_connect("/communicate?client_id=test-client") as socket:
        socket.send_json({"type": "user", "text": "echo: Test"})
        response = socket.receive_json()

    assert response["message"]["text"] == "Hello from backend! Did you say 'Test'?"


def test_malformed_message_gets_an_error_and_keeps_the_connection(client):
    """A bad payload is the client's problem, not a reason to drop the socket."""
    with client.websocket_connect("/communicate?client_id=test-client") as socket:
        socket.send_json({"nonsense": True})
        rejected = socket.receive_json()

        assert rejected["type"] == "bot"
        assert "could not read" in rejected["message"]["text"]

        # The same connection still works afterwards.
        socket.send_json({"type": "user", "text": "echo: Test"})
        recovered = socket.receive_json()

    assert recovered["message"]["text"] == "Hello from backend! Did you say 'Test'?"
