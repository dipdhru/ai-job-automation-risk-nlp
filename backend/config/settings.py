"""Application configuration and environment variables."""
from pydantic_settings import BaseSettings
from pydantic import ConfigDict
from functools import lru_cache


class Settings(BaseSettings):
    model_config = ConfigDict(env_file=".env", case_sensitive=True)

    APP_NAME: str = "AI Job Risk Analyzer"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = False

    DATABASE_URL: str = "postgresql://user:password@localhost:5432/ai_risk_analyzer"

    SECRET_KEY: str = "your-secret-key-change-in-production"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    STRIPE_API_KEY: str = ""
    STRIPE_WEBHOOK_SECRET: str = ""

    CORS_ORIGINS: list = ["http://localhost:3000", "http://localhost:8501"]

    MODEL_ARTIFACTS_PATH: str = "../app/artifacts"


@lru_cache()
def get_settings() -> Settings:
    return Settings()
