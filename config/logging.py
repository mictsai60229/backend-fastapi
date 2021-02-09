from pydantic import BaseSettings

class Settings(BaseSettings):
    log_file: str = ".log"

    class Config:
        env_file = ".env"

settings = Settings()