from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")

    DATABASE_URL: str
    SECRET_KEY: str = "dev-secret-change-me"
    CORS_ORIGINS: list[str] = ["http://localhost:3000"]


settings = Settings()
