from typing import Annotated
from fastapi import Depends, APIRouter, status

from schemas.auth import UserCreateRequest, UserLoginRequest
from services.auth.auth import AuthorizeService
from models import User, Token
from .dependencies.auth_dependencies import get_authorize_service
from core.settings import settings

router = APIRouter(
    prefix=settings.api_prefix.v1.auth,
    tags=["Auth"],
)


@router.post(
    "/register",
    summary="Register a new user",
    description="Create a new user account with email and password.",
    response_model=User.read_model,
    status_code=status.HTTP_201_CREATED,
    responses={
        201: {"description": "User successfully registered"},
        400: {"description": "User with this email already exists"},
    },
)
async def register_user(
    user_create_request: UserCreateRequest,
    auth_service: Annotated[AuthorizeService, Depends(get_authorize_service)],
) -> User.read_model:
    return await auth_service.create_user(user_create_request)


@router.post(
    "/login",
    summary="User login",
    description="Authenticate a user with email and password. Returns an access token.",
    response_model=Token.read_model,
    responses={
        200: {"description": "Login successful"},
        401: {"description": "Invalid credentials"},
    },
)
async def login_user(
    user_login_request: UserLoginRequest,
    auth_service: Annotated[AuthorizeService, Depends(get_authorize_service)],
) -> Token.read_model:
    return await auth_service.login_user(user_login_request)
