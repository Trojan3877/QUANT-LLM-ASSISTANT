# Config Loader

`src/config.py` provides a simple class to load and validate required environment variables.

```python
from .config import Config

# Access values
api_key = Config.OPENAI_API_KEY
base_url = Config.DATA_API_BASE_URL

# Validate at runtime (raises if missing)
Config.validate()

## Class: `Config`

| Attribute           | Type   | Default                                       | Description                                   |
|---------------------|--------|-----------------------------------------------|-----------------------------------------------|
| `OPENAI_API_KEY`    | `str`  | _env var_                                     | Your OpenAI API key (required).               |
| `DATA_API_KEY`      | `str`  | _env var_                                     | Your market-data API key (required).          |
| `DATA_API_BASE_URL` | `str`  | `"https://www.alphavantage.co/query"`         | Base URL for data-provider requests.          |
| `OPENAI_API_BASE`   | `str`  | `"https://api.openai.com/v1"`                 | Base URL for OpenAI API requests.             |
