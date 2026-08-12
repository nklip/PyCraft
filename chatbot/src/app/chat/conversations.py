"""
Per-tab conversation state.

The Messages API is stateless: the whole history goes up on every turn, so this
side has to own it. A conversation belongs to one WebSocket connection -- opening
a tab starts one, closing or refreshing the tab ends it, and the history goes
with it.

That lifetime is why there is no registry here. The conversation is created by
the socket handler and referenced only by it, so it is collected when the handler
returns; there is no map of live conversations to fall out of step with the map
of live connections. A conversation that had to survive a reload would need one.
"""

from dataclasses import dataclass, field
from uuid import uuid4

USER = "user"
ASSISTANT = "assistant"


def new_session_id() -> str:
    """A fresh session id. One per connection, never reused."""
    return str(uuid4())


@dataclass
class Conversation:
    """
    One tab's chat with the model.

    `history` is already in the shape the Messages API expects, so a turn can be
    sent without translating it first.
    """

    session_id: str = field(default_factory=new_session_id)
    history: list[dict] = field(default_factory=list)

    def record(self, role: str, content: str) -> None:
        self.history.append({"role": role, "content": content})

    @property
    def turns(self) -> int:
        return len(self.history)

    @property
    def short_id(self) -> str:
        """The leading block of the session id, for logs and messages."""
        return self.session_id.split("-")[0]
