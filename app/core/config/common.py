import secrets

from pydantic import AnyHttpUrl, BaseSettings, validator


class Common(BaseSettings):
    PROJECT_NAME: str = "scrape"

    API_V1_STR: str = "/api/v1"

    SECRET_KEY: str = secrets.token_urlsafe(32)
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8

    SERVER_NAME: str

    BACKEND_CORS_ORIGINS: list[AnyHttpUrl] = []

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(
        self,
        v: str | list[str],
    ) -> str | list[str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)
