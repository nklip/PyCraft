"""Application configuration, read from the environment and from chatbot/.env."""

from pathlib import Path

from pydantic import SecretStr
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

    @property
    def has_anthropic_api_key(self) -> bool:
        """Whether a key that could plausibly work was configured."""
        key = self.anthropic_api_key.get_secret_value().strip()
        return bool(key) and key != PLACEHOLDER_API_KEY


settings = Settings()
