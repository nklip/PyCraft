"""Each mode, exercised without a socket."""

import pytest

from app.chat import messages, modes


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
    assert modes.dispatch(text)["text"] == expected


def test_echo_without_an_argument_explains_itself():
    assert "echo: Test" in modes.dispatch("echo:")["text"]


def test_help_lists_every_registered_mode():
    body = modes.dispatch("help")["text"]

    for name in modes.MODES:
        assert name in body, f"help does not mention the {name} mode"


def test_help_can_describe_one_mode():
    body = modes.dispatch("help: echo")["text"]

    assert modes.MODES["echo"].SUMMARY in body
    assert modes.MODES["claude"].SUMMARY not in body


def test_help_rejects_an_unknown_mode():
    assert "no mode called" in modes.dispatch("help: nonsense")["text"]


def test_type_table_renders_the_catalog():
    reply = modes.dispatch("type: table")

    assert reply["template_type"] == messages.TABLE
    assert len(reply["msg_payload"]) == 6
    assert reply["msg_payload"][0]["Name"] == "Umbrealla corporation"


def test_type_text_renders_a_text_message():
    assert modes.dispatch("type: text")["template_type"] == messages.TEXT


def test_type_lists_what_it_can_render_when_asked_for_something_else():
    body = modes.dispatch("type: hologram")["text"]

    assert "hologram" in body
    assert messages.TABLE in body


def test_claude_is_scaffolded_but_not_wired_up():
    body = modes.dispatch("claude: Why is the sky blue?")["text"]

    assert "not wired up yet" in body


def test_unknown_mode_points_at_help():
    body = modes.dispatch("do a backflip")["text"]

    assert "help" in body


def test_mode_names_are_case_insensitive():
    assert modes.dispatch("ECHO: Test")["text"] == modes.dispatch("echo: Test")["text"]


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
