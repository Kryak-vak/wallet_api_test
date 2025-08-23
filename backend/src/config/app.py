import secrets
from pathlib import Path
from typing import Literal

from pydantic_settings import BaseSettings, SettingsConfigDict

ENV_DIR = Path(__file__).resolve().parent.parent.parent
ENV_FILE = ENV_DIR / ".env"


class AppConfig(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=ENV_FILE,
        env_ignore_empty=True,
        extra="ignore",
    )

    api_v1_str: str = "/api/v1"
    secret_key: str = secrets.token_urlsafe(32)
    enviroment: Literal["local", "staging", "production"] = "local"

    project_name: str

    first_superuser: str
    first_superuser_password: str
