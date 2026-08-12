# AGENTS.md

PyCraft is a collection of independent Python applications: `chatbot`, `lemon`,
and `mathparser`. Each owns its virtual environment, dependencies, and
`README.md`. Nothing is shared between them, so changes to one project should
not require touching another.

Per-project setup and commands live in that project's `README.md`.

## Documentation conventions

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
