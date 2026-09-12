import json

import pytest
from helpers import FakeClient, MessageStub, TextBlockStub, ToolUse, make_tool, text_result

from core.tools import ToolManager


async def test_get_all_tools_aggregates_every_client():
    clients = {
        "a": FakeClient(tools=[make_tool("read", "Read a doc")]),
        "b": FakeClient(tools=[make_tool("write"), make_tool("list")]),
    }

    tools = await ToolManager.get_all_tools(clients)

    assert [t["name"] for t in tools] == ["read", "write", "list"]
    assert tools[0]["description"] == "Read a doc"
    assert tools[0]["input_schema"] == {"type": "object"}


async def test_execute_tool_requests_returns_tool_output():
    client = FakeClient(tools=[make_tool("read")], result=text_result("contents"))

    blocks = await ToolManager.execute_tool_requests(
        {"a": client},
        MessageStub([TextBlockStub("thinking"), ToolUse("call-1", "read", {"path": "x"})]),
    )

    assert client.calls == [("read", {"path": "x"})]
    assert blocks == [
        {
            "tool_use_id": "call-1",
            "type": "tool_result",
            "content": json.dumps(["contents"]),
            "is_error": False,
        }
    ]


async def test_execute_tool_requests_marks_a_failed_call_as_an_error():
    client = FakeClient(tools=[make_tool("read")], result=text_result("nope", is_error=True))

    blocks = await ToolManager.execute_tool_requests(
        {"a": client}, MessageStub([ToolUse("call-1", "read", {})])
    )

    assert blocks[0]["is_error"] is True


async def test_execute_tool_requests_reports_an_unknown_tool():
    client = FakeClient(tools=[make_tool("read")])

    blocks = await ToolManager.execute_tool_requests(
        {"a": client}, MessageStub([ToolUse("call-1", "absent", {})])
    )

    assert blocks == [
        {
            "tool_use_id": "call-1",
            "type": "tool_result",
            "content": "Could not find that tool",
            "is_error": True,
        }
    ]


async def test_a_raising_tool_is_reported_rather_than_crashing_the_turn():
    """The error branch used to read tool_output, which the raise left unbound.
    The UnboundLocalError replaced the tool error and ended the conversation."""
    client = FakeClient(tools=[make_tool("read")], raises=RuntimeError("transport gone"))

    blocks = await ToolManager.execute_tool_requests(
        {"a": client}, MessageStub([ToolUse("call-1", "read", {})])
    )

    assert blocks[0]["is_error"] is True
    assert "transport gone" in json.loads(blocks[0]["content"])["error"]


async def test_every_tool_request_in_one_message_is_answered():
    client = FakeClient(tools=[make_tool("read"), make_tool("write")], result=text_result("done"))

    blocks = await ToolManager.execute_tool_requests(
        {"a": client},
        MessageStub([ToolUse("c1", "read", {}), ToolUse("c2", "write", {})]),
    )

    assert [b["tool_use_id"] for b in blocks] == ["c1", "c2"]


@pytest.mark.parametrize(("status", "expected"), [("success", False), ("error", True)])
def test_build_tool_result_part_sets_the_error_flag(status, expected):
    part = ToolManager._build_tool_result_part("id", "body", status)

    assert part["is_error"] is expected
    assert part["type"] == "tool_result"
