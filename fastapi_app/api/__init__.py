from fastapi import APIRouter

from core.settings import settings

router = APIRouter(
    prefix=settings.api_prefix.prefix,
    tags=["API"],
)
