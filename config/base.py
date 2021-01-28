from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "backend-fastapi"

    class Config:
        env_file = ".env"

settings = Settings()
