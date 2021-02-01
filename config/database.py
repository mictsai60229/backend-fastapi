from pydantic import BaseSettings

class Settings(BaseSettings):
    db_connection: str = "sqlite"

    class Config:
        env_file = ".env"


class SqliteSettings(BaseSettings):
    db_driver: str = "sqlite"
    db_database: str = "database.sqlite"

    class Config:
        env_file = ".env"


class PqsqlSettings(BaseSettings):
    db_driver: str = "postgresql"
    db_host: str = "127.0.0.1"
    db_port: str = "5432"
    db_database: str = "forge"
    db_username: str = "forge"
    db_password: str = ""
    db_charset: str = "utf8"

    class Config:
        env_file = ".env"


db_mappings = {
    "sqlite": SqliteSettings,
    "postgresql":  PqsqlSettings
}

settings = Settings()
db_dirver = db_mappings.get(settings.db_connection, "sqlite")
db_settings = db_mappings[db_dirver]()





