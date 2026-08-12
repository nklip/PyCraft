#!/usr/bin/env bash
#
# Brings Lemon up from scratch: dependencies, database, migrations, sample data,
# development server. Tests are deliberately not part of this path -- run them
# with `make test`.

set -Eeuo pipefail

LEMON_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
cd "${LEMON_DIR}"

if ! command -v uv >/dev/null 2>&1; then
    echo "uv is required to manage Lemon's dependencies." >&2
    echo "Install it with: brew install uv" >&2
    exit 1
fi

if ! docker compose version >/dev/null 2>&1; then
    echo "Docker Compose is required to start Lemon's MySQL service." >&2
    exit 1
fi

if ! docker info >/dev/null 2>&1; then
    echo "Docker is not running. Start Docker Desktop and try again." >&2
    exit 1
fi

if [[ ! -f .env ]]; then
    echo "Creating .env from .env.example..."
    cp .env.example .env
fi

echo "Syncing dependencies..."
uv sync

echo "Starting MySQL..."
docker compose up --detach --wait mysql

echo "Applying database migrations..."
uv run python src/manage.py migrate --noinput

MEAL_COUNT="$(uv run python src/manage.py shell --no-imports \
    --command='from api.models import Meal; print(Meal.objects.count())')"
if [[ "${MEAL_COUNT}" == "0" ]]; then
    echo "Loading sample catalog data..."
    uv run python src/manage.py loaddata Category Cuisine Meal
else
    echo "Catalog data already exists; skipping sample fixtures."
fi

echo "Starting Lemon server..."
exec uv run python src/manage.py runserver "$@"
