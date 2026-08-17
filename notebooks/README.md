# Notebooks
<sub>[Back to PyCraft](../README.md#pycraft)</sub>

Jupyter notebooks for trying the Anthropic API by hand.

This folder is not an application. A notebook is a scratchpad: it is here to
be run a cell at a time and edited while it runs.

## Contents
1. [Project structure](#project-structure)
2. [Requirements](#requirements)
3. [Start Jupyter](#start-jupyter)
4. [Open a notebook](#open-a-notebook)
5. [Add a library](#add-a-library)
6. [Configuration](#configuration)
7. [Why this folder is not a uv project](#why-this-folder-is-not-a-uv-project)

## Project structure
<sub>[Back to top](#notebooks)</sub>

```text
notebooks/
├── tools_usage/
└── README.md
```

Notebooks live in subject folders, numbered so they read in the order they were
written. `tools_usage` covers Anthropic tool use — tool schemas, fine-grained
streaming, the text editor tool, web search — the same tool-calling ideas the
chatbot's [claude mode](../chatbot/README.md#modes) does not use yet.

**The notebooks themselves are deliberately not listed here.** They are added,
renamed, and split as subjects are worked through, and a file list would be
wrong within a week. Open the folder to see what is in it; this file explains
how to run whatever you find there.

`.env` sits at the top of this folder rather than beside the notebooks, so one
key serves every subfolder. That works because of how the key is looked up —
see [Configuration](#configuration).

Running a notebook leaves artefacts beside it — `.ipynb_checkpoints/` from
Jupyter, and `.backups/` from the text editor tool, which copies a file before
editing it. Both are git-ignored, as is `.env`, and none of them belong in the
tree above.

## Requirements
<sub>[Back to top](#notebooks)</sub>

- [uv](https://docs.astral.sh/uv/) — the only thing to install

```bash
brew install uv
```

uv downloads Python itself, and Jupyter with it, so nothing else needs to be
installed first.

## Start Jupyter
<sub>[Back to top](#notebooks)</sub>

Run this from the `notebooks` folder:

```bash
uv run \
  --with jupyter \
  --with anthropic \
  --with python-dotenv \
  jupyter lab
```

**There is no separate install step.** `uv run --with` builds a throwaway
environment containing what the flags name, then runs the command inside it.
The first run downloads Jupyter and the libraries — around twenty seconds — and
every later run reuses uv's cache and starts immediately.

Each `--with` is one library the notebooks need:

| Flag | Why |
| --- | --- |
| `--with jupyter` | JupyterLab itself, and the kernel that runs the cells |
| `--with anthropic` | The Anthropic SDK, imported by every notebook |
| `--with python-dotenv` | Reads `.env`, so the API key never sits in a cell |

JupyterLab prints a `http://localhost:8888/lab?token=...` URL and opens it in a
browser. Stop the server with `Ctrl-C` in that terminal, twice — the second one
skips the confirmation prompt and shuts the kernels down with it.

**An already-installed Jupyter is the one thing to watch for.** If `jupyter lab`
is on the path — from Homebrew, or from a system `pip install` — typing it
bare will start a server that works, right up to the point where a cell says
`ModuleNotFoundError: No module named 'anthropic'`. Its kernel is that
installation's environment, which knows nothing about the libraries the
notebooks need. Starting through `uv run --with` is what ties the two together,
so use the full command rather than the short one.

The [official Jupyter instructions](https://jupyter.org/install) are
`pip install jupyterlab` instead. Both work, and the difference is deliberate:
this repository has uv manage every environment, and `pip install` would put
Jupyter either in a hand-made virtual environment or in the system Python. The
uv form is also what [uv's own Jupyter guide](https://docs.astral.sh/uv/guides/integration/jupyter/)
recommends. The tradeoff is that the versions are not pinned here — see
[below](#why-this-folder-is-not-a-uv-project).

## Open a notebook
<sub>[Back to top](#notebooks)</sub>

JupyterLab serves the folder it was started in, so the file browser on the left
lists what is beside it — here, the `tools_usage` folder. **Double-click the
folder, then the notebook, to load it.**

To skip that, name the file when starting:

```bash
uv run \
  --with jupyter \
  --with anthropic \
  --with python-dotenv \
  jupyter lab tools_usage/<notebook>.ipynb
```

The browser then opens on `/lab/tree/<notebook>.ipynb` with that notebook loaded
rather than on the launcher.

Note what that path is missing: naming a file inside a subfolder makes **that
subfolder the server root**, so JupyterLab serves `tools_usage/` and the URL is
relative to it. The file browser is then scoped to that folder and cannot
navigate up to `notebooks/`. The key still loads, because `load_dotenv()`
searches the filesystem rather than Jupyter's tree — but if you want to move
between subject folders in one session, start from `notebooks/` without naming
a file.

Once it is open:

- The kernel is **Python 3 (ipykernel)**, shown top right. It is the throwaway
  environment from the `uv run` command, which is what makes the `--with`
  libraries importable.
- `Shift-Enter` runs the focused cell and moves to the next one. **Run ▸ Run All
  Cells** runs the notebook top to bottom.
- Cells share one interpreter, so a name defined in the first cell is still
  there in the last. **Kernel ▸ Restart Kernel** throws that state away, which
  is the fix for a notebook that only works in the order you happened to click.

A notebook opened from a different folder still works — Jupyter can open any
path under the directory it was started in, but not above it.

## Add a library
<sub>[Back to top](#notebooks)</sub>

**Add one more `--with` line to the launch command.** For pandas:

```bash
uv run \
  --with jupyter \
  --with anthropic \
  --with python-dotenv \
  --with pandas \
  jupyter lab
```

This is the form worth keeping: the command names everything the notebooks need,
so it reproduces the same environment on another machine, and restarting the
kernel does not lose the library.

A cell can install one too, using the `%pip` magic — `%`, not `!`, so it
installs into the kernel that is running rather than into whatever `pip` happens
to be first on the path:

```python
%pip install pandas
```

That works immediately, but it lands in the throwaway environment under
`~/.cache/uv`, so it is gone the next time Jupyter starts. Treat it as a way to
try something, and move it into a `--with` once it turns out to be needed.

## Configuration
<sub>[Back to top](#notebooks)</sub>

Each notebook calls `load_dotenv()` and then builds an `Anthropic()` client,
which reads `ANTHROPIC_API_KEY` from the environment. That key is the one thing
this folder needs configured, and it lives in `notebooks/.env`:

```bash
ANTHROPIC_API_KEY=sk-ant-...
```

**The key sits a directory above the notebooks, and that is deliberate.**
`load_dotenv()` searches from the notebook's own folder *upwards* until it finds
a `.env`, so a notebook in `tools_usage/` walks up one level and finds
`notebooks/.env`. One key therefore serves every subfolder, and a new subject
folder needs no `.env` of its own. `.env` is git-ignored for the whole
repository, so the key cannot be committed from here by accident.

Two consequences of that search worth knowing:

- **The nearest file wins, and only that one is read.** Dropping a `.env` into
  `tools_usage/` would shadow `notebooks/.env` entirely rather than adding to it,
  so any variable defined only in the outer file would quietly stop loading.
- **The search does not stop at this repository.** It runs to the filesystem
  root, so a forgotten `.env` in a parent directory can supply a key. Print
  `find_dotenv()` when a value is not what you expect — it names the file that
  actually won.

Nothing else in `.env` is read by a notebook. Each one sets its own model in a
cell — `model = "..."` near the top — so a `CLAUDE_MODEL` copied over from the
chatbot's `.env` sits there unused rather than taking effect. Change the model
for a notebook in that cell, not here.

**A missing key does not fail where you would expect.** `Anthropic()` is built
with `api_key=None` without complaining, and every cell that only defines
functions or schemas runs fine; the error appears at the first
`client.messages.create(...)`. A notebook that runs eight cells and then fails
on the ninth is usually this.

The same key runs the [chatbot](../chatbot/README.md#configuration), which keeps
its own `.env` — the two are separate files on purpose, because each project
owns its configuration.

## Why this folder is not a uv project
<sub>[Back to top](#notebooks)</sub>

The three applications each own a `pyproject.toml` and a committed `uv.lock`.
This folder owns neither, and the `--with` flags stand in for both.

That is a real tradeoff, not an oversight. What is given up is pinning: `--with
anthropic` resolves to whatever is current on the day it runs, so a notebook
re-run in six months may not get the versions it was written against. What is
gained is that a scratchpad stays a scratchpad — no lock file to update, no
environment to sync, and one command that works on a fresh clone.

If the notebooks ever need pinned versions, the repository already has the shape
to copy: a `pyproject.toml` here, `uv add anthropic python-dotenv`, a committed
`uv.lock`, and a kernel registered against the project environment, which is
what [uv's guide](https://docs.astral.sh/uv/guides/integration/jupyter/)
describes. `!uv add` from inside a cell only works once that file exists.
