"""Application configuration, read from the environment and from chatbot/.env."""

from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

# chatbot/ -- up out of src/chatbot/
PROJECT_DIR = Path(__file__).resolve().parents[2]

# Where the browser fetches assets from. Fixed rather than injected per request,
# so templates and JavaScript can reference assets without Python rendering them.
STATIC_URL = "/chatbot/static"


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


settings = Settings()
