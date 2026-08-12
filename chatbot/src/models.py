from fastapi import WebSocket
from pydantic import BaseModel


class Payload(BaseModel):
    type: str
    intent: str
    context: dict


class WebSocketConnectionModel:
    client_id: str
    socket: WebSocket
