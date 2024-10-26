from pydantic_settings import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    API_KEY: str
    OLLAMA_BASE_URL: str
    OLLAMA_MODEL: str

    class Config:
        env_file = ".env"

# New decorator for cache
@lru_cache()
def get_settings():
    return Settings()