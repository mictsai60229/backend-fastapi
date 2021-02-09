from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "backend-fastapi"
    service_name: str = "fastapi"
    env: str = "beta"

    class Config:
        env_file = ".env"

settings = Settings()
