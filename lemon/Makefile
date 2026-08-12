RUN := uv run
MANAGE := $(RUN) python src/manage.py

# Extra arguments for targets that forward them, e.g. `make test ARGS="-k cart"`.
ARGS ?=

.DEFAULT_GOAL := help
.PHONY: help install run test coverage lint format check migrate makemigrations \
        superuser shell fixtures db-up db-stop db-down db-reset clean

help:  ## Show this help
	@grep -hE '^[a-zA-Z_-]+:.*?##' $(MAKEFILE_LIST) \
		| awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-14s\033[0m %s\n", $$1, $$2}'

install:  ## Install dependencies into .venv
	uv sync

run:  ## Start the development server
	$(MANAGE) runserver $(ARGS)

test: db-up  ## Run the test suite
	$(RUN) pytest $(ARGS)

coverage: db-up  ## Run the test suite with a coverage report
	$(RUN) pytest --cov --cov-report=term $(ARGS)

lint:  ## Check formatting and lint rules
	$(RUN) ruff check .
	$(RUN) ruff format --check .

format:  ## Apply formatting and safe lint fixes
	$(RUN) ruff format .
	$(RUN) ruff check --fix .

check: lint test  ## Everything CI would run

migrate: db-up  ## Apply database migrations
	$(MANAGE) migrate --noinput

makemigrations:  ## Generate migrations for the api and lemon apps
	$(MANAGE) makemigrations api lemon

superuser: db-up  ## Create an administrator account
	$(MANAGE) createsuperuser

shell: db-up  ## Open the Django shell
	$(MANAGE) shell

fixtures: db-up  ## Load the sample catalog, overwriting existing rows
	$(MANAGE) loaddata Category Cuisine Meal

db-up:  ## Start MySQL and wait until it is healthy
	docker compose up --detach --wait mysql

db-stop:  ## Stop MySQL, keeping its data
	docker compose stop mysql

db-down:  ## Remove the container, keeping its data volume
	docker compose down

db-reset:  ## Remove the container and delete its data volume
	docker compose down --volumes

clean:  ## Delete caches and build artefacts
	rm -rf .pytest_cache .ruff_cache .coverage htmlcov
	find src -type d -name __pycache__ -prune -exec rm -rf {} +
