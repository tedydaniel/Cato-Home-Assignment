from functools import lru_cache
import os
from pydantic import field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path

PROJECT_ROOT = Path(os.environ.get("PROJECT_ROOT", Path(__file__).resolve().parents[2]))

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=PROJECT_ROOT / ".env", extra="ignore")
    postgres_url: str
    data_path: Path = Path(PROJECT_ROOT / "data")
    openai_api_key: str = ""
    openai_model: str = "gpt-5.4-mini"
    knowledge_min_score: float = 0.020
    langsmith_api_key: str = ""
    langsmith_project: str = "cato-support-engineer"
    langsmith_endpoint: str = ""
    cors_origins: str = "http://localhost:3000"

    @field_validator("openai_model", mode="before")
    @classmethod
    def use_default_model_when_blank(cls, value: object) -> object:
        return "gpt-5.4-mini" if value is None or not str(value).strip() else value

@lru_cache
def get_settings() -> Settings:
    return Settings()
