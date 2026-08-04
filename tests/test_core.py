from types import SimpleNamespace

import pandas as pd
import pytest
import requests

from src.backtest import BacktestEngine
from src.config import Settings
from src.data_client import DataClient, MarketDataError, validate_symbol
from src.llm_agent import SYSTEM_PROMPT, LLMAgent


class Response:
    def __init__(self, payload, error=False):
        self.payload, self.error = payload, error

    def raise_for_status(self):
        if self.error:
            raise requests.HTTPError("bad status")

    def json(self):
        return self.payload


class Session:
    def __init__(self, response):
        self.response = response
        self.calls = []

    def get(self, url, **kwargs):
        self.calls.append((url, kwargs))
        return self.response


def test_settings_are_lazy_and_validated(monkeypatch):
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    with pytest.raises(RuntimeError, match="OPENAI_API_KEY"):
        Settings.from_env(require_openai=True)
    monkeypatch.setenv("OPENAI_API_KEY", "secret")
    monkeypatch.setenv("REQUEST_TIMEOUT_SECONDS", "61")
    with pytest.raises(ValueError, match="at most 60"):
        Settings.from_env()
    monkeypatch.setenv("REQUEST_TIMEOUT_SECONDS", "5")
    monkeypatch.setenv("OPENAI_API_BASE", "http://unsafe.example")
    with pytest.raises(ValueError, match="HTTPS"):
        Settings.from_env()


@pytest.mark.parametrize("raw,expected", [("aapl", "AAPL"), ("brk.b", "BRK.B")])
def test_symbol_normalization(raw, expected):
    assert validate_symbol(raw) == expected


@pytest.mark.parametrize("raw", ["", "../../etc", "AAPL&x=1", "WAYTOOLONG11"])
def test_symbol_rejects_untrusted_input(raw):
    with pytest.raises(ValueError):
        validate_symbol(raw)


def client_for(payload):
    return DataClient(
        base_url="https://example.com/query",
        api_key="key",
        timeout=3,
        session=Session(Response(payload)),
    )


def test_data_client_contract_and_timeout():
    payload = {"Time Series (Daily)": {"2026-01-01": {"4. close": "10"}}}
    client = client_for(payload)
    assert client.get_daily_time_series("aapl") == payload
    _, call = client.session.calls[0]
    assert call["timeout"] == 3
    assert call["params"]["symbol"] == "AAPL"


@pytest.mark.parametrize("payload", [{}, [], {"Note": "rate limited"}])
def test_data_client_rejects_bad_provider_payload(payload):
    with pytest.raises(MarketDataError):
        client_for(payload).get_daily_time_series("AAPL")


def test_data_client_validates_enums():
    client = client_for({})
    with pytest.raises(ValueError):
        client.get_intraday("AAPL", interval="2min")
    with pytest.raises(ValueError):
        client.get_daily_time_series("AAPL", outputsize="huge")


def prices():
    return pd.DataFrame(
        {"close": [100.0, 110.0, 90.0]}, index=pd.date_range("2026-01-01", periods=3)
    )


def test_backtest_return_and_drawdown():
    engine = BacktestEngine(prices(), lambda frame: pd.Series(1, index=frame.index), 1000)
    curve = engine.run()
    assert curve.iloc[-1]["total"] == 990
    assert engine.stats()["total_return"] == pytest.approx(-0.01)
    assert engine.stats()["max_drawdown"] < 0


def test_backtest_rejects_invalid_inputs_and_signals():
    with pytest.raises(ValueError):
        BacktestEngine(pd.DataFrame(), lambda frame: pd.Series(dtype=int))
    engine = BacktestEngine(prices(), lambda frame: pd.Series([2, 2, 2], index=frame.index))
    with pytest.raises(ValueError, match="positions"):
        engine.run()
    with pytest.raises(RuntimeError):
        engine.stats()


def test_backtest_rejects_non_finite_prices():
    non_finite = prices()
    non_finite.iloc[1, 0] = float("inf")
    with pytest.raises(ValueError, match="finite positive"):
        BacktestEngine(non_finite, lambda frame: pd.Series(1, index=frame.index))


class CompletionClient:
    def __init__(self, content="analysis"):
        self.kwargs = None
        self.content = content
        self.chat = SimpleNamespace(completions=self)

    def create(self, **kwargs):
        self.kwargs = kwargs
        message = SimpleNamespace(content=self.content)
        return SimpleNamespace(choices=[SimpleNamespace(message=message)])


def test_llm_agent_applies_financial_safety_boundary():
    client = CompletionClient()
    assert LLMAgent(client=client).ask("Analyze AAPL") == "analysis"
    assert client.kwargs["messages"][0] == {"role": "system", "content": SYSTEM_PROMPT}
    assert "not investment advice" in SYSTEM_PROMPT


@pytest.mark.parametrize("prompt", ["", "x" * 20_001])
def test_llm_agent_rejects_invalid_prompt(prompt):
    with pytest.raises(ValueError):
        LLMAgent(client=CompletionClient()).ask(prompt)


def test_llm_agent_rejects_empty_response():
    with pytest.raises(RuntimeError):
        LLMAgent(client=CompletionClient(" ")).ask("hello")
