"""Wire shapes for the chat socket."""

from pydantic import BaseModel, Field


class Payload(BaseModel):
    """
    One message from the browser.

    The client sends what the user typed and nothing more: choosing a mode is a
    decision this side makes, so the browser cannot limit what the chat is able
    to answer.

    `context` is optional because the client does not send it. It was declared
    required while nothing validated against it, so every real message would
    have been rejected the moment validation was switched on.
    """

    type: str
    text: str
    context: dict = Field(default_factory=dict)
