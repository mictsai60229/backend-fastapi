from pydantic import BaseSettings

class Settings(BaseSettings):
    log_file: str = "logs/.log"
    backup_count: int = 7
    max_bytes: int = 1024*1024

    class Config:
        env_file = ".env"

settings = Settings()