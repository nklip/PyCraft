# Mathparser

Mathparser is an interactive top-down mathematical expression parser.

## Project structure

```text
mathparser/
├── src/
│   ├── calculator/
│   └── main.py
├── tests/
├── README.md
└── run.sh
```

The Python virtual environment is created at `mathparser/.venv` and is
isolated from the other PyCraft applications. Mathparser uses only the Python
standard library, so it has no `requirements.txt` file.

## Start the application

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

## Run the tests

Use the launcher to create the environment and run all tests:

```bash
./mathparser/run.sh --test
```

To run them manually:

```bash
source mathparser/.venv/bin/activate
PYTHONPATH=mathparser/src python -m unittest discover \
    --start-directory mathparser/tests \
    --verbose
```
