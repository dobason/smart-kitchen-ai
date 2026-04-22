from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path
from typing import Optional

ROOT = Path(__file__).resolve().parents[2]
ENV_FILE = str(ROOT / ".env") if (ROOT / ".env").exists() else str(ROOT / ".env.example")

class Settings(BaseSettings):

    model_config = SettingsConfigDict(
        env_file=ENV_FILE,
        extra="ignore",
        env_ignore_empty=True)

    # minIO
    MINIO_ENDPOINT: str
    MINIO_ACCESS_KEY: str
    MINIO_SECRET_KEY: str
    MINIO_BUCKET: str
    MINIO_ENDPOINT_SECURE: Optional[bool] = True
    MINIO_IS_PUBLIC_BUCKET: Optional[bool] = False
    MINIO_PRESIGNED_URL_EXPIRY_DAYS: Optional[int] = 7

    # LLM
    GEMINI_API_KEY: str
    OPENROUTER_API_KEY: str
    OPENROUTER_URL: str

settings = Settings()
