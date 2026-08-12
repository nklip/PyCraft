# Chatbot

## Project structure

```text
chatbot/
├── profile/
├── src/
│   ├── static/
│   ├── templates/
│   ├── connection_manager.py
│   ├── main.py
│   └── models.py
├── requirements.txt
└── run.sh
```

The Python virtual environment is created at `chatbot/.venv` and is isolated
from the other PyCraft applications.

## Requirements

- Python 3.14

## Start the application

Run this command from the top-level `PyCraft` directory:

```bash
./chatbot/run.sh
```

The launcher:

1. Creates `chatbot/.venv` with Python 3.14 if it does not exist.
2. Activates the virtual environment.
3. Installs the pinned dependencies from `chatbot/requirements.txt`.
4. Loads variables from `chatbot/profile/chatbot.local.profile`.
5. Starts the Uvicorn development server.

Arguments are forwarded to Uvicorn. For example:

```bash
./chatbot/run.sh --reload
```

## Manual commands

Activate Chatbot's environment:

```bash
source chatbot/.venv/bin/activate
```

Install dependencies:

```bash
python -m pip install -r chatbot/requirements.txt
```

Start the server manually:

```bash
set -a
source chatbot/profile/chatbot.local.profile
set +a
cd chatbot/src
python -m uvicorn main:server
```
