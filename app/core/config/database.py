from typing import Any

from pydantic import BaseSettings, validator


class Database(BaseSettings):
    MYSQL_HOST: str
    MYSQL_DATABASE: str = "scrape-master"
    MYSQL_USER: str
    MYSQL_PASSWORD: str
    MYSQL_PORT: str

    DB_URI: str | None

    @validator("DB_URI", pre=True)
    def assemble_db_uri(self, v: str, values: dict[str, Any]) -> str | None:
        if isinstance(v, str):
            return v
        return (
            f'mysql+mysqldb://{values.get("MYSQL_USER")}'
            f':{values.get("MYSQL_PASSWORD")}'
            f'@{values.get("MYSQL_HOST")}:{values.get("MYSQL_PORT")}'
            f'/{values.get("MYSQL_DATABASE")}'
        )
