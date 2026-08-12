"""Wire shapes for the chat socket."""

from pydantic import BaseModel, Field


class Payload(BaseModel):
    """
    One message from the browser.

    `context` is optional because the client does not send it: the field was
    declared required while nothing validated against it, so every real message
    would have been rejected the moment validation was switched on.
    """

    type: str
    intent: str
    context: dict = Field(default_factory=dict)
