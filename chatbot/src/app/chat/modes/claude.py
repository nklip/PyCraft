"""
Claude mode: sends the conversation to the model and replies with the answer.

The mode is a toggle. Without an API key it stays reachable, listed by help, and
answers with what to do about it -- so a checkout with no key is a chat that
explains itself rather than one with a broken mode in it. `claude_client.py`
owns the key, the model, and the call; this module owns the turn.

Still to come, in rough order: trimming or compacting the history as it grows,
streaming the reply as deltas land instead of waiting for the whole turn, and a
tool call with a schema so a table comes back as data for `messages.table`
rather than as prose to parse.
"""

from app.chat import claude_client, conversations, messages
from app.chat.conversations import Conversation

# Opting in is what gets this mode the conversation at all. Dispatch hands the
# history only to modes that declare they need it, so no other mode is even in a
# position to write to it: the session holds the exchange with the model and
# nothing else.
NEEDS_HISTORY = True

NAME = "claude"
SUMMARY = "Ask Claude. Needs an Anthropic API key."
USAGE = "claude: Why is the sky blue?"


DISABLED = (
    "Claude mode is switched off because no `ANTHROPIC_API_KEY` was found. "
    "Put a key in `chatbot/.env` as `ANTHROPIC_API_KEY=sk-ant-...` and restart the "
    "server, and this mode answers for real.\n\n"
    "Every other mode works without it -- say `help` for the list."
)


async def reply(argument: str, conversation: Conversation) -> dict:
    if not argument:
        return messages.text(f"Ask something, like `{USAGE}`.")

    if not claude_client.configured():
        return messages.text(DISABLED)

    # The question goes up with the history but is not recorded until it has been
    # answered: a history holding a turn the model never replied to would be
    # resent on every later turn.
    turn = [*conversation.history, {"role": conversations.USER, "content": argument}]

    try:
        answer = await claude_client.complete(turn)
    except claude_client.ClaudeError as error:
        return messages.text(str(error))

    conversation.record(conversations.USER, argument)
    conversation.record(conversations.ASSISTANT, answer)

    return messages.text(answer)
