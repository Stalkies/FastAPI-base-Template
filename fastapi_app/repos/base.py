from abc import ABC

from core.database import async_session


class AbstractRepository(ABC):
    async def add(self, obj) -> None:
        """Add an object to the database."""
        pass

    async def get_by_id(self, id_) -> None:
        """Get an object by its ID."""
        pass

    async def get_by_field(self, **kwargs) -> None:
        """Get an object by a specific field."""
        pass

    async def update(self, id_, **kwargs) -> None:
        """Update an object by its ID."""
        pass

    async def delete(self, id_) -> None:
        """Delete an object by its ID."""
        pass

    async def get_all(self) -> None:
        """Get all objects."""
        pass

    async def get_with_pagination(self, offset: int, limit: int) -> None:
        """Get objects with pagination."""
        pass

    async def get_with_filter(self, **kwargs) -> None:
        """Get objects with specific filters."""
        pass

    async def get_with_pagination_and_filter(
        self, offset: int, limit: int, **kwargs
    ) -> None:
        """Get objects with pagination and specific filters."""
        pass


class SQLAlchemyRepository(AbstractRepository):
    model = None

    async def add(self, obj) -> model:
        """Add an object to the database."""
        async with async_session() as session:
            session.add(obj)
            await session.commit()
            await session.refresh(obj)
            return obj

    async def get_by_id(self, id_) -> model | None:
        """Get an object by its ID."""
        async with async_session() as session:
            obj = await session.get(self.model, id_)
            return obj

    async def get_by_field(self, **kwargs) -> model | None:
        """Get an object by a specific field."""
        async with async_session() as session:
            obj = await session.query(self.model).filter_by(**kwargs).first()
            return obj

    async def update(self, id_, **kwargs) -> model | None:
        """Update an object by its ID."""
        async with async_session() as session:
            obj = await session.get(self.model, id_)
            for key, value in kwargs.items():
                setattr(obj, key, value)
            await session.commit()
            await session.refresh(obj)
            return obj

    async def delete(self, id_) -> model | None:
        """Delete an object by its ID."""
        async with async_session() as session:
            obj = await session.get(self.model, id_)
            await session.delete(obj)
            await session.commit()
            return obj

    async def get_all(self) -> list[model]:
        """Get all objects."""
        async with async_session() as session:
            objs = await session.query(self.model).all()
            return objs

    async def get_with_pagination(self, offset: int, limit: int) -> list[model]:
        """Get objects with pagination."""
        async with async_session() as session:
            objs = await session.query(self.model).offset(offset).limit(limit).all()
            return objs

    async def get_with_filter(self, **kwargs) -> list[model]:
        """Get objects with specific filters."""
        async with async_session() as session:
            objs = await session.query(self.model).filter_by(**kwargs).all()
            return objs

    async def get_with_pagination_and_filter(
        self, offset: int, limit: int, **kwargs
    ) -> list[model]:
        """Get objects with pagination and specific filters."""
        async with async_session() as session:
            objs = (
                await session.query(self.model)
                .filter_by(**kwargs)
                .offset(offset)
                .limit(limit)
                .all()
            )
            return objs
