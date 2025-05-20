from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, ForeignKey
from .base import Base
from schemas.tokens import TokenRead


class Token(Base[TokenRead]):

    read_model = TokenRead

    token: Mapped[str] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), index=True)
    user: Mapped["User"] = relationship("User", back_populates="tokens")
    created_at: Mapped[int] = mapped_column(
        Integer, index=True, default=int(datetime.now().timestamp())
    )
