# Little Lemon Backend
<sub>[Back to PyCraft](../README.md#pycraft)</sub>

Little Lemon is a Django and Django REST Framework application backed by MySQL.

## Contents
1. [Project structure](#project-structure)
2. [Requirements](#requirements)
3. [Configuration](#configuration)
4. [Start the application](#start-the-application)
5. [Everyday commands](#everyday-commands)
6. [Tests](#tests)
7. [Code style](#code-style)
8. [Docker lifecycle](#docker-lifecycle)
9. [Debug toolbar](#debug-toolbar)

## Project structure
<sub>[Back to top](#little-lemon-backend)</sub>

```text
lemon/
├── src/
│   ├── api/
│   ├── config/
│   │   ├── settings/
│   │   │   ├── base.py
│   │   │   ├── local.py
│   │   │   └── test.py
│   │   └── urls.py
│   ├── lemon/
│   └── manage.py
├── .env.example
├── compose.yaml
├── Makefile
├── pyproject.toml
├── README.md
├── run.sh
└── uv.lock
```

Dependencies, tooling configuration, and test settings all live in
`pyproject.toml`. The virtual environment is created at `lemon/.venv` and is
isolated from the other PyCraft applications.

## Requirements
<sub>[Back to top](#little-lemon-backend)</sub>

- [uv](https://docs.astral.sh/uv/) — manages the Python version, the virtual
  environment, and dependencies
- Docker Desktop with Docker Compose
- Homebrew MySQL client libraries and `pkg-config` for building `mysqlclient`

```bash
brew install uv mysql pkg-config
```

uv downloads Python 3.14 itself if the machine does not already have it, so no
interpreter needs to be installed separately.

The Homebrew MySQL service does not need to run because MySQL runs in Docker.
If another MySQL server already occupies port 3306, stop it before launching:

```bash
brew services stop mysql
```

## Configuration
<sub>[Back to top](#little-lemon-backend)</sub>

All configuration lives in a single `lemon/.env`, which `run.sh` creates from
`.env.example` on first run. Docker Compose reads it for `${VAR}` interpolation
in `compose.yaml`, and Django reads it through `django-environ`, so each value
is defined exactly once.

| Variable | Default | Purpose |
| --- | --- | --- |
| `DJANGO_SECRET_KEY` | insecure development key | Must be set to a real secret anywhere but a laptop |
| `DJANGO_DEBUG` | `True` | Enables the debug toolbar and detailed error pages |
| `DJANGO_ALLOWED_HOSTS` | `127.0.0.1,localhost` | Comma-separated host allowlist |
| `MYSQL_DATABASE` | `lemon` | Application database |
| `MYSQL_USER` | `mysql_fid` | Application database user |
| `MYSQL_PASSWORD` | `mysql_fid` | Application database password |
| `MYSQL_ROOT_PASSWORD` | `root` | Container superuser, also used by the test suite |
| `MYSQL_HOST` | `127.0.0.1` | Database host as seen from the application |
| `MYSQL_PORT` | `3306` | Published container port |

`.env` is git-ignored; `.env.example` is the committed template.

Settings are split by environment. `config.settings.base` holds everything
shared, `config.settings.local` is the default for `manage.py` and `run.sh`, and
`config.settings.test` is selected automatically by pytest.

## Start the application
<sub>[Back to top](#little-lemon-backend)</sub>

Start Docker Desktop, then run this command from the top-level `PyCraft`
directory:

```bash
./lemon/run.sh
```

The launcher:

1. Verifies that uv and Docker are available.
2. Creates `.env` from `.env.example` if it is missing.
3. Syncs `lemon/.venv` against `pyproject.toml`.
4. Starts the MySQL 8.4 LTS container and waits for it to become healthy.
5. Applies Django database migrations.
6. Loads sample categories, cuisines, and meals when the meal table is empty.
7. Starts the Django development server.

It deliberately does not run the tests; `make test` does that.

Arguments are forwarded to Django's `runserver` command. For example:

```bash
./lemon/run.sh 0.0.0.0:8000
```

## Everyday commands
<sub>[Back to top](#little-lemon-backend)</sub>

Run these from the `lemon` directory. `make` on its own lists them.

| Target | What it does |
| --- | --- |
| `make install` | Sync dependencies into `.venv` |
| `make run` | Start the development server |
| `make test` | Start MySQL if needed, then run the suite |
| `make coverage` | Run the suite with a coverage report |
| `make lint` | Check formatting and lint rules |
| `make format` | Apply formatting and safe lint fixes |
| `make check` | `lint` plus `test` — everything CI would run |
| `make migrate` | Apply migrations |
| `make makemigrations` | Generate migrations for the `api` and `lemon` apps |
| `make superuser` | Create an administrator account |
| `make shell` | Open the Django shell |
| `make fixtures` | Load the sample catalog, overwriting existing rows |
| `make db-up` / `db-stop` | Start / stop MySQL, keeping its data |
| `make db-down` | Remove the container, keeping its data volume |
| `make db-reset` | Remove the container and delete its data volume |
| `make clean` | Delete caches and build artefacts |

Targets that take extra arguments accept them through `ARGS`:

```bash
make test ARGS="-k cart -vv"
make run ARGS="0.0.0.0:8000"
```

Anything without a target is one `uv run` away:

```bash
uv run python src/manage.py dbshell
uv run python src/manage.py startapp APP_NAME
```

## Tests
<sub>[Back to top](#little-lemon-backend)</sub>

```bash
make test
```

The suite runs on pytest through `pytest-django`; existing `django.test.TestCase`
classes work unchanged. Configuration lives under `[tool.pytest.ini_options]` in
`pyproject.toml`.

`--reuse-db` skips the create-and-migrate step when the schema has not changed:

```bash
make test ARGS="--reuse-db"
```

Test settings connect as the MySQL superuser rather than as `mysql_fid`. The
test runner creates and drops `test_lemon`, which the application user is not
granted, and granting it would mean provisioning database privileges purely to
support a test harness. Local and CI databases are disposable, so the simpler
arrangement is to let tests use the superuser and leave the application user
scoped to the application database.

Test settings also swap in a fast password hasher and disable DRF throttling,
whose counters live in the cache and would otherwise make results depend on
execution order.

## Code style
<sub>[Back to top](#little-lemon-backend)</sub>

`ruff` handles both linting and formatting, configured in `pyproject.toml`:

```bash
make format
make lint
```

## Docker lifecycle
<sub>[Back to top](#little-lemon-backend)</sub>

The `make db-*` targets above cover the common cases. The underlying commands,
if you want them directly:

```bash
docker compose -f lemon/compose.yaml ps
docker compose -f lemon/compose.yaml logs --follow mysql
```

## Debug toolbar
<sub>[Back to top](#little-lemon-backend)</sub>

`django-debug-toolbar` is a development-only dependency, installed and wired up
only by the local settings. When the server is running, open:

```text
http://127.0.0.1:8000/__debug__/
```
