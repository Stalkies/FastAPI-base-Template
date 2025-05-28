from bcrypt import hashpw, gensalt, checkpw
from fastapi import HTTPException
from starlette.status import HTTP_401_UNAUTHORIZED

from repos.token import TokenRepository
from repos.user import UserRepository
from schemas.tokens import TokenRead
from schemas.auth import UserCreateRequest, UserInDB, UserLoginRequest, UserDBAdd

from .token import TokenService


class AuthorizeService:
    def __init__(self, user_repository: UserRepository):
        self._user_repository = user_repository
        self._token_service = TokenService(TokenRepository())

    @staticmethod
    def _hash_password(password: str):
        pwd_bytes = password.encode()
        salt = gensalt()
        return hashpw(pwd_bytes, salt)

    @staticmethod
    def _verify_password(password: str, hashed_password: bytes):
        return checkpw(password=password.encode(), hashed_password=hashed_password)

    async def create_user(self, user_create_request: UserCreateRequest):
        user_record = await self._user_repository.get_by_email(user_create_request.email)
        if user_record:
            raise HTTPException(status_code=400, detail="User with this email already exists")
        hashed_password = self._hash_password(user_create_request.password)
        user_db_add_model = UserDBAdd(
            email=user_create_request.email,
            hashed_password=hashed_password,
        )

        user_record = await self._user_repository.add(user_db_add_model.model_dump())
        return user_record.to_read_model()


    async def login_user(self, user_login_request: UserLoginRequest) -> TokenRead:
        user_record = await self._user_repository.get_by_email(user_login_request.email)
        if not user_record:
            raise HTTPException(HTTP_401_UNAUTHORIZED, "Invalid credentials")
        user_in_db = UserInDB.model_validate(user_record)
        if self._verify_password(
            user_login_request.password, user_in_db.hashed_password
        ):
            token = await self._token_service.create_token(user_in_db.id)
            return token
        else:
            raise HTTPException(HTTP_401_UNAUTHORIZED, "Invalid credentials")



