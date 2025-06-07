import os
from dotenv import load_dotenv

# Load variables from .env
load_dotenv()

class Config:
    """Configuration values pulled from environment variables."""
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY")
    DATA_API_KEY: str = os.getenv("DATA_API_KEY")
    
    # Optional: override defaults via .env
    DATA_API_BASE_URL: str = os.getenv(
        "DATA_API_BASE_URL",
        "https://www.alphavantage.co/query"
    )
    OPENAI_API_BASE: str = os.getenv(
        "OPENAI_API_BASE",
        "https://api.openai.com/v1"
    )

    @classmethod
    def validate(cls):
        missing = [
            name for name in ("OPENAI_API_KEY", "DATA_API_KEY")
            if not getattr(cls, name)
        ]
        if missing:
            raise RuntimeError(
                f"Missing required config vars: {', '.join(missing)}"
            )

# Validate on import
Config.validate()

git add src/config.py
git commit -m "Add config loader for environment variables"
