# Chatbot
<sub>[Back to PyCraft](../README.md#pycraft)</sub>

Chatbot is a FastAPI application serving a WebSocket chat UI.

There is no Django here. Django belongs to [lemon](../lemon/README.md);
this project is FastAPI plus vanilla JavaScript, and a fourth project should
not assume the repository is a Django repository.

## Contents
1. [Project structure](#project-structure)
2. [Sessions](#sessions)
3. [Modes](#modes)
4. [How the frontend loads](#how-the-frontend-loads)
5. [Requirements](#requirements)
6. [Configuration](#configuration)
7. [Start the application](#start-the-application)
8. [Everyday commands](#everyday-commands)
9. [Tests](#tests)
10. [Code style](#code-style)

## Project structure
<sub>[Back to top](#chatbot)</sub>

```text
chatbot/
├── src/
│   └── app/
│       ├── chat/
│       │   ├── modes/
│       │   │   ├── claude.py
│       │   │   ├── echo.py
│       │   │   ├── help.py
│       │   │   └── types.py
│       │   ├── catalog.py
│       │   ├── connections.py
│       │   ├── conversations.py
│       │   ├── messages.py
│       │   ├── router.py
│       │   └── schemas.py
│       ├── static/
│       │   ├── css/
│       │   ├── img/
│       │   ├── js/
│       │   └── vendor/
│       ├── templates/
│       │   └── index.html
│       ├── main.py
│       ├── pages.py
│       └── settings.py
├── tests/
│   ├── test_app.py
│   └── test_modes.py
├── .env.example
├── Makefile
├── pyproject.toml
├── README.md
├── run.sh
└── uv.lock
```

`static/vendor/` holds third-party libraries exactly as downloaded, so
hand-written code is never mistaken for a vendored one.

### How the Python is organised

Modules are grouped **by feature, not by technical layer**. There is no `models/`
next to `schemas/` next to `services/`; instead everything belonging to the chat
lives in `chat/`, using the conventional FastAPI file names — `router.py` for
endpoints, `schemas.py` for the Pydantic wire shapes, and the modules that make
up the feature beside them. Incoming socket messages are validated against
`schemas.Payload` before they reach a mode, so a malformed message gets an error
reply and leaves the connection open rather than reaching the reply logic. A change to how the assistant replies stays inside
one folder rather than touching four.

The layer-first alternative is common in tutorials, and it is the one that ages
badly: adding a feature means editing `api/`, `schemas/`, `services/`, and
`models/` in parallel. Grouping by feature is also what Django does with apps,
which is why [lemon](../lemon/README.md) is laid out as `api/` and `lemon/`.

Two modules stay at the package root because they belong to no single feature:
`main.py` builds the application, and `settings.py` holds configuration.
`pages.py` is a single HTML route and does not need a folder of its own.

### Why the package is `app`, not `chatbot`

The Python package deliberately does not repeat the project name. `chatbot/src/`
holds one package, so naming it `chatbot` too would give every path a doubled
`chatbot/.../chatbot/...` — the layout `django-admin startproject` produces and
the one people most often complain about, because no path tells you which of the
two you are looking at. The entry point is `main.py` for the same reason:
`app/app.py` would reintroduce the doubling one level down.

The package still exists rather than putting modules loose in `src/`. Without
it, `src/` goes on `sys.path` directly and `settings`, `pages`, and `chat`
become importable top-level names — generic enough to collide with an installed
package, and ambiguous to read (`from settings import settings`). `app.settings`
says where it comes from.

`src/` itself is kept for consistency with the sibling projects, where it earns
its place: lemon's holds three Django apps side by side. Here it holds one
package, and its only real job is keeping Python code separate from the
project's `Makefile`, `pyproject.toml`, and `.env`.

Dependencies and tooling configuration all live in `pyproject.toml`. The virtual
environment is created at `chatbot/.venv` and is isolated from the other PyCraft
applications.

## Sessions
<sub>[Back to top](#chatbot)</sub>

**One browser tab is one session.** Opening a tab starts a conversation with a
fresh UUID; closing or refreshing it ends the conversation and the history goes
with it. Two tabs are two independent chats even for the same user, and nothing
is persisted.

`client_id` and the session id answer different questions. `client_id` says who
the user is and repeats across their tabs; the session id identifies *this* tab
and is minted server-side, so the browser cannot pick it or reach another tab's
history by guessing.

That lifetime is why `conversations.py` has no registry. The conversation is
created by the socket handler and referenced only by it, so it is collected when
the handler returns — there is no map of live conversations that can drift out of
step with the map of live connections. Surviving a reload would need one.

Replies route by **session id, not `client_id`**: with a tab per session, "send
to this user" is ambiguous as soon as a second tab is open.

The history holds **the exchange with the model and nothing else**. Talking to
`help`, `echo`, or `type` mid-conversation leaves it untouched, so those replies
never end up in a request or get paid for as input tokens.

That is enforced by what each mode is handed, not by trusting it to behave: a
mode receives the conversation only if it sets `NEEDS_HISTORY`, and the rest are
called with the argument alone. `claude` is the only one that opts in, so no
other mode is in a position to record a turn even by mistake.

The history is kept in the shape the Messages API expects, so a turn can be sent
without translating it first. `claude` already records both sides of every turn —
that is what will be sent once the integration lands, and recording it now means
the session behaviour is real and tested before a network call exists.

Two limits worth stating plainly. History lives in the process, so **`uvicorn
--workers 2` breaks it**: a second worker has its own memory and knows nothing of
a session opened on the first. And nothing trims the history yet — every turn
resends all of it, so cost grows with conversation length.

## Modes
<sub>[Back to top](#chatbot)</sub>

The chat works in modes. A message is a mode name, then `:`, then whatever the
mode needs — `echo: Test`. A mode that needs no argument is written on its own,
like `help`. Mode names are case-insensitive, and only the first `:` splits, so
an argument may contain more.

| Mode | Example | What it does |
| --- | --- | --- |
| `help` | `help`, `help: echo` | Lists the modes, or explains one of them |
| `echo` | `echo: Test` | Replies `Hello from backend! Did you say 'Test'?` |
| `type` | `type: table` | Renders a content type, to show how the chat displays it |
| `claude` | `claude: Why is the sky blue?` | Scaffolding only — see below |

Anything that names no known mode gets a reply listing what is available.

Each mode is a module in `chat/modes/` exposing `NAME`, `SUMMARY`, `USAGE`, and
a `reply()` that turns the argument into a message. Adding one is a new module
plus a single entry in the `MODES` registry: `help` lists whatever is
registered, so it cannot fall out of date with the code.

Replies are built through `chat/messages.py`, which holds the render contract
the JavaScript understands. A mode never assembles that shape by hand, so
changing how a table is delivered is a change in one file.

**Claude mode is scaffolding, not an integration.** It is reachable, tested, and
listed by help, but makes no model call — `chat/modes/claude.py` documents what
wiring it up involves, in order. No API dependency is installed.

**The browser does not choose the mode.** It sends the raw text and the server
routes it. Until this change the JavaScript mapped text to one of two intents
and silently discarded everything else, which put a limit on what the chat could
answer inside the client.

## How the frontend loads
<sub>[Back to top](#chatbot)</sub>

`templates/index.html` loads scripts in three ordered groups, all as ordinary
`<script>` tags:

1. **Vendored libraries** from `static/vendor/`, loaded synchronously.
2. **An inline script that opens the WebSocket.** It runs before the component
   scripts because `chat.js` assigns `ws.onmessage` at the top level, so `ws`
   has to be a real object by then. Its values go through Jinja's `tojson`
   filter, which quotes and escapes them correctly.
3. **The application scripts, marked `defer`.** Deferred scripts run after the
   document is parsed and in document order — which matters because `chat.js`
   binds handlers to elements, `.userInput` among them, that appear further down
   the page.

None of this is dynamic, and that is deliberate. An earlier version injected the
component scripts at runtime through a hand-written `include()` helper, which
caused two problems worth not repeating:

- **Browsers do not reliably revalidate dynamically inserted scripts** on a hard
  reload, so a stale component could survive a cache clear. The symptom is
  miserable to diagnose: the page renders correctly and nothing responds to
  clicks, because the first script threw a `ReferenceError` before binding any
  handler, and nothing else reports an error.
- **Load order was decided by network timing.** Injected scripts ignore `defer`
  and behave as `async`, so the ordering held only because the chained requests
  happened to be slower than parsing the document.

For the same reason the server sends `Cache-Control: no-cache` on **every**
response, not only static files: the page and its scripts have to agree with
each other, so a fresh page against a cached script breaks exactly as badly as
the reverse. `no-cache` still permits caching — it only requires the ETag to be
checked first, so unchanged files come back as a cheap `304`. A deployment that
wants real caching should serve hashed filenames with a long `max-age` instead.

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
`.env.example` on first run. `src/app/settings.py` reads it through
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
`pyproject.toml`. `tests/test_app.py` covers the entry points — the rendered
page, socket round trips, and a malformed payload getting an error reply without
dropping the connection. `tests/test_modes.py` covers each mode directly, with
no socket involved, which is the point of keeping the reply logic out of the
router, plus session isolation: separate conversations never see each other's
history, and only `claude` records turns.

## Code style
<sub>[Back to top](#chatbot)</sub>

`ruff` handles both linting and formatting, configured in `pyproject.toml`:

```bash
make format
make lint
```
