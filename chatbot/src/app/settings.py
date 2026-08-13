"""Application configuration, read from the environment and from chatbot/.env."""

from pathlib import Path

from pydantic import Field, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict

# chatbot/ -- up out of src/chatbot/
PROJECT_DIR = Path(__file__).resolve().parents[2]

# Where the browser fetches assets from. Fixed rather than injected per request,
# so templates and JavaScript can reference assets without Python rendering them.
STATIC_URL = "/chatbot/static"

# The stand-in `.env.example` carries. run.sh copies that file to `.env` on a
# first run, so a fresh checkout has the variable set to something that is not a
# key -- counting it as configured would send it to Anthropic and get a 401 back
# instead of the setup explanation the user actually needs.
PLACEHOLDER_API_KEY = "sk-ant-api03-your-api-key-here"


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=PROJECT_DIR / ".env",
        env_file_encoding="utf-8",
        # Real environment variables win over .env, so a deployment can override
        # any single value without shipping a file.
        extra="ignore",
    )

    # Names the running environment; surfaced in the page template.
    profile: str = "local"

    # WebSocket endpoint the browser connects back to.
    ws_host: str = "ws://127.0.0.1:8000"

    # Read from ANTHROPIC_API_KEY. Unset is a supported state, not an error: the
    # claude mode explains itself instead of calling the model, and the rest of
    # the chat is unaffected. SecretStr so the value cannot reach a log or a
    # traceback by being printed alongside the settings it lives in.
    anthropic_api_key: SecretStr = SecretStr("")

    # The model the claude mode talks to. Haiku is the smallest and quickest in
    # the family: a chat reply is short and someone is watching the socket for
    # it, so latency matters more here than depth would.
    claude_model: str = "claude-haiku-4-5"

    # A ceiling on a runaway answer rather than a target: replies are read in a
    # chat bubble, and this is what caps the cost of a single turn. Only "more
    # than nothing" is enforced here -- each model has its own upper limit, so
    # the API is the thing that knows it, and it answers with an error the chat
    # reports like any other.
    claude_max_tokens: int = Field(default=4096, gt=0)

    @property
    def has_anthropic_api_key(self) -> bool:
        """Whether a key that could plausibly work was configured."""
        key = self.anthropic_api_key.get_secret_value().strip()
        return bool(key) and key != PLACEHOLDER_API_KEY


settings = Settings()
