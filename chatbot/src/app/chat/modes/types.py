"""Type mode: renders one of the content types the chat can display."""

from app.chat import messages
from app.chat.catalog import ORGANISATIONS

# The separator the menu builds its commands with. Imported lazily below to
# avoid a circular import; kept here so the commands cannot drift from parse().
SEPARATOR = ":"

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


MENU_LABEL = "Types"


async def reply(argument: str) -> dict:
    wanted = argument.lower()

    if not wanted:
        # Asked for the mode itself: offer the menu rather than describing it.
        # The options come from RENDERERS, so the menu cannot list something the
        # chat is unable to draw.
        return messages.choices(
            "Which one would you like to see?",
            MENU_LABEL,
            [(name.capitalize(), f"{NAME}{SEPARATOR} {name}") for name in sorted(RENDERERS)],
        )

    renderer = RENDERERS.get(wanted)
    if renderer is None:
        known = ", ".join(f"`{name}`" for name in sorted(RENDERERS))
        return messages.text(f"I cannot render `{wanted}`. I know: {known}.")

    return renderer()
