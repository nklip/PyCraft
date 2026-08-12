"""
Builders for the render contract the frontend understands.

Every reply the browser receives is one of these shapes. Adding a new kind of
reply means adding a builder here and a renderer in the JavaScript -- the
contract is deliberately narrow so the two sides can move independently.
"""

TEXT = "text"
TABLE = "table"


def text(body: str) -> dict:
    """A plain message. Markdown is rendered by the client."""
    return {"template_type": TEXT, "text": body}


def table(caption: str, rows: list[dict], *, clickable: bool = False) -> dict:
    """A caption above a table of uniform rows."""
    return {
        "template_type": TABLE,
        "clickable": "true" if clickable else "false",
        "text": caption,
        "msg_payload": rows,
    }
