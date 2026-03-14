import os
from dotenv import load_dotenv

load_dotenv()


def _require(key: str) -> str:
    value = os.getenv(key)
    if not value:
        raise EnvironmentError(f"Missing required environment variable: {key}")
    return value


BASE_URL: str = os.getenv("OPENAI_BASE_URL", "https://api.openai.com/v1")
API_KEY: str = _require("OPENAI_API_KEY")
MODEL: str = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
NUM_RESULTS: int = int(os.getenv("NUM_RESULTS", "5"))
MAX_PAGE_CHARS: int = int(os.getenv("MAX_PAGE_CHARS", "4000"))
