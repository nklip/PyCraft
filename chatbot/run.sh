#!/usr/bin/env bash

set -Eeuo pipefail

CHATBOT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
SOURCE_DIR="${CHATBOT_DIR}/src"
VENV_DIR="${CHATBOT_DIR}/.venv"
REQUIREMENTS_FILE="${CHATBOT_DIR}/requirements.txt"
PROFILE_FILE="${CHATBOT_DIR}/profile/chatbot.local.profile"
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

echo "Installing dependencies from ${REQUIREMENTS_FILE}..."
python -m pip install -r "${REQUIREMENTS_FILE}"

echo "Loading profile from ${PROFILE_FILE}..."
set -a
source "${PROFILE_FILE}"
set +a

cd "${SOURCE_DIR}"

echo "Starting chatbot server..."
printf 'Open Chatbot at \033[1mhttp://127.0.0.1:8000/chatbot\033[0m\n'
exec python -m uvicorn main:server "$@"
