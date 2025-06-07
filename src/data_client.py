import requests
from .config import Config

class DataClient:
    """
    Wrapper for market-data API calls (e.g., Alpha Vantage).
    """

    def __init__(self, base_url: str = Config.DATA_API_BASE_URL, api_key: str = Config.DATA_API_KEY):
        self.base_url = base_url
        self.api_key = api_key

    def get_daily_time_series(self, symbol: str, outputsize: str = "compact") -> dict:
        """
        Fetch daily adjusted time series for a given symbol.
        :param symbol: Ticker symbol (e.g., "AAPL")
        :param outputsize: "compact" (last 100 points) or "full"
        :return: Parsed JSON response
        """
        params = {
            "function": "TIME_SERIES_DAILY_ADJUSTED",
            "symbol": symbol,
            "apikey": self.api_key,
            "outputsize": outputsize,
        }
        resp = requests.get(self.base_url, params=params)
        resp.raise_for_status()
        return resp.json()

    def get_intraday(self, symbol: str, interval: str = "60min", outputsize: str = "compact") -> dict:
        """
        Fetch intraday time series for a given symbol.
        :param symbol: Ticker symbol
        :param interval: "1min", "5min", "15min", "30min", or "60min"
        :param outputsize: "compact" or "full"
        :return: Parsed JSON response
        """
        params = {
            "function": "TIME_SERIES_INTRADAY",
            "symbol": symbol,
            "interval": interval,
            "apikey": self.api_key,
            "outputsize": outputsize,
        }
        resp = requests.get(self.base_url, params=params)
        resp.raise_for_status()
        return resp.json()

git add src/data_client.py
git commit -m "Add market-data API wrapper in src/data_client.py"
