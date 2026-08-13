"""Smoke tests for the two entry points: the rendered page and the socket."""

import pytest
from fastapi.testclient import TestClient

from app.chat import claude_client
from app.chat.router import manager
from app.main import server


@pytest.fixture
def client():
    return TestClient(server)


@pytest.fixture
def claude(monkeypatch):
    """
    Claude mode with the model call replaced by a report of what it was sent.

    The session tests are about which history reaches the model, so a stub that
    answers with the size of that history says everything they need -- and the
    suite stays off the network whether or not this machine has an API key.
    """

    async def complete(history: list[dict]) -> str:
        return f"history:{len(history)}"

    monkeypatch.setattr(claude_client, "configured", lambda: True)
    monkeypatch.setattr(claude_client, "complete", complete)


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


def test_each_connection_is_its_own_session(client, claude):
    """A tab is a session: two tabs never share history, and a reload starts over."""

    def ask_twice(socket):
        replies = []
        for text in ("claude: first", "claude: second"):
            socket.send_json({"type": "user", "text": text})
            replies.append(socket.receive_json()["message"]["text"])
        return replies

    with client.websocket_connect("/communicate?client_id=same-user") as first:
        first_replies = ask_twice(first)
        with client.websocket_connect("/communicate?client_id=same-user") as second:
            second_replies = ask_twice(second)

            # Both have replied, so both are registered: one entry each rather
            # than a single connection shared by the client_id they have in common.
            assert len(manager.active_connections) == 2

    # Same client_id, two connections: the second sent up its own history, not
    # one carrying the four turns the first had already accumulated.
    assert first_replies == ["history:1", "history:3"]
    assert second_replies == ["history:1", "history:3"]


def test_a_reconnect_starts_a_fresh_session(client, claude):
    with client.websocket_connect("/communicate?client_id=same-user") as socket:
        socket.send_json({"type": "user", "text": "claude: remember this"})
        socket.receive_json()
        before = set(manager.active_connections)

    # Closing the socket is a tab closing: the history goes with it.
    with client.websocket_connect("/communicate?client_id=same-user") as socket:
        socket.send_json({"type": "user", "text": "claude: anything there?"})
        after = socket.receive_json()["message"]["text"]
        sessions = set(manager.active_connections)

    assert after == "history:1", "history survived a reconnect"
    assert before.isdisjoint(sessions)


def test_a_crashing_mode_tells_the_client_instead_of_going_quiet(client, monkeypatch):
    """A bug in a mode must not read as a frozen chat."""

    async def boom(argument):
        raise RuntimeError("mode is broken")

    monkeypatch.setattr("app.chat.modes.echo.reply", boom)

    with client.websocket_connect("/communicate?client_id=same-user") as socket:
        socket.send_json({"type": "user", "text": "echo: Test"})
        reply = socket.receive_json()

    assert "went wrong" in reply["message"]["text"]
