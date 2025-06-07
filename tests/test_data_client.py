import pytest
import requests
from src.data_client import DataClient

class DummyResponse:
    def __init__(self, json_data, status_code=200):
        self._json = json_data
        self.status_code = status_code

    def json(self):
        return self._json

    def raise_for_status(self):
        if self.status_code != 200:
            raise requests.HTTPError(f"Status code: {self.status_code}")

@pytest.fixture(autouse=True)
def env_vars(monkeypatch):
    # Ensure Config.validate() passes
    monkeypatch.setenv("DATA_API_KEY", "testkey")
    monkeypatch.setenv("DATA_API_BASE_URL", "https://example.com")

def test_get_daily_time_series(monkeypatch):
    expected = {"Time Series (Daily)": {"2025-06-07": {"4. close": "100.0"}}}

    def mock_get(url, params):
        assert url == "https://example.com"
        assert params["apikey"] == "testkey"
        assert params["symbol"] == "TEST"
        return DummyResponse(expected)

    monkeypatch.setattr("src.data_client.requests.get", mock_get)
    client = DataClient()
    result = client.get_daily_time_series("TEST")
    assert result == expected

def test_get_intraday(monkeypatch):
    expected = {"Time Series (60min)": {"2025-06-07 15:00:00": {"4. close": "150.0"}}}

    def mock_get(url, params):
        assert params["function"] == "TIME_SERIES_INTRADAY"
        assert params["interval"] == "60min"
        return DummyResponse(expected)

    monkeypatch.setattr("src.data_client.requests.get", mock_get)
    client = DataClient()
    result = client.get_intraday("TEST", interval="60min")
    assert result == expected

git add tests/test_data_client.py
git commit -m "Add pytest suite for DataClient"
