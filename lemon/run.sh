#!/usr/bin/env bash

set -Eeuo pipefail

LEMON_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
SOURCE_DIR="${LEMON_DIR}/src"
VENV_DIR="${LEMON_DIR}/.venv"
REQUIREMENTS_FILE="${LEMON_DIR}/requirements.txt"
COMPOSE_FILE="${LEMON_DIR}/compose.yaml"
PYTHON_COMMAND="${PYTHON_COMMAND:-python3.14}"

export MYSQL_DATABASE="${MYSQL_DATABASE:-lemon}"
export MYSQL_HOST="${MYSQL_HOST:-127.0.0.1}"
export MYSQL_PASSWORD="${MYSQL_PASSWORD:-mysql_fid}"
export MYSQL_PORT="${MYSQL_PORT:-3306}"
export MYSQL_ROOT_PASSWORD="${MYSQL_ROOT_PASSWORD:-root}"
export MYSQL_USER="${MYSQL_USER:-mysql_fid}"

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

if ! docker compose version >/dev/null 2>&1; then
    echo "Docker Compose is required to start Lemon's MySQL service." >&2
    exit 1
fi

if ! docker info >/dev/null 2>&1; then
    echo "Docker is not running. Start Docker Desktop and try again." >&2
    exit 1
fi

echo "Starting MySQL..."
docker compose -f "${COMPOSE_FILE}" up --detach --wait mysql

cd "${SOURCE_DIR}"

echo "Applying database migrations..."
python manage.py migrate --noinput

MEAL_COUNT="$(python manage.py shell --no-imports --command='from api.models import Meal; print(Meal.objects.count())')"
if [[ "${MEAL_COUNT}" == "0" ]]; then
    echo "Loading sample catalog data..."
    python manage.py loaddata \
        "${SOURCE_DIR}/api/fixtures/Category.json" \
        "${SOURCE_DIR}/api/fixtures/Cuisine.json" \
        "${SOURCE_DIR}/api/fixtures/Meal.json"
else
    echo "Catalog data already exists; skipping sample fixtures."
fi

echo "Starting Lemon server..."
exec python manage.py runserver "$@"
