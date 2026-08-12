RUN := uv run

# Extra arguments for targets that forward them, e.g. `make test ARGS="-k chat"`.
ARGS ?=

.DEFAULT_GOAL := help
.PHONY: help install run test coverage lint format check clean

help:  ## Show this help
	@grep -hE '^[a-zA-Z_-]+:.*?##' $(MAKEFILE_LIST) \
		| awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-14s\033[0m %s\n", $$1, $$2}'

install:  ## Install dependencies into .venv
	uv sync

run:  ## Start the development server
	$(RUN) uvicorn --app-dir src main:server $(ARGS)

test:  ## Run the test suite
	$(RUN) pytest $(ARGS)

coverage:  ## Run the test suite with a coverage report
	$(RUN) pytest --cov --cov-report=term $(ARGS)

lint:  ## Check formatting and lint rules
	$(RUN) ruff check .
	$(RUN) ruff format --check .

format:  ## Apply formatting and safe lint fixes
	$(RUN) ruff format .
	$(RUN) ruff check --fix .

check: lint test  ## Everything CI would run

clean:  ## Delete caches and build artefacts
	rm -rf .pytest_cache .ruff_cache .coverage htmlcov
	find src tests -type d -name __pycache__ -prune -exec rm -rf {} +
