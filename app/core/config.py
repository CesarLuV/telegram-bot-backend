from os import getenv

from pydantic_settings import BaseSettings


DB_USER = getenv("DB_USER", "root")
DB_PWD = getenv("DB_PWD", "my_super_strong_pass")
DB_HOST = getenv("DB_HOST", "localhost")
DB_PORT = getenv("DB_PORT", 3306)
DB_NAME = getenv("DB_NAME", "db_name")


class Settings(BaseSettings):
    DATABASE_URL: str = f"mysql+pymysql://{DB_USER}:{DB_PWD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    SECRET_KEY: str = "secret-key"

    class Config:
        env_file = ".env"


settings = Settings()
