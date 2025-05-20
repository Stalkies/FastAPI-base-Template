from models import Token
from .base import SQLAlchemyRepository


class TokenRepository(SQLAlchemyRepository[Token]):
    model = Token
