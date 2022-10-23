from pydantic import BaseSettings


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"

    PROJECT_NAME: str = "Data API"

    POSTGRES_HOST: str

    POSTGRES_USERNAME: str

    POSTGRES_PASSWORD: str

    POSTGRES_DATABASE: str
    
    POSTGRES_PORT : int

    class Config:
        case_sensitive = True
        env_file = ".env"


settings = Settings()
