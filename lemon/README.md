# Little Lemon Backend

Little Lemon is a Django and Django REST Framework application backed by MySQL.

## Project structure

```text
lemon/
├── compose.yaml
├── docker/
│   └── mysql/
│       └── init-test-permissions.sh
├── requirements.txt
├── run.sh
└── src/
    ├── manage.py
    ├── api/
    ├── config/
    └── lemon/
```

The Python virtual environment is created at `lemon/.venv` and is isolated
from the other PyCraft applications.

## Requirements

- Python 3.14
- Docker Desktop with Docker Compose
- Homebrew MySQL client libraries and `pkg-config` for building `mysqlclient`

Install the native build dependencies on macOS:

```bash
brew install mysql pkg-config
```

The Homebrew MySQL service does not need to run because MySQL runs in Docker.
If another MySQL server already occupies port 3306, stop it before launching:

```bash
brew services stop mysql
```

## Start the application

Start Docker Desktop, then run this command from the top-level `PyCraft`
directory:

```bash
./lemon/run.sh
```

The launcher:

1. Creates `lemon/.venv` with Python 3.14 if it does not exist.
2. Activates the virtual environment.
3. Installs the pinned Python dependencies.
4. Starts the MySQL 8.4 LTS container and waits for it to become healthy.
5. Applies Django database migrations.
6. Loads sample categories, cuisines, and meals when the meal table is empty.
7. Starts the Django development server.

Arguments are forwarded to Django's `runserver` command. For example:

```bash
./lemon/run.sh 0.0.0.0:8000
```

The default local database configuration is:

- Database: `lemon`
- User: `mysql_fid`
- Password: `mysql_fid`
- Host: `127.0.0.1:3306`

These local-development defaults can be overridden with `MYSQL_DATABASE`,
`MYSQL_USER`, `MYSQL_PASSWORD`, `MYSQL_ROOT_PASSWORD`, and `MYSQL_PORT`.

## Docker lifecycle

Inspect the database service:

```bash
docker compose -f lemon/compose.yaml ps
docker compose -f lemon/compose.yaml logs --follow mysql
```

Stop the database while preserving its data:

```bash
docker compose -f lemon/compose.yaml stop
```

Remove the container while preserving its named data volume:

```bash
docker compose -f lemon/compose.yaml down
```

To delete the local database data as well, explicitly remove the volume:

```bash
docker compose -f lemon/compose.yaml down --volumes
```

## Management commands

Activate Lemon's environment and enter the source directory:

```bash
source lemon/.venv/bin/activate
cd lemon/src
```

Load or restore the sample catalog manually:

```bash
python manage.py loaddata \
    api/fixtures/Category.json \
    api/fixtures/Cuisine.json \
    api/fixtures/Meal.json
```

The launcher runs this automatically only when the meal table is empty, so it
does not overwrite an existing catalog.

Run the tests:

```bash
python manage.py test
```

Create and apply migrations:

```bash
python manage.py makemigrations api lemon
python manage.py migrate
python manage.py showmigrations
```

Create an administrator account:

```bash
python manage.py createsuperuser
```

Open the configured database shell:

```bash
python manage.py dbshell
```

Create another Django application:

```bash
python manage.py startapp APP_NAME
```

## Debug toolbar

The Django debug toolbar is installed and configured for local requests from
`127.0.0.1`. When the server is running, open:

```text
http://127.0.0.1:8000/__debug__/
```
