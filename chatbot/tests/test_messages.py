"""The render contract the JavaScript understands."""

from app.chat import messages


def test_text_message():
    assert messages.text("hello") == {"template_type": "text", "text": "hello"}


def test_table_message_carries_its_rows():
    reply = messages.table("caption", [{"a": 1}])

    assert reply["template_type"] == messages.TABLE
    assert reply["text"] == "caption"
    assert reply["msg_payload"] == [{"a": 1}]
    assert reply["clickable"] == "false"


def test_choices_message_pairs_labels_with_commands():
    reply = messages.choices("pick one", "Types", [("Table", "type: table")])

    assert reply["template_type"] == messages.CHOICES
    assert reply["label"] == "Types"
    assert reply["msg_payload"] == [{"label": "Table", "command": "type: table"}]
