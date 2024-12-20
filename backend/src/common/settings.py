from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    jwt_secret_key: str = "JWT_SECRET_KEY"
    database_url: str = f"sqlite:///database.db"
    
    model_config = SettingsConfigDict(env_file=".env")

@lru_cache
def get_settings() -> Settings:
    return Settings()