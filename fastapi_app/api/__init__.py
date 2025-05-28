from fastapi import APIRouter

from core.settings import settings
from .v1 import router as v1_router

router = APIRouter(
    prefix=settings.api_prefix.prefix,
)

router.include_router(v1_router)
