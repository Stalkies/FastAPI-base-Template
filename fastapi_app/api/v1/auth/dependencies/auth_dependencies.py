from repos.token import TokenRepository
from services.auth.auth import AuthorizeService
from repos.user import UserRepository
from services.auth.token import TokenService


def get_authorize_service() -> AuthorizeService:
    return AuthorizeService(UserRepository())


def get_token_service() -> TokenService:
    return TokenService(TokenRepository())
