from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, ForeignKey

from core.settings import settings
from .base import Base
from schemas.tokens import TokenRead


class Token(Base[TokenRead]):

    read_model = TokenRead
    id: Mapped[int] = mapped_column(primary_key=True)
    token: Mapped[str] = mapped_column(index=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), index=True)
    user: Mapped["User"] = relationship("User")
    created_at: Mapped[int] = mapped_column(
        Integer, default=int(datetime.now().timestamp())
    )
    expire_at: Mapped[int] = mapped_column(
        Integer, default=int(datetime.now().timestamp()) + int(settings.token.expire_in)
    )
