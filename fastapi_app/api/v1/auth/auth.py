from typing import Annotated, Type
from fastapi import Depends

from schemas.auth import UserCreateRequest, UserLoginRequest
from services.auth.auth import AuthorizeService
from models import User, Token
from fastapi.routing import APIRouter

from .dependencies.auth_dependencies import get_authorize_service
from core.settings import settings

router = APIRouter(
    prefix=settings.api_prefix.v1.auth,
    tags=["Auth"],
)


@router.post("/register")
async def register_user(
    user_create_request: UserCreateRequest,
    auth_service: Annotated[AuthorizeService, Depends(get_authorize_service)],
) -> User.read_model:
    return await auth_service.create_user(user_create_request)


@router.post("/login")
async def login_user(
    user_login_request: UserLoginRequest,
    auth_service: Annotated[AuthorizeService, Depends(get_authorize_service)],
) -> Token.read_model:
    return await auth_service.login_user(user_login_request)
