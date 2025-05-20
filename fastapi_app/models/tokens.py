from typing import TYPE_CHECKING
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer, ForeignKey
from .base import Base

if TYPE_CHECKING:
    from .users import User


class Token(Base):

    token: Mapped[str] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), index=True)
    user: Mapped["User"] = mapped_column(back_populates="tokens")
    created_at: Mapped[int] = mapped_column(Integer, index=True)
