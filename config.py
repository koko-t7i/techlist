import secrets
from typing import Literal

from pydantic_settings import BaseSettings


class Config(BaseSettings):
    VERSION: str = 'v1'
    DEBUG: bool = True
    PROJECT_NAME: str = 'Tech API'
    SENTRY_DSN: str | None = None

    API_V1_STR: str = '/api/v1'
    SECRET_KEY: str = secrets.token_urlsafe(32)

    # 60 minutes * 24 hours * 8 days = 8 days
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
    FRONTEND_HOST: str = 'http://localhost:5173'
    ENVIRONMENT: Literal['local', 'staging', 'production'] = 'local'

    APP_MODELS: dict = {'models': ['app.models']}
    POSTGRES_SERVER: str = 'localhost'
    POSTGRES_PORT: int = 5432
    POSTGRES_USER: str = 'postgres'
    POSTGRES_PASSWORD: str = 'postgres'
    POSTGRES_DB: str = 'tech'

    REDIS_URL: str = 'redis://localhost:6379/1'

    @property
    def ORM_URL(self) -> str:
        return (
            f'postgres://{self.POSTGRES_USER}:'
            f'{self.POSTGRES_PASSWORD}@'
            f'{self.POSTGRES_SERVER}:'
            f'{self.POSTGRES_PORT}/'
            f'{self.POSTGRES_DB}'
        )

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


CONF = Config()
