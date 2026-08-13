"""
The Anthropic client, without Anthropic.

Every call the SDK would make is replaced here: the suite has to pass the same
way on a machine with a real key in `.env` as on one without.
"""

import asyncio
from types import SimpleNamespace

import anthropic
import httpx
import pytest
from pydantic import SecretStr, ValidationError

from app.chat import claude_client
from app.settings import PLACEHOLDER_API_KEY, Settings, settings

# --- the toggle ------------------------------------------------------------


@pytest.mark.parametrize(
    ("key", "expected"),
    [
        ("sk-ant-api03-a-real-looking-key", True),
        ("", False),
        ("   ", False),
        # run.sh copies .env.example to .env, so an untouched checkout has the
        # variable set to the template value rather than to nothing at all.
        (PLACEHOLDER_API_KEY, False),
    ],
)
def test_a_key_counts_as_configured_only_when_it_could_work(key, expected):
    assert Settings(anthropic_api_key=key).has_anthropic_api_key is expected


def test_the_key_is_not_printed_with_the_settings():
    """It reaches the API and nowhere else -- not a log line, not a traceback."""
    configured = Settings(anthropic_api_key="sk-ant-api03-secret")

    assert "secret" not in repr(configured)
    assert configured.anthropic_api_key.get_secret_value() == "sk-ant-api03-secret"


def test_configured_follows_the_settings(monkeypatch):
    monkeypatch.setattr(settings, "anthropic_api_key", SecretStr("sk-ant-api03-key"))
    assert claude_client.configured() is True

    monkeypatch.setattr(settings, "anthropic_api_key", SecretStr(""))
    assert claude_client.configured() is False


# --- reading a response ----------------------------------------------------


def text_block(text: str) -> SimpleNamespace:
    return SimpleNamespace(type="text", text=text)


def response(*content, stop_reason: str = "end_turn") -> SimpleNamespace:
    return SimpleNamespace(content=list(content), stop_reason=stop_reason)


def test_text_is_taken_from_the_content_blocks():
    assert claude_client.text_of(response(text_block("Because of the air."))) == (
        "Because of the air."
    )


def test_several_text_blocks_are_joined_into_one_message():
    answer = claude_client.text_of(response(text_block("First."), text_block("Second.")))

    assert answer == "First.\n\nSecond."


def test_blocks_that_are_not_text_are_left_out():
    """The chat renders text; anything else in a reply has no place on screen."""
    thinking = SimpleNamespace(type="thinking", thinking="Hmm.")

    assert claude_client.text_of(response(thinking, text_block("Because."))) == "Because."


def test_a_refusal_is_an_ordinary_reply():
    """Nothing went wrong -- the model declined, and the user should hear that."""
    answer = claude_client.text_of(response(stop_reason="refusal"))

    assert "not able to answer" in answer


def test_a_truncated_reply_says_so():
    answer = claude_client.text_of(response(text_block("It goes"), stop_reason="max_tokens"))

    assert answer.startswith("It goes")
    assert str(settings.claude_max_tokens) in answer


def test_an_empty_reply_still_says_something():
    assert claude_client.text_of(response()) != ""


# --- failures --------------------------------------------------------------


def answering(monkeypatch, with_: Exception | SimpleNamespace) -> dict:
    """
    Stand a client in front of `complete()` that raises or returns `with_`.

    Returns the dict of arguments the call was made with, filled in once it has
    been made, so a test can check what would have gone to Anthropic.
    """
    sent = {}

    async def create(**kwargs):
        sent.update(kwargs)
        if isinstance(with_, Exception):
            raise with_
        return with_

    monkeypatch.setattr(
        claude_client,
        "client",
        lambda: SimpleNamespace(messages=SimpleNamespace(create=create)),
    )

    return sent


def ask() -> str:
    return asyncio.run(claude_client.complete([{"role": "user", "content": "Hi"}]))


def api_error(status: int, kind: type[anthropic.APIStatusError]) -> anthropic.APIStatusError:
    request = httpx.Request("POST", "https://api.anthropic.com/v1/messages")
    return kind("boom", response=httpx.Response(status, request=request), body=None)


@pytest.mark.parametrize(
    ("raised", "expected"),
    [
        (api_error(401, anthropic.AuthenticationError), "rejected the API key"),
        (api_error(403, anthropic.PermissionDeniedError), "not allowed"),
        (api_error(404, anthropic.NotFoundError), "does not know a model"),
        (api_error(429, anthropic.RateLimitError), "rate limiting"),
        (api_error(500, anthropic.InternalServerError), "answered with an error"),
        (
            anthropic.APIConnectionError(
                request=httpx.Request("POST", "https://api.anthropic.com/v1/messages")
            ),
            "could not reach",
        ),
    ],
)
def test_every_failure_becomes_something_worth_reading(monkeypatch, raised, expected):
    """The mode renders these as-is, so none of them may reach the user as a stack."""
    answering(monkeypatch, with_=raised)

    with pytest.raises(claude_client.ClaudeError) as error:
        ask()

    assert expected in str(error.value)


def test_a_successful_call_comes_back_as_text(monkeypatch):
    answering(monkeypatch, with_=response(text_block("Because of the air.")))

    assert ask() == "Because of the air."


# --- the model and the reply ceiling ---------------------------------------


def test_the_defaults_work_without_an_env_file():
    """`.env` is optional for these two: the code ships usable values."""
    without_env = Settings(_env_file=None)

    assert without_env.claude_model == "claude-haiku-4-5"
    assert without_env.claude_max_tokens == 4096


def test_the_call_uses_whatever_the_settings_say(monkeypatch):
    """Changing the model is an `.env` edit, not a code change."""
    sent = answering(monkeypatch, with_=response(text_block("Fine.")))
    monkeypatch.setattr(settings, "claude_model", "claude-sonnet-5")
    monkeypatch.setattr(settings, "claude_max_tokens", 128)

    ask()

    assert sent["model"] == "claude-sonnet-5"
    assert sent["max_tokens"] == 128


def test_the_reply_ceiling_has_to_be_a_positive_number():
    """A zero or negative ceiling would fail on every call instead of at startup."""
    with pytest.raises(ValidationError):
        Settings(claude_max_tokens=0)

    with pytest.raises(ValidationError):
        Settings(claude_max_tokens=-1)


def test_the_client_is_built_once(monkeypatch):
    monkeypatch.setattr(settings, "anthropic_api_key", SecretStr("sk-ant-api03-key"))
    monkeypatch.setattr(claude_client, "_client", None)

    assert claude_client.client() is claude_client.client()
