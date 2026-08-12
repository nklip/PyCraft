"""The live WebSocket connections, one per open tab."""

from dataclasses import dataclass

from fastapi import WebSocket

from app.chat.conversations import Conversation


@dataclass
class Connection:
    """
    One live browser connection and the conversation it owns.

    `client_id` says who the user is and can repeat across tabs; the session id
    on the conversation is what identifies *this* tab. Routing keys on the
    session, because "send to client_id" is ambiguous the moment a second tab is
    open -- which is the normal case here, since every tab is its own chat.
    """

    client_id: str
    socket: WebSocket
    conversation: Conversation

    @property
    def session_id(self) -> str:
        return self.conversation.session_id


class ConnectionManager:
    def __init__(self):
        self.active_connections: dict[str, Connection] = {}

    async def connect(self, websocket: WebSocket, client_id: str) -> Connection:
        """Accept the socket and start a conversation for it."""
        await websocket.accept()

        connection = Connection(client_id=client_id, socket=websocket, conversation=Conversation())
        self.active_connections[connection.session_id] = connection

        print(f"Connected: client '{client_id}', session {connection.session_id}")
        return connection

    def disconnect(self, session_id: str) -> None:
        """Forget the connection and, with it, the conversation history."""
        connection = self.active_connections.pop(session_id, None)
        if connection is None:
            return
        print(f"Disconnected: client '{connection.client_id}', session {session_id}")

    async def send_personal_message(self, message: dict, session_id: str) -> None:
        """
        Send to one session.

        A session that is not connected is not an error: the tab can close while
        a reply is being prepared, and there is nothing left to deliver to.
        """
        connection = self.active_connections.get(session_id)
        if connection is None:
            print(f"Dropped a reply for session {session_id}: no longer connected")
            return

        await connection.socket.send_json(message)

    def create_json_response(self, data: dict, response_type: str) -> dict:
        if response_type in ("user", "bot"):
            data["type"] = response_type
        return data
