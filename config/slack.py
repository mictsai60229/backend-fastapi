from pydantic import BaseSettings

class Settings(BaseSettings):
    slack_bot_token: str = ""
    slack_is_log: bool = False
    slack_channel: str = ""

    class Config:
        env_file = ".env"

settings = Settings()