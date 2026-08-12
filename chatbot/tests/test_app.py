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


def test_each_connection_is_its_own_session(client):
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

    # Same client_id, two connections: the histories must not have merged.
    assert "2 turns recorded" in first_replies[0]
    assert "2 turns recorded" in second_replies[0]
    assert "4 turns recorded" in first_replies[1]
    assert "4 turns recorded" in second_replies[1]

    # And the sessions are distinct.
    assert _session_of(first_replies[0]) != _session_of(second_replies[0])


def test_a_reconnect_starts_a_fresh_session(client):
    with client.websocket_connect("/communicate?client_id=same-user") as socket:
        socket.send_json({"type": "user", "text": "claude: remember this"})
        before = socket.receive_json()["message"]["text"]

    # Closing the socket is a tab closing: the history goes with it.
    with client.websocket_connect("/communicate?client_id=same-user") as socket:
        socket.send_json({"type": "user", "text": "claude: anything there?"})
        after = socket.receive_json()["message"]["text"]

    assert "2 turns recorded" in after, "history survived a reconnect"
    assert _session_of(before) != _session_of(after)


def _session_of(reply: str) -> str:
    """Pull the session id out of the claude placeholder."""
    return reply.split("session `")[1].split("`")[0]


def test_a_crashing_mode_tells_the_client_instead_of_going_quiet(client, monkeypatch):
    """A bug in a mode must not read as a frozen chat."""

    async def boom(argument):
        raise RuntimeError("mode is broken")

    monkeypatch.setattr("app.chat.modes.echo.reply", boom)

    with client.websocket_connect("/communicate?client_id=same-user") as socket:
        socket.send_json({"type": "user", "text": "echo: Test"})
        reply = socket.receive_json()

    assert "went wrong" in reply["message"]["text"]
