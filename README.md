# PyCraft

My micro Python applications
* [chatbot](chatbot/README.md) - a ui for chatbot created using Python / JS
* [lemon](lemon/README.md) - Django project for Little Lemon backend
* [mathparser](mathparser/README.md) - Complex Math parser working from console
* [mcp](mcp/README.md) - Simple MCP server and client

Not an application, but kept here too:
* [notebooks](notebooks/README.md) - Jupyter notebooks for playing with the Anthropic API

## Checking every project
<sub>[Back to top](#pycraft)</sub>

The root `Makefile` runs a target across all three projects, stopping at the
first failure:

```bash
make check
```

`make` on its own lists the shared targets. To work on one project, use `-C`:

```bash
make -C lemon test
```
