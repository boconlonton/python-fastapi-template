from pydantic import BaseSettings, HttpUrl, validator


class Sentry(BaseSettings):
    SENTRY_DSN: HttpUrl | None = None

    @validator("SENTRY_DSN", pre=True)
    def sentry_dsn_can_be_blank(self, v: str) -> str | None:
        if len(v) == 0:
            return None
        return v
