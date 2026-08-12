#!/usr/bin/env bash
#
# Brings Chatbot up from scratch: dependencies, configuration, development
# server. Tests are deliberately not part of this path -- run them with
# `make test`.

set -Eeuo pipefail

CHATBOT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
cd "${CHATBOT_DIR}"

if ! command -v uv >/dev/null 2>&1; then
    echo "uv is required to manage Chatbot's dependencies." >&2
    echo "Install it with: brew install uv" >&2
    exit 1
fi

if [[ ! -f .env ]]; then
    echo "Creating .env from .env.example..."
    cp .env.example .env
fi

echo "Syncing dependencies..."
uv sync

echo "Starting chatbot server..."
printf 'Open Chatbot at \033[1mhttp://127.0.0.1:8000/chatbot\033[0m\n'
exec uv run uvicorn --app-dir src main:server "$@"
