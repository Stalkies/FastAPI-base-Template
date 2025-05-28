from sys import prefix

from fastapi import APIRouter
from core.settings import settings
from .auth.auth import router as auth_router


router = APIRouter(prefix=settings.api_prefix.v1.prefix)

router.include_router(auth_router)
