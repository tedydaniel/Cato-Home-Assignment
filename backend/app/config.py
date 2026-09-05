from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=PROJECT_ROOT / ".env", extra="ignore")
    postgres_url: str
    redis_url: str
    data_path: Path = Path(PROJECT_ROOT / "data")
    openai_api_key: str = ""

@lru_cache
def get_settings() -> Settings:
    return Settings()
