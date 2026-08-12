"""Echo mode: repeats back whatever was said after the separator."""

from app.chat import messages
from app.chat.conversations import Conversation

NAME = "echo"
SUMMARY = "Repeat something back to you."
USAGE = "echo: Test"


async def reply(argument: str, conversation: Conversation) -> dict:
    if not argument:
        return messages.text(f"Give me something to echo, like `{USAGE}`.")

    return messages.text(f"Hello from backend! Did you say '{argument}'?")
