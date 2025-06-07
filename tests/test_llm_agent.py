import pytest
import openai
from src.llm_agent import LLMAgent

class DummyChoice:
    def __init__(self, content):
        self.message = DummyMessage(content)

class DummyMessage:
    def __init__(self, content):
        self.content = content

class DummyResponse:
    def __init__(self, content):
        self.choices = [DummyChoice(content)]

@pytest.fixture(autouse=True)
def env_vars(monkeypatch):
    # Ensure Config.validate() passes for OPENAI_API_KEY
    monkeypatch.setenv("OPENAI_API_KEY", "testkey")
    monkeypatch.setenv("OPENAI_API_BASE", "https://api.openai.com/v1")

def test_ask_invokes_openai(monkeypatch):
    prompt = "Hello, world!"
    expected = "Response text"

    def mock_create(**kwargs):
        assert kwargs["model"] == "gpt-4o-mini"
        assert kwargs["messages"] == [{"role": "user", "content": prompt}]
        return DummyResponse(expected)

    monkeypatch.setattr(openai.ChatCompletion, "create", mock_create)
    agent = LLMAgent()
    result = agent.ask(prompt, temperature=0.5, max_tokens=128)
    assert result == expected

def test_custom_model(monkeypatch):
    prompt = "Test prompt"
    expected = "OK"

    def mock_create(**kwargs):
        assert kwargs["model"] == "my-model"
        return DummyResponse(expected)

    monkeypatch.setenv("OPENAI_API_KEY", "testkey")
    monkeypatch.setenv("OPENAI_API_BASE", "https://api.openai.com/v1")
    monkeypatch.setattr(openai.ChatCompletion, "create", mock_create)
    agent = LLMAgent(model="my-model")
    result = agent.ask(prompt)
    assert result == expected

git add tests/test_llm_agent.py
git commit -m "Add pytest suite for LLMAgent"
