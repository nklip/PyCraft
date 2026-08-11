#!/usr/bin/env bash

set -Eeuo pipefail

CHATBOT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(cd -- "${CHATBOT_DIR}/.." && pwd)"
VENV_DIR="${PROJECT_DIR}/.venv"
REQUIREMENTS_FILE="${CHATBOT_DIR}/requirements.txt"
PROFILE_FILE="${CHATBOT_DIR}/profile/chatbot.local.profile"

if [[ ! -x "${VENV_DIR}/bin/python" ]]; then
    echo "Creating virtual environment at ${VENV_DIR}..."
    python3 -m venv "${VENV_DIR}"
fi

echo "Activating virtual environment..."
source "${VENV_DIR}/bin/activate"

echo "Installing dependencies from ${REQUIREMENTS_FILE}..."
python -m pip install -r "${REQUIREMENTS_FILE}"

echo "Loading profile from ${PROFILE_FILE}..."
set -a
source "${PROFILE_FILE}"
set +a

cd "${CHATBOT_DIR}"

echo "Starting chatbot server..."
exec python -m uvicorn main:server "$@"
