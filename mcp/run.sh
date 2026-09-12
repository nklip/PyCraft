#!/usr/bin/env bash
#
# Brings MCP Chat up from scratch: dependencies, configuration, chat client.
# Tests are deliberately not part of this path -- run them with `make test`.

set -Eeuo pipefail

MCP_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
cd "${MCP_DIR}"

if ! command -v uv >/dev/null 2>&1; then
    echo "uv is required to manage MCP Chat's dependencies." >&2
    echo "Install it with: brew install uv" >&2
    exit 1
fi

if [[ ! -f .env ]]; then
    echo "Creating .env from .env.example..."
    cp .env.example .env
    echo "Set ANTHROPIC_API_KEY in .env before chatting." >&2
fi

echo "Syncing dependencies..."
uv sync

echo "Starting MCP Chat..."
exec uv run python src/main.py "$@"
