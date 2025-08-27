import secrets
from typing import Literal

from pydantic_settings import BaseSettings, SettingsConfigDict


class AppConfig(BaseSettings):
    model_config = SettingsConfigDict(
        env_ignore_empty=True,
        extra="ignore",
    )

    api_v1_str: str = "/api/v1"
    secret_key: str = secrets.token_urlsafe(32)
    enviroment: Literal["local", "staging", "production"] = "local"

    project_name: str

    first_superuser: str
    first_superuser_password: str


app_config = AppConfig()  # type: ignore[call-arg]
