"""
Claude mode: scaffolding only -- no model call is made yet.

The reply below is a placeholder so the mode is reachable, testable, and listed
by help while the real integration is still to be written. Wiring it up means
replacing reply() and adding, roughly in this order:

1. An API client built once at startup, not per message, reading its key from
   settings (never from the message).
2. Per-client conversation history. The Messages API is stateless -- the full
   history is sent on every turn -- so it has to be stored on this side, keyed
   by client_id, and trimmed or compacted as it grows.
3. A translation from the response content blocks into `messages.py` builders.
   The frontend should never see the API's wire format; keeping that mapping
   here is what lets the model or provider change without touching JavaScript.
4. Streaming. Replies arrive as deltas, and the socket can forward them as they
   land instead of making the user wait for the whole turn.
5. Handling for a response that stops early -- a refusal or a token limit --
   surfaced as an ordinary text reply rather than an exception.

A table should come from a tool call with a schema rather than from parsing
prose, so the result maps straight onto `messages.table`.
"""

from app.chat import messages

NAME = "claude"
SUMMARY = "Ask Claude. Not wired up yet."
USAGE = "claude: Why is the sky blue?"


def reply(argument: str) -> dict:
    if not argument:
        return messages.text(f"Ask something, like `{USAGE}`.")

    return messages.text(
        "Claude mode is not wired up yet, so I cannot answer that. "
        "The scaffolding is in place -- see `chat/modes/claude.py`."
    )
