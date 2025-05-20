from core.database import async_session
from .base import SQLAlchemyRepository
from models import User
from sqlalchemy import select


class UserRepository(SQLAlchemyRepository):
    model = User

    async def get_by_email(self, email: str) -> User | None:
        """Get a user by their email."""
        async with async_session() as session:
            user = await session.execute(
                select(self.model).where(self.model.email == email)
            )
            return user.scalars().first()
