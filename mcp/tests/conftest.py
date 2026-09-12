import pytest


@pytest.fixture(autouse=True)
def anthropic_key(monkeypatch):
    """Anthropic() reads the key at construction and raises without one."""
    monkeypatch.setenv("ANTHROPIC_API_KEY", "sk-ant-test-not-a-real-key")
