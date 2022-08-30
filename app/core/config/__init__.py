from pydantic import BaseSettings

from .common import Common
from .sentry import Sentry
from .logging import LogConfig
from .database import Database


class Settings(Common, Sentry, Database, LogConfig):
    class Config:
        case_sensitive = True
        env_file = ".env"


settings = Settings()
