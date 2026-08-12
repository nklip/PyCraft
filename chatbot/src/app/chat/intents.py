"""
Turns an incoming message into a reply.

This is the only module that decides what the assistant says. The router next to
it is transport: receive, validate, hand the payload here, send the reply back.
Keeping the two apart is what makes replies testable without a WebSocket.
"""

from app.chat.catalog import ORGANISATIONS
from app.chat.schemas import Payload

# The render contract the frontend understands. Adding a new kind of reply means
# adding a template_type here and a renderer in the JavaScript -- deliberately
# decoupled from whatever produces the content.
TEXT = "text"
TABLE = "table"


def text_reply(text: str) -> dict:
    """Build a plain-text reply."""
    return {"type": "bot", "message": {"template_type": TEXT, "text": text}}


def handle(payload: Payload, client_id: str) -> dict:
    """
    Build the reply for one incoming message.

    Args:
        payload: the validated client message.
        client_id: who sent it, for logging and future per-client context.

    Returns:
        A reply dict carrying the render contract under "message".
    """
    print(f"Processing intent '{payload.intent}' for user '{client_id}'")

    if payload.intent == "table":
        message = {
            "template_type": TABLE,
            "clickable": "false",
            "text": "This table contains next values.",
            "msg_payload": ORGANISATIONS,
        }
    else:
        message = {
            "template_type": TEXT,
            "text": "This message is from backend, ohoho!",
        }

    return {
        "type": payload.type,
        "intent": payload.intent,
        "context": payload.context,
        "message": message,
    }
