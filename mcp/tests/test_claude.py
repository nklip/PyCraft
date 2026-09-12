import pytest
from anthropic.types import Message, TextBlock
from helpers import TextBlockStub

from core.claude import Claude


class RecordingMessages:
    """Captures the kwargs Claude.chat builds instead of calling the API."""

    def __init__(self):
        self.calls = []

    def create(self, **params):
        self.calls.append(params)
        return "response"


@pytest.fixture
def claude():
    service = Claude(model="claude-haiku-4-5")
    service.client.messages = RecordingMessages()
    return service


def assistant_message(text: str) -> Message:
    return Message(
        id="msg_1",
        content=[TextBlock(type="text", text=text)],
        model="claude-haiku-4-5",
        role="assistant",
        stop_reason="end_turn",
        type="message",
        usage={"input_tokens": 1, "output_tokens": 1},
    )


def test_add_user_message_accepts_plain_text(claude):
    messages = []

    claude.add_user_message(messages, "hello")

    assert messages == [{"role": "user", "content": "hello"}]


def test_add_user_message_unwraps_a_message(claude):
    messages = []
    reply = assistant_message("hi there")

    claude.add_user_message(messages, reply)

    assert messages[0]["role"] == "user"
    assert messages[0]["content"] is reply.content


def test_add_assistant_message_unwraps_a_message(claude):
    messages = []
    reply = assistant_message("hi there")

    claude.add_assistant_message(messages, reply)

    assert messages[0] == {"role": "assistant", "content": reply.content}


def test_text_from_message_keeps_only_text_blocks(claude):
    message = type("M", (), {"content": [TextBlockStub("one"), TextBlockStub("two")]})()

    assert claude.text_from_message(message) == "one\ntwo"


def test_chat_sends_the_model_and_messages(claude):
    claude.chat(messages=[{"role": "user", "content": "hi"}])

    params = claude.client.messages.calls[0]
    assert params["model"] == "claude-haiku-4-5"
    assert params["messages"] == [{"role": "user", "content": "hi"}]
    assert params["stop_sequences"] == []


def test_chat_omits_optional_parameters_by_default(claude):
    claude.chat(messages=[])

    params = claude.client.messages.calls[0]
    assert "tools" not in params
    assert "system" not in params
    assert "thinking" not in params


def test_chat_includes_optional_parameters_when_asked(claude):
    claude.chat(messages=[], system="be brief", tools=[{"name": "read"}], thinking=True)

    params = claude.client.messages.calls[0]
    assert params["system"] == "be brief"
    assert params["tools"] == [{"name": "read"}]
    assert params["thinking"] == {"type": "enabled", "budget_tokens": 1024}


def test_stop_sequences_do_not_leak_between_calls(claude):
    """The default used to be a shared list, so anything appended to one call's
    stop sequences showed up in every later call."""
    claude.chat(messages=[])
    claude.client.messages.calls[0]["stop_sequences"].append("STOP")

    claude.chat(messages=[])

    assert claude.client.messages.calls[1]["stop_sequences"] == []
