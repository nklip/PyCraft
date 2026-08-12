"""Type mode: renders one of the content types the chat can display."""

from app.chat import messages
from app.chat.catalog import ORGANISATIONS

NAME = "type"
SUMMARY = "Render a content type, to see how the chat displays it."
USAGE = "type: table"


def _table() -> dict:
    return messages.table("This table contains next values.", ORGANISATIONS)


def _text() -> dict:
    return messages.text("This is what a plain text message looks like.")


# Every content type the frontend can render, by name.
RENDERERS = {
    messages.TABLE: _table,
    messages.TEXT: _text,
}


def reply(argument: str) -> dict:
    wanted = argument.lower()
    renderer = RENDERERS.get(wanted)

    if renderer is None:
        known = ", ".join(f"`{name}`" for name in sorted(RENDERERS))
        if wanted:
            return messages.text(f"I cannot render `{wanted}`. I know: {known}.")
        return messages.text(f"Name a type to render: {known}. For example `{USAGE}`.")

    return renderer()
