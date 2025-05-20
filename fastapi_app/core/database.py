from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from core.settings import settings


engine = create_async_engine(settings.db.url, echo=settings.db.echo)

# noinspection PyTypeChecker
async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


async def get_session() -> AsyncGenerator[AsyncSession, AsyncSession]:
    async with async_session() as session:
        yield session
