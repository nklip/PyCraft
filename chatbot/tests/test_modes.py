"""Each mode, exercised without a socket."""

import asyncio

import pytest

from app.chat import messages, modes
from app.chat.conversations import Conversation


def dispatch(text: str, conversation: Conversation | None = None) -> dict:
    """Run one message through the dispatcher. Sync so the tests stay plain."""
    return asyncio.run(modes.dispatch(text, conversation or Conversation()))


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("echo: Test", "Hello from backend! Did you say 'Test'?"),
        ("echo: hello world", "Hello from backend! Did you say 'hello world'?"),
        # The separator may be written without a space, or with several.
        ("echo:Test", "Hello from backend! Did you say 'Test'?"),
        ("echo:   Test  ", "Hello from backend! Did you say 'Test'?"),
        # Only the first separator splits, so colons survive in the argument.
        ("echo: a: b", "Hello from backend! Did you say 'a: b'?"),
    ],
)
def test_echo_repeats_the_argument(text, expected):
    assert dispatch(text)["text"] == expected


def test_echo_without_an_argument_explains_itself():
    assert "echo: Test" in dispatch("echo:")["text"]


def test_help_lists_every_registered_mode():
    body = dispatch("help")["text"]

    for name in modes.MODES:
        assert name in body, f"help does not mention the {name} mode"


def test_help_can_describe_one_mode():
    body = dispatch("help: echo")["text"]

    assert modes.MODES["echo"].SUMMARY in body
    assert modes.MODES["claude"].SUMMARY not in body


def test_help_rejects_an_unknown_mode():
    assert "no mode called" in dispatch("help: nonsense")["text"]


def test_type_table_renders_the_catalog():
    reply = dispatch("type: table")

    assert reply["template_type"] == messages.TABLE
    assert len(reply["msg_payload"]) == 6
    assert reply["msg_payload"][0]["Name"] == "Umbrealla corporation"


def test_type_text_renders_a_text_message():
    assert dispatch("type: text")["template_type"] == messages.TEXT


def test_type_lists_what_it_can_render_when_asked_for_something_else():
    body = dispatch("type: hologram")["text"]

    assert "hologram" in body
    assert messages.TABLE in body


def test_unknown_mode_points_at_help():
    assert "help" in dispatch("do a backflip")["text"]


def test_mode_names_are_case_insensitive():
    assert dispatch("ECHO: Test")["text"] == dispatch("echo: Test")["text"]


@pytest.mark.parametrize(
    ("text", "name", "argument"),
    [
        ("echo: Test", "echo", "Test"),
        ("help", "help", ""),
        ("type:table", "type", "table"),
        ("", "", ""),
    ],
)
def test_parse_splits_mode_from_argument(text, name, argument):
    assert modes.parse(text) == (name, argument)


# --- claude mode and conversation history ---------------------------------


def test_claude_is_scaffolded_but_not_wired_up():
    assert "not wired up yet" in dispatch("claude: Why is the sky blue?")["text"]


def test_claude_records_both_sides_of_the_turn():
    conversation = Conversation()

    dispatch("claude: first", conversation)

    assert [turn["role"] for turn in conversation.history] == ["user", "assistant"]
    assert conversation.history[0]["content"] == "first"


def test_claude_accumulates_history_within_one_conversation():
    conversation = Conversation()

    dispatch("claude: first", conversation)
    dispatch("claude: second", conversation)

    assert conversation.turns == 4
    assert [turn["content"] for turn in conversation.history if turn["role"] == "user"] == [
        "first",
        "second",
    ]


def test_claude_without_an_argument_records_nothing():
    conversation = Conversation()

    dispatch("claude:", conversation)

    assert conversation.turns == 0


def test_other_modes_do_not_touch_the_history():
    conversation = Conversation()

    dispatch("echo: Test", conversation)
    dispatch("help", conversation)
    dispatch("type: table", conversation)

    assert conversation.turns == 0


def test_conversations_are_isolated_from_each_other():
    one, two = Conversation(), Conversation()

    dispatch("claude: mine", one)
    dispatch("claude: yours", two)
    dispatch("claude: mine again", one)

    assert one.turns == 4
    assert two.turns == 2
    assert "yours" not in [turn["content"] for turn in one.history]


def test_every_conversation_gets_its_own_session_id():
    ids = {Conversation().session_id for _ in range(100)}

    assert len(ids) == 100


def test_session_id_is_a_uuid():
    from uuid import UUID

    conversation = Conversation()

    assert UUID(conversation.session_id).version == 4
    assert conversation.short_id == conversation.session_id.split("-")[0]
