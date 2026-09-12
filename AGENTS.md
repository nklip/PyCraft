# AGENTS.md

PyCraft is a collection of independent Python applications: `chatbot`, `lemon`,
`mathparser`, and `mcp`. Each owns its virtual environment, dependencies, and
`README.md`. Nothing is shared between them, so changes to one project should
not require touching another.

`notebooks` sits alongside them but is not one of them: it holds Jupyter
notebooks, not an application, and none of the conventions below apply to it.

Per-project setup and commands live in that project's `README.md`.

## Project conventions

All four projects share the same shape. A fifth should follow it rather than
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
  `[dependency-groups]`** as `test` and `dev`, keeping what ships apart from
  what only builds it. The split marks that boundary; it does not narrow any
  install, since `make check` lints as well as tests and uv syncs the `dev`
  group that `test` is included in.
- **`make` is the task runner.** Every project answers to the same verbs:
  `install`, `run`, `test`, `coverage`, `lint`, `format`, `check`, and `clean`.
  Lemon adds database and Django targets on top. The repository root has a
  `Makefile` that runs any shared target across all four, and its `PROJECTS`
  variable is the single list of them — CI reads it rather than keeping a copy.
- **`run.sh` starts the application from scratch and never runs tests.** It
  checks its prerequisites, creates `.env` from `.env.example` when missing,
  syncs dependencies, and execs the server. Testing is `make test` — a launcher
  that doubles as a test runner is the pattern this repository moved away from.
- **Configuration is a single `.env` per project**, git-ignored, with a
  committed `.env.example` template. Nothing sources shell profile scripts.
  A project that needs no configuration has neither file.
- **`ruff` handles both linting and formatting**, configured in `pyproject.toml`.
- **Tests run on pytest**, even where the test classes are `unittest.TestCase`.
- **A bug fix arrives with a test that fails without it.** Reintroduce the
  bug once and watch the new test go red; a test written after the fix and
  never seen failing proves nothing about the bug.
- **CI runs `make check`, and nothing else.** `.github/workflows/ci.yml` gives
  each project a job that checks out, installs uv, and runs that one target, so
  CI exercises the same path a developer does instead of reimplementing it. A
  project needing a service brings it up from its own `compose.yaml` inside
  `make test`; GitHub's Linux runners ship the Docker engine and compose, so no
  CI-specific variant is needed.
- **Actions are pinned to a ref that resolves.** Not every action publishes a
  moving major tag, so a plausible-looking major can be a 404 that fails every
  job during setup, before a line of the project runs. Resolve the ref against
  the tags API before committing it.
- **Dependabot opens the upgrade pull requests**, configured in
  `.github/dependabot.yml` against every project's `uv.lock`. Minor and patch
  bumps are grouped per project; majors arrive on their own. A pull request cut
  before a workflow fix carries the broken workflow with it, so a red
  Dependabot check is worth reading before it is worth debugging.

## Dependency conventions

`uv.lock` is the reproducible truth, which leaves the `>=` floors in
`pyproject.toml` as documentation: they say what the project claims to support.
Keep them honest.

- **A floor must be a version the code can actually run on.** Verify it against
  that release rather than inheriting whatever scaffolding wrote, and remember
  that a lock resolving well above a floor hides a floor that would not even
  import. A floor nothing ever resolves against is a comment, not a constraint.
- **Floors match the locked version**, runtime dependencies and tooling alike.
  Tooling is not exempt: the linter and formatter decide what `make lint` means,
  so a floor far below the lock invites a fresh resolve onto a release that
  disagrees with the committed sources, failing for a reason no source change
  explains.
- **Declare every package the code imports.** Arriving through another
  dependency is not declaring, and holds only until that dependency drops it or
  changes what it requires.
- **An upgrade is the lock and the floors together**, done per project and
  verified with that project's `make check`.
- **A dependency the tests never exercise needs a check of its own.** A green
  suite says nothing about a development-only integration; run whatever actually
  loads it.

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
