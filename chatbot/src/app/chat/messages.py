"""
Builders for the render contract the frontend understands.

Every reply the browser receives is one of these shapes. Adding a new kind of
reply means adding a builder here and a renderer in the JavaScript -- the
contract is deliberately narrow so the two sides can move independently.
"""

TEXT = "text"
TABLE = "table"
CHOICES = "choices"


def text(body: str) -> dict:
    """A plain message. Markdown is rendered by the client."""
    return {"template_type": TEXT, "text": body}


def choices(body: str, label: str, options: list[tuple[str, str]]) -> dict:
    """
    A collapsible group of things the user can click.

    `label` names the group -- the button that expands it -- and each option is
    a (label, command) pair. Clicking one sends its command as if the user had
    typed it, so a menu never does anything a typed message could not.
    """
    return {
        "template_type": CHOICES,
        "text": body,
        "label": label,
        "msg_payload": [{"label": option, "command": command} for option, command in options],
    }


def table(caption: str, rows: list[dict], *, clickable: bool = False) -> dict:
    """A caption above a table of uniform rows."""
    return {
        "template_type": TABLE,
        "clickable": "true" if clickable else "false",
        "text": caption,
        "msg_payload": rows,
    }
