# MCP Chat
<sub>[Back to PyCraft](../README.md#pycraft)</sub>

MCP Chat is a command-line interface application that enables interactive chat capabilities with AI models through the Anthropic API. The application supports document retrieval, command-based prompts, and extensible tool integrations via the MCP (Model Context Protocol) architecture.

## Contents
1. [Prerequisites](#prerequisites)
2. [Setup](#setup)
3. [Usage](#usage)

## Prerequisites
<sub>[Back to top](#mcp-chat)</sub>

- Python 3.14+ (uv downloads it for you)
- Anthropic API Key

## Setup
<sub>[Back to top](#mcp-chat)</sub>

### Step 1: Configure the environment variables

1. Create or edit the `.env` file in the project root and verify that the following variables are set correctly:

```
CLAUDE_MODEL="claude-sonnet-5"  # Model the chat talks to
ANTHROPIC_API_KEY=""             # Enter your Anthropic API secret key
USE_UV=1                         # 1 if running through uv, 0 if not
```

`main.py` asserts that `CLAUDE_MODEL` and `ANTHROPIC_API_KEY` are both
non-empty, so it exits immediately rather than failing on the first request.

### Step 2: Install dependencies

[uv](https://github.com/astral-sh/uv) is a fast Python package installer and resolver.

1. Install uv, if not already installed:

```bash
brew install uv
```

2. Run the project — uv creates the environment and installs `uv.lock` on the
   way, so there is no venv to make or activate by hand:

```bash
uv run main.py
```

To install the dependencies without starting the app, use `uv sync`.

### Step 3: MCP Inspector

Run command with extra dependency - pydantic
```bash
uv run mcp dev mcp_server.py --with pydantic
```

## Usage
<sub>[Back to top](#mcp-chat)</sub>

### Basic Interaction

Simply type your message and press Enter to chat with the model.

### Document Retrieval

Use the @ symbol followed by a document ID to include document content in your query:

```
> Tell me about @deposition.md
```

### Commands

Use the / prefix to execute commands defined in the MCP server:

```
> /summarize deposition.md
```

Commands will auto-complete when you press Tab.
