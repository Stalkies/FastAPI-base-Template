from pydantic_settings import BaseSettings
from pydantic import BaseModel


class FastAPI(BaseModel):
    host: str = "127.0.0.1"
    port: int = 8000
    reload: bool = True


class ApiPrefix(BaseModel):
    prefix: str = "/api"


class Settings(BaseSettings):
    fastapi: FastAPI = FastAPI()
    api_prefix: ApiPrefix = ApiPrefix()


settings = Settings()
