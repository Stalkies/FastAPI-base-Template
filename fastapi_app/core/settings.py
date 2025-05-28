from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import BaseModel
from pydantic import PostgresDsn


class FastAPI(BaseModel):
    host: str = "127.0.0.1"
    port: int = 8000
    reload: bool = True


class DatabaseConfig(BaseModel):
    url: PostgresDsn
    echo: bool = False
    echo_pool: bool = False
    pool_size: int = 50
    max_overflow: int = 10


class TokenConfig(BaseModel):
    expire_in: int = 604800  # 7 days


class ApiV1Prefix(BaseModel):
    prefix: str = "/v1"
    auth: str = "/auth"


class ApiPrefix(BaseModel):
    prefix: str = "/api"
    v1: ApiV1Prefix = ApiV1Prefix()


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=(".env.template", ".env"),
        case_sensitive=False,
        env_nested_delimiter="__",
        env_prefix="APP_CONFIG__",
    )
    fastapi: FastAPI = FastAPI()
    api_prefix: ApiPrefix = ApiPrefix()
    token: TokenConfig = TokenConfig()
    db: DatabaseConfig


settings = Settings()
