"""Stand-ins for the pieces that would otherwise need a live transport or API.

The MCP client talks to the document server over a subprocess, so the tests
substitute it rather than spawning one.
"""

from mcp.types import CallToolResult, TextContent, Tool


def make_tool(name: str, description: str = "") -> Tool:
    return Tool(name=name, description=description, input_schema={"type": "object"})


def text_result(text: str, is_error: bool = False) -> CallToolResult:
    return CallToolResult(content=[TextContent(type="text", text=text)], is_error=is_error)


class FakeClient:
    """Implements the two MCPClient methods ToolManager actually calls."""

    def __init__(self, tools=(), result=None, raises=None):
        self._tools = list(tools)
        self._result = result
        self._raises = raises
        self.calls = []

    async def list_tools(self):
        return self._tools

    async def call_tool(self, tool_name, tool_input):
        self.calls.append((tool_name, tool_input))
        if self._raises is not None:
            raise self._raises
        return self._result


class ToolUse:
    """The shape ToolManager reads off an assistant message block."""

    def __init__(self, id, name, input):
        self.type = "tool_use"
        self.id = id
        self.name = name
        self.input = input


class TextBlockStub:
    def __init__(self, text):
        self.type = "text"
        self.text = text


class MessageStub:
    def __init__(self, content):
        self.content = content
