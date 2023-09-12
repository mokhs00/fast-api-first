from pydantic.v1 import BaseSettings


class Settings(BaseSettings):
    SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"


settings = Settings()
