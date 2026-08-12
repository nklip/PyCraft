"""
The modes the chat can operate in.

A message is `mode: argument`, or a bare mode name when it needs no argument.
Each mode module exposes NAME, SUMMARY, USAGE, and an async reply() that turns
the argument into a message from `messages.py`. reply() is async so a mode can
await a network call without every other mode having to change.

The session history holds the exchange with the model and nothing else, so a
mode receives the conversation only if it sets NEEDS_HISTORY. The rest are
called with the argument alone and are therefore not able to record a turn --
the rule is enforced by what they are handed, not by remembering to behave.

Adding a mode is a new module plus one entry in MODES -- help lists whatever is
registered here, so it never goes out of date.
"""

from app.chat import messages
from app.chat.conversations import Conversation
from app.chat.modes import claude, echo, types
from app.chat.modes import help as help_  # bare `help` would shadow the builtin

SEPARATOR = ":"

MODES = {module.NAME: module for module in (help_, echo, types, claude)}


def parse(text: str) -> tuple[str, str]:
    """
    Split a message into its mode name and argument.

    `echo: Test` is ("echo", "Test"); a bare `help` is ("help", ""). Text with
    no separator is returned whole as the name, which simply will not match a
    mode -- that is how unrecognised input reaches the fallback.
    """
    name, separator, argument = text.partition(SEPARATOR)
    return name.strip().lower(), argument.strip() if separator else ""


def needs_history(mode) -> bool:
    """Whether a mode takes part in the conversation sent to the model."""
    return getattr(mode, "NEEDS_HISTORY", False)


async def dispatch(text: str, conversation: Conversation) -> dict:
    """Route one message to its mode and return the reply message."""
    name, argument = parse(text)
    mode = MODES.get(name)

    if mode is None:
        return _unknown(name)

    if needs_history(mode):
        return await mode.reply(argument, conversation)

    return await mode.reply(argument)


def _unknown(name: str) -> dict:
    known = ", ".join(f"`{mode}`" for mode in MODES)
    opening = f"I do not have a mode called `{name}`." if name else "That message was empty."
    return messages.text(f"{opening} I know: {known}. Say `help` for what each one does.")
