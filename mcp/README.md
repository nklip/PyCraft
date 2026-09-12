# MCP Chat
<sub>[Back to PyCraft](../README.md#pycraft)</sub>

MCP Chat is a command-line chat client for the Anthropic API that reaches its
tools over the Model Context Protocol. It ships with a document server of its
own, and connects to any number of additional MCP servers named on the command
line.

## Contents
1. [Project structure](#project-structure)
2. [Requirements](#requirements)
3. [Configuration](#configuration)
4. [Start the application](#start-the-application)
5. [Everyday commands](#everyday-commands)
6. [Usage](#usage)
7. [MCP Inspector](#mcp-inspector)
8. [Tests](#tests)
9. [Code style](#code-style)

## Project structure
<sub>[Back to top](#mcp-chat)</sub>

```text
mcp/
├── src/
│   ├── core/
│   │   ├── __init__.py
│   │   ├── chat.py
│   │   ├── claude.py
│   │   ├── cli.py
│   │   ├── cli_chat.py
│   │   └── tools.py
│   ├── main.py
│   ├── mcp_client.py
│   └── mcp_server.py
├── tests/
│   ├── conftest.py
│   ├── helpers.py
│   ├── test_claude.py
│   └── test_tools.py
├── .env.example
├── Makefile
├── pyproject.toml
├── README.md
├── run.sh
└── uv.lock
```

`main.py` wires everything together: it loads configuration, starts
`mcp_server.py` as a subprocess client, and hands the result to the CLI.
`core/` holds the parts worth testing on their own — `claude.py` wraps the
Anthropic API, `tools.py` turns the model's tool requests into MCP calls, and
`chat.py` runs the tool-use loop between them. `cli.py` and `cli_chat.py` are
the prompt-toolkit interface.

The project is named `mcp-chat` in `pyproject.toml` rather than `mcp`, because
a project cannot share a name with its own dependency — the MCP SDK is `mcp`.

Dependencies and tooling configuration all live in `pyproject.toml`. The virtual
environment is created at `mcp/.venv` and is isolated from the other PyCraft
applications.

## Requirements
<sub>[Back to top](#mcp-chat)</sub>

- Python 3.14+ (uv downloads it for you)
- [uv](https://docs.astral.sh/uv/) — `brew install uv`
- An Anthropic API key

## Configuration
<sub>[Back to top](#mcp-chat)</sub>

Configuration is a single `.env` file, git-ignored, created from the committed
`.env.example` template:

| Variable | What it does |
| --- | --- |
| `ANTHROPIC_API_KEY` | Your API secret key. Costs real money; protect it. |
| `CLAUDE_MODEL` | The model the chat client talks to. |

`main.py` asserts that both are non-empty, so it exits immediately rather than
failing on the first request.

## Start the application
<sub>[Back to top](#mcp-chat)</sub>

```bash
./run.sh
```

`run.sh` checks for uv, creates `.env` from `.env.example` when missing, syncs
dependencies, and starts the client. It never runs tests — that is `make test`.

## Everyday commands
<sub>[Back to top](#mcp-chat)</sub>

Run these from the `mcp` directory. `make` on its own lists them.

| Target | What it does |
| --- | --- |
| `make install` | Sync dependencies into `.venv` |
| `make run` | Start the chat client |
| `make test` | Run the test suite |
| `make coverage` | Run the test suite with a coverage report |
| `make lint` | Check formatting and lint rules |
| `make format` | Apply formatting and safe lint fixes |
| `make check` | `lint` plus `test` — everything CI would run |
| `make clean` | Delete caches and build artefacts |

Targets that take extra arguments accept them through `ARGS`:

```bash
make test ARGS="-k tools -vv"
make run ARGS="path/to/another_server.py"
```

Extra arguments to `make run` are MCP server scripts; each one is started and
its tools join the set the model can call.

## Usage
<sub>[Back to top](#mcp-chat)</sub>

### Basic interaction

Type your message and press Enter to chat with the model.

### Document retrieval

Use `@` followed by a document ID to include its content in your query:

```
> Tell me about @deposition.md
```

### Commands

Use the `/` prefix to run a prompt defined in the MCP server. Commands
auto-complete on Tab:

```
> /summarize deposition.md
```

## MCP Inspector
<sub>[Back to top](#mcp-chat)</sub>

The Inspector exercises the document server on its own, without the chat client:

```bash
uv run mcp dev src/mcp_server.py
```

## Tests
<sub>[Back to top](#mcp-chat)</sub>

```bash
make test
```

The suite runs on pytest, configured under `[tool.pytest.ini_options]` in
`pyproject.toml`. `tests/test_tools.py` covers `ToolManager`: collecting tools
across clients, routing a request to the client that has the tool, and the
three ways a call can end — output, an unknown tool, and a raising one.
`tests/test_claude.py` covers the Anthropic wrapper — how messages are
assembled, which optional parameters reach the API, and which do not.

**The suite never calls Anthropic and never starts an MCP server.** The client
is replaced by a fake implementing the two methods `ToolManager` uses, and the
Anthropic transport is replaced by a recorder, so the tests behave the same with
or without a real key in `.env` — and cost nothing to run.

## Code style
<sub>[Back to top](#mcp-chat)</sub>

`ruff` handles both linting and formatting, configured in `pyproject.toml`:

```bash
make format
make lint
```
