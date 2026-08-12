# Mathparser
<sub>[Back to PyCraft](../README.md#pycraft)</sub>

Mathparser is an interactive top-down mathematical expression parser.

## Contents
1. [Project structure](#project-structure)
2. [Requirements](#requirements)
3. [Start the application](#start-the-application)
4. [Everyday commands](#everyday-commands)
5. [Tests](#tests)
6. [Code style](#code-style)

## Project structure
<sub>[Back to top](#mathparser)</sub>

```text
mathparser/
├── src/
│   ├── calculator/
│   └── main.py
├── tests/
├── Makefile
├── pyproject.toml
├── README.md
├── run.sh
└── uv.lock
```

Tooling configuration lives in `pyproject.toml`. The virtual environment is
created at `mathparser/.venv` and is isolated from the other PyCraft
applications.

## Requirements
<sub>[Back to top](#mathparser)</sub>

- [uv](https://docs.astral.sh/uv/) — manages the Python version, the virtual
  environment, and dependencies

```bash
brew install uv
```

uv downloads Python 3.14 itself if the machine does not already have it, so no
interpreter needs to be installed separately.

Mathparser uses only the Python standard library, so it has no runtime
dependencies. The `.venv` exists to hold the development tools.

## Start the application
<sub>[Back to top](#mathparser)</sub>

Run this command from the top-level `PyCraft` directory:

```bash
./mathparser/run.sh
```

Enter a mathematical expression at the prompt. Type `exit` or `quit` to stop.

Example:

```text
Enter your expression: 2 + 3 * 4
14.0
Enter your expression: quit
```

## Everyday commands
<sub>[Back to top](#mathparser)</sub>

Run these from the `mathparser` directory. `make` on its own lists them.

| Target | What it does |
| --- | --- |
| `make install` | Sync development tools into `.venv` |
| `make run` | Start the interactive parser |
| `make test` | Run the test suite |
| `make coverage` | Run the test suite with a coverage report |
| `make lint` | Check formatting and lint rules |
| `make format` | Apply formatting and safe lint fixes |
| `make check` | `lint` plus `test` — everything CI would run |
| `make clean` | Delete caches and build artefacts |

Targets that take extra arguments accept them through `ARGS`:

```bash
make test ARGS="-k division -vv"
```

## Tests
<sub>[Back to top](#mathparser)</sub>

```bash
make test
```

The suite runs on pytest, configured under `[tool.pytest.ini_options]` in
`pyproject.toml`. The tests are `unittest.TestCase` classes and pytest runs them
unchanged.

## Code style
<sub>[Back to top](#mathparser)</sub>

`ruff` handles both linting and formatting, configured in `pyproject.toml`:

```bash
make format
make lint
```
