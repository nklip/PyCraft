import asyncio
import os
import sys
from contextlib import AsyncExitStack
from pathlib import Path

from dotenv import load_dotenv

from core.claude import Claude
from core.cli import CliApp
from core.cli_chat import CliChat
from mcp_client import MCPClient

# Configuration is a single .env in the project root, one directory above the
# sources, so it is found no matter where the process was started from.
PROJECT_DIR = Path(__file__).resolve().parents[1]
SERVER_SCRIPT = Path(__file__).with_name("mcp_server.py")

load_dotenv(PROJECT_DIR / ".env")

# Anthropic Config
claude_model = os.getenv("CLAUDE_MODEL", "")
anthropic_api_key = os.getenv("ANTHROPIC_API_KEY", "")


assert claude_model, "Error: CLAUDE_MODEL cannot be empty. Update .env"
assert anthropic_api_key, "Error: ANTHROPIC_API_KEY cannot be empty. Update .env"


async def main():
    claude_service = Claude(model=claude_model)

    server_scripts = sys.argv[1:]
    clients = {}

    async with AsyncExitStack() as stack:
        doc_client = await stack.enter_async_context(
            MCPClient(command="uv", args=["run", str(SERVER_SCRIPT)])
        )
        clients["doc_client"] = doc_client

        for i, server_script in enumerate(server_scripts):
            client_id = f"client_{i}_{server_script}"
            client = await stack.enter_async_context(
                MCPClient(command="uv", args=["run", server_script])
            )
            clients[client_id] = client

        chat = CliChat(
            doc_client=doc_client,
            clients=clients,
            claude_service=claude_service,
        )

        cli = CliApp(chat)
        await cli.initialize()
        await cli.run()


if __name__ == "__main__":
    if sys.platform == "win32":
        asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())
    asyncio.run(main())
