#!/usr/bin/env bash
#
# Brings Mathparser up from scratch: dependencies, then the interactive parser.
# Tests are deliberately not part of this path -- run them with `make test`.

set -Eeuo pipefail

MATHPARSER_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
cd "${MATHPARSER_DIR}"

if ! command -v uv >/dev/null 2>&1; then
    echo "uv is required to manage Mathparser's dependencies." >&2
    echo "Install it with: brew install uv" >&2
    exit 1
fi

echo "Syncing dependencies..."
uv sync

echo "Starting Mathparser..."
echo "Enter an expression, or type 'exit' or 'quit' to stop."
exec uv run python src/main.py "$@"
