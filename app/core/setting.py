from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    app_name: str = Field(default="FastAPI")
    secret_key: str = Field(default="change_me")
    database_url: str = Field(default="sqlite:///./my-fastapi-template.db")


@lru_cache
def get_settings() -> Settings:
    settings = Settings()  # type: ignore
    if settings.secret_key == "change_me":
        ...  # TODO warning
    return settings
