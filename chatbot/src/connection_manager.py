from fastapi import WebSocket, WebSocketDisconnect
from models import WebSocketConnectionModel
from typing import List, Dict

# Initial global context

gc = {
    "config" : {
        "acronyms" : {
            "counter" : 0
        },
        "session" : {
            "utterance" : "",
            "intent" : ""
        }
    }
}

class ConnectionManager:

    def __init__(self):
        self.activate_connections: List[WebSocketConnectionModel] = []
        self.global_context: Dict[str, Dict[str]] = {}

    async def connect(self, websocket: WebSocket, client_id: str):
        try:
            await websocket.accept()
            connection = WebSocketConnectionModel()
            connection.client_id = client_id
            connection.socket = websocket

            self.activate_connections.append(connection)

            print("Connection has been established!")

            if client_id in self.global_context:
                del self.global_context[client_id]

            self.global_context[client_id] = gc
            print(f"Global context has been initialized for {client_id}")

        except WebSocketDisconnect as e:
            print(f"An exception has occured while trying to connect: {e}")

    async def send_personal_message(self, message: str, client_id: str):
        for connection in self.activate_connections:
            if connection.client_id == client_id:
                client_socket = connection.socket
        await client_socket.send_json(message)

    def disconnect(self, connection: WebSocketConnectionModel):
        try:
            client_id = connection.client_id
            for index_id, conn in enumerate(self.activate_connections):
                if conn.client_id == client_id:
                    self.activate_connections.pop(index_id)
                    print(f"Connection has been successfully closed for user: {client_id}")
        except Exception as e:
            print(f"An exception has occured while trying to close WebSocket connction: {e}")

    def create_json_response(self, data, response_type):
        if response_type == "user":
            data["type"] = "user"
        elif response_type == "bot":
            data["type"] = "bot"
        return data

    def update_global_context(self, client_id, key, value):
        self.global_context[client_id][key] = value
        print("Global context has been updated.")