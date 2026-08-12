"""Echo mode: repeats back whatever was said after the separator."""

from app.chat import messages

NAME = "echo"
SUMMARY = "Repeat something back to you."
USAGE = "echo: Test"


def reply(argument: str) -> dict:
    if not argument:
        return messages.text(f"Give me something to echo, like `{USAGE}`.")

    return messages.text(f"Hello from backend! Did you say '{argument}'?")
