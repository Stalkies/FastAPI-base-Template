from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import declared_attr
from utils import camel_case_to_snake_case
from pydantic import BaseModel
from typing import Generic, TypeVar, Type

T = TypeVar("T")


class Base(DeclarativeBase, Generic[T]):
    read_model: Type[T]

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return camel_case_to_snake_case(cls.__name__)

    def to_read_model(self) -> T:
        """Convert the model to a read model."""
        return self.read_model(**self.model_dump())

    def model_dump(self) -> dict:
        """Dump the model to a dictionary."""
        return {
            column.name: getattr(self, column.name)
            for column in self.__tablename__.columns
        }
