# Chatbot
<sub>[Back to PyCraft](../README.md#pycraft)</sub>

Chatbot is a FastAPI application serving a WebSocket chat UI.

## Contents
1. [Project structure](#project-structure)
2. [Requirements](#requirements)
3. [Configuration](#configuration)
4. [Start the application](#start-the-application)
5. [Everyday commands](#everyday-commands)
6. [Tests](#tests)
7. [Code style](#code-style)

## Project structure
<sub>[Back to top](#chatbot)</sub>

```text
chatbot/
├── src/
│   ├── static/
│   ├── templates/
│   ├── connection_manager.py
│   ├── main.py
│   ├── models.py
│   └── settings.py
├── tests/
│   └── test_main.py
├── .env.example
├── Makefile
├── pyproject.toml
└── run.sh
```

Dependencies and tooling configuration all live in `pyproject.toml`. The virtual
environment is created at `chatbot/.venv` and is isolated from the other PyCraft
applications.

## Requirements
<sub>[Back to top](#chatbot)</sub>

- [uv](https://docs.astral.sh/uv/) — manages the Python version, the virtual
  environment, and dependencies

```bash
brew install uv
```

uv downloads Python 3.14 itself if the machine does not already have it, so no
interpreter needs to be installed separately.

## Configuration
<sub>[Back to top](#chatbot)</sub>

Configuration lives in `chatbot/.env`, which `run.sh` creates from
`.env.example` on first run. `src/settings.py` reads it through
`pydantic-settings`, so every value is typed, has a default, and can be
overridden by a real environment variable.

| Variable | Default | Purpose |
| --- | --- | --- |
| `PROFILE` | `local` | Names the running environment; surfaced in the page template |
| `WS_HOST` | `ws://127.0.0.1:8000` | WebSocket endpoint the browser connects back to |

`.env` is git-ignored; `.env.example` is the committed template.

## Start the application
<sub>[Back to top](#chatbot)</sub>

Run this command from the top-level `PyCraft` directory:

```bash
./chatbot/run.sh
```

The launcher:

1. Verifies that uv is available.
2. Creates `.env` from `.env.example` if it is missing.
3. Syncs `chatbot/.venv` against `pyproject.toml`.
4. Starts the Uvicorn development server.

It deliberately does not run the tests; `make test` does that.

Then open <http://127.0.0.1:8000/chatbot>.

Arguments are forwarded to Uvicorn. For example:

```bash
./chatbot/run.sh --reload
```

## Everyday commands
<sub>[Back to top](#chatbot)</sub>

Run these from the `chatbot` directory. `make` on its own lists them.

| Target | What it does |
| --- | --- |
| `make install` | Sync dependencies into `.venv` |
| `make run` | Start the development server |
| `make test` | Run the test suite |
| `make coverage` | Run the test suite with a coverage report |
| `make lint` | Check formatting and lint rules |
| `make format` | Apply formatting and safe lint fixes |
| `make check` | `lint` plus `test` — everything CI would run |
| `make clean` | Delete caches and build artefacts |

Targets that take extra arguments accept them through `ARGS`:

```bash
make test ARGS="-k socket -vv"
make run ARGS="--reload"
```

## Tests
<sub>[Back to top](#chatbot)</sub>

```bash
make test
```

The suite runs on pytest, configured under `[tool.pytest.ini_options]` in
`pyproject.toml`. `tests/test_main.py` covers the two entry points: the rendered
page and a WebSocket round trip through `process_message`.

## Code style
<sub>[Back to top](#chatbot)</sub>

`ruff` handles both linting and formatting, configured in `pyproject.toml`:

```bash
make format
make lint
```
