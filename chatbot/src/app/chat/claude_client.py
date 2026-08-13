"""
The Anthropic client, and the single call the chat makes through it.

Kept apart from `modes/claude.py` so that module stays about the conversation --
what to record, what to say -- while everything to do with the SDK, the API key,
and what a failure should sound like lives here. Swapping the model, or the
provider, is then a change to one file that no mode has to know about.

The client is built once and reused. It is created on first use rather than at
import so that importing the chat never depends on configuration: with no key
set, `configured()` is False and nothing here is ever constructed.
"""

import anthropic

from app.settings import settings

# Haiku is the smallest and quickest model in the family. A chat reply is short
# and someone is watching the socket for it, so latency matters more here than
# depth would.
MODEL = "claude-haiku-4-5"

# A ceiling on a runaway answer rather than a target: replies are read in a chat
# bubble, and this is what caps the cost of a single turn.
MAX_TOKENS = 4096

SYSTEM = (
    "You are the assistant inside PyCraft's chatbot demo, a small FastAPI chat UI. "
    "Replies are rendered as Markdown in a chat bubble, so keep them short and answer "
    "what was asked."
)


class ClaudeError(Exception):
    """
    A call that failed in a way the user should hear about.

    The message is written to be shown as-is, so the mode can render it without
    knowing which SDK exception it came from.
    """


_client: anthropic.AsyncAnthropic | None = None


def configured() -> bool:
    """Whether the mode can call the model at all. False turns it into a toggle."""
    return settings.has_anthropic_api_key


def client() -> anthropic.AsyncAnthropic:
    """The shared client, built on first use."""
    global _client

    if _client is None:
        # Passed explicitly: the key comes from chatbot/.env through settings,
        # and the SDK reads only the real environment on its own.
        _client = anthropic.AsyncAnthropic(api_key=settings.anthropic_api_key.get_secret_value())

    return _client


async def complete(history: list[dict]) -> str:
    """
    Send a conversation and return the reply as text.

    `history` is already in the shape the Messages API expects and must end with
    the turn being answered -- the API is stateless, so the whole exchange goes
    up every time.
    """
    try:
        response = await client().messages.create(
            model=MODEL,
            max_tokens=MAX_TOKENS,
            system=SYSTEM,
            messages=history,
        )
    except anthropic.AuthenticationError as error:
        raise ClaudeError(
            "Anthropic rejected the API key. Check `ANTHROPIC_API_KEY` in `chatbot/.env`."
        ) from error
    except anthropic.PermissionDeniedError as error:
        raise ClaudeError(f"That API key is not allowed to use `{MODEL}`.") from error
    except anthropic.NotFoundError as error:
        raise ClaudeError(f"Anthropic does not know a model called `{MODEL}`.") from error
    except anthropic.RateLimitError as error:
        raise ClaudeError("Anthropic is rate limiting me. Try again in a moment.") from error
    except anthropic.APIStatusError as error:
        raise ClaudeError(f"Anthropic answered with an error ({error.status_code}).") from error
    except anthropic.APIConnectionError as error:
        raise ClaudeError("I could not reach Anthropic. Check the network.") from error

    return text_of(response)


def text_of(response) -> str:
    """
    Flatten a response into the one string the chat can render.

    A reply is a list of content blocks, and only the text ones belong on screen.
    A stop that is not `end_turn` is reported as ordinary text as well: a refusal
    or a hit token limit is something to tell the user, not an exception.
    """
    if response.stop_reason == "refusal":
        return "I am not able to answer that one."

    body = "\n\n".join(block.text for block in response.content if block.type == "text")

    if not body:
        return "I had nothing to say to that."

    if response.stop_reason == "max_tokens":
        body += f"\n\n_(Cut off at the {MAX_TOKENS} token reply limit.)_"

    return body
