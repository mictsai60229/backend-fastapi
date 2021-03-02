from pydantic import BaseSettings

class Settings(BaseSettings):
    logging_file: str = "logs/.log"
    logging_backup_count: int = 7
    logging_max_bytes: int = 1024*1024

    class Config:
        env_file = ".env"

settings = Settings()