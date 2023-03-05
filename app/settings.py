from pydantic import BaseSettings

class Settings(BaseSettings):
    BASE_URI: str        = "/api/v1"
    PROJECT_NAME: str    = "Student Depression Analysis"
    TWEETS_LANGUAGE: str = "pt-br"


settings = Settings()