"""Help mode: explains the chat's own functionality."""

from app.chat import messages

NAME = "help"
SUMMARY = "Explain what I can do."
USAGE = "help"


async def reply(argument: str) -> dict:
    # Imported here rather than at module level: the registry imports this
    # module, so importing it back at the top would be a circular import.
    from app.chat.modes import MODES, SEPARATOR

    if argument:
        wanted = argument.lower()
        mode = MODES.get(wanted)
        if mode is None:
            return messages.text(f"I have no mode called `{wanted}`. Say `help` for the list.")
        return messages.text(f"**{mode.NAME}** — {mode.SUMMARY}\n\nTry: `{mode.USAGE}`")

    lines = [
        "I work in modes. Start a message with a mode name, then "
        f"`{SEPARATOR}`, then whatever the mode needs.",
        "",
    ]
    lines += [f"- **{mode.NAME}** — {mode.SUMMARY} Try `{mode.USAGE}`" for mode in MODES.values()]
    lines += ["", f"Say `help{SEPARATOR} <mode>` for one of them on its own."]

    return messages.text("\n".join(lines))
