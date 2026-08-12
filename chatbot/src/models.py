from pydantic import BaseModel
from typing import Dict
from fastapi import WebSocket

class Payload(BaseModel):
    type: str
    intent: str
    context: Dict

class WebSocketConnectionModel:
    client_id: str
    socket: WebSocket