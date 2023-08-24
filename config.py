from pydantic.v1 import BaseSettings


class Settings(BaseSettings):
    TOKEN: str

    OPENWEATHER_API_LINK: str
    OPENWEATHER_API_TOKEN: str

    class Config:
        env_file = ".env"


settings = Settings()
