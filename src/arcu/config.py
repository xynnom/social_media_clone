from pydantic import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    app_name: str = "CDS APP API"

    POSTGRES_SERVER: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    POSTGRES_DB_CONN_STRING: str

    authjwt_private_key: str
    authjwt_public_key: str
    authjwt_algorithm: str
    authjwt_decode_audience: str

    class Config:
        env_file = "../.env"


@lru_cache()
def get_settings():
    return Settings()
