import secrets

from repos.token import TokenRepository
from schemas.tokens import TokenCreate, TokenRead


class TokenService:
    """Service for managing tokens.
    This service is responsible for creating, retrieving, and deleting tokens.
    """

    def __init__(self, token_repository: TokenRepository):
        self.token_repository: TokenRepository = token_repository

    def _generate_token(self):
        return secrets.token_urlsafe(32)

    async def create_token(self, user_id: int) -> TokenRead:
        token = self._generate_token()
        token_data = TokenCreate(user_id=user_id, token=token)
        token_model = await self.token_repository.add(token_data.model_dump())
        return token_model.to_read_model()

    async def get_token(self, token: str) -> TokenRead | None:
        token_model = await self.token_repository.get_by_field(token=token)
        if token_model:
            return token_model.to_read_model()
        return None

    async def delete_token(self, token: str) -> None:
        token_model = await self.token_repository.get_by_field(token=token)
        if token_model:
            await self.token_repository.delete(token_model.id)
