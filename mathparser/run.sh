#!/usr/bin/env bash

set -Eeuo pipefail

MATHPARSER_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
SOURCE_DIR="${MATHPARSER_DIR}/src"
VENV_DIR="${MATHPARSER_DIR}/.venv"
PYTHON_COMMAND="${PYTHON_COMMAND:-python3.14}"

if [[ ! -x "${VENV_DIR}/bin/python" ]]; then
    echo "Creating virtual environment at ${VENV_DIR}..."
    if ! command -v "${PYTHON_COMMAND}" >/dev/null 2>&1; then
        echo "Python command '${PYTHON_COMMAND}' was not found." >&2
        exit 1
    fi
    "${PYTHON_COMMAND}" -m venv "${VENV_DIR}"
fi

echo "Activating virtual environment..."
source "${VENV_DIR}/bin/activate"

export PYTHONPATH="${SOURCE_DIR}${PYTHONPATH:+:${PYTHONPATH}}"

if [[ "${1:-}" == "--test" ]]; then
    cd "${MATHPARSER_DIR}"
    exec python -m unittest discover --start-directory tests --verbose
fi

cd "${SOURCE_DIR}"

echo "Starting Mathparser..."
echo "Enter an expression, or type 'exit' or 'quit' to stop."
exec python main.py "$@"
