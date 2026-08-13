# AGENTS.md

PyCraft is a collection of independent Python applications: `chatbot`, `lemon`,
and `mathparser`. Each owns its virtual environment, dependencies, and
`README.md`. Nothing is shared between them, so changes to one project should
not require touching another.

Per-project setup and commands live in that project's `README.md`.

## Project conventions

All three projects share the same shape. A fourth should follow it rather than
invent its own.

- **Follow established Python industry practices.** Validate every decision
  presented as a standard practice against current authoritative sources: the
  Python documentation and PEPs, PyPA specifications and guides, or the
  relevant tool or framework's official documentation. Also verify that the
  choice fits this repository's existing conventions and validate the result
  with the applicable tests, linting, type checks, or runtime checks. When
  authoritative guidance differs or a project constraint justifies a
  deviation, document the tradeoff instead of claiming one approach is
  universally standard.
- **[uv](https://docs.astral.sh/uv/) manages everything.** Dependencies,
  tooling configuration, and the virtual environment come from the project's
  `pyproject.toml`; `uv.lock` is committed. There is no `requirements.txt`, and
  nothing creates or activates a virtual environment by hand.
- **Runtime dependencies go in `[project]`, everything else in
  `[dependency-groups]`** as `test` and `dev`, so CI can install `--group test`
  without pulling in linters.
- **`make` is the task runner.** Every project answers to the same verbs:
  `install`, `run`, `test`, `coverage`, `lint`, `format`, `check`, and `clean`.
  Lemon adds database and Django targets on top. The repository root has a
  `Makefile` that runs any shared target across all three.
- **`run.sh` starts the application from scratch and never runs tests.** It
  checks its prerequisites, creates `.env` from `.env.example` when missing,
  syncs dependencies, and execs the server. Testing is `make test` — a launcher
  that doubles as a test runner is the pattern this repository moved away from.
- **Configuration is a single `.env` per project**, git-ignored, with a
  committed `.env.example` template. Nothing sources shell profile scripts.
- **`ruff` handles both linting and formatting**, configured in `pyproject.toml`.
- **Tests run on pytest**, even where the test classes are `unittest.TestCase`.

## Documentation conventions

### Navigation links

READMEs link in both directions, matching the sibling JavaCraft repository.

- The root `README.md` lists every project and links to its `README.md`.
- Each project `README.md` carries a back link on the line directly below its
  H1: `<sub>[Back to PyCraft](../README.md#pycraft)</sub>`.
- Each project `README.md` then opens with a `## Contents` section: a numbered
  list linking to its own `##` sections.
- Every `##` section except `Contents` is followed on the next line by
  `<sub>[Back to top](#<h1-anchor>)</sub>`.

Anchors are GitHub heading slugs: lowercased, punctuation stripped, spaces
turned into hyphens. `# Little Lemon Backend` becomes `#little-lemon-backend`.

### Project structure trees

Every project `README.md` carries a `## Project structure` section with a tree
of its layout. Order entries the way the Visual Studio Code explorer displays a
directory:

1. **Folders first**, sorted by name.
2. **Then files**, sorted by name.

Apply the rule at every level of nesting. Folder names take a trailing slash so
they stay distinguishable from extensionless files.

```text
lemon/
├── src/
│   ├── api/
│   ├── config/
│   │   ├── settings/
│   │   └── urls.py
│   ├── lemon/
│   └── manage.py
├── .env.example
├── compose.yaml
├── Makefile
├── pyproject.toml
└── run.sh
```

Two details that follow VS Code rather than plain ASCII sorting:

- Sorting is **case-insensitive**, so `compose.yaml` precedes `Makefile`, which
  precedes `pyproject.toml`.
- **Dotfiles sort before** everything else in their group, so `.env.example`
  heads the file list.

Trees are curated, not generated: they show the folders and files that explain
the project, and omit build artefacts and tool directories such as `.venv`,
`.vscode`, and `__pycache__`.
