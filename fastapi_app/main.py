from fastapi import FastAPI
from core.settings import settings
from api import router as api_router


app = FastAPI()

app.include_router(
    api_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host=settings.fastapi.host, port=settings.fastapi.port, reload=settings.fastapi.reload)