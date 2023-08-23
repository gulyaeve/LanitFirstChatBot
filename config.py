from pydantic.v1 import BaseSettings


class Settings(BaseSettings):
    TOKEN: str

    class Config:
        env_file = ".env"


settings = Settings()
