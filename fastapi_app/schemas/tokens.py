from pydantic import BaseModel


class TokenBase(BaseModel):
    token: str


class TokenCreate(TokenBase):
    user_id: int


class TokenRead(TokenCreate):
    created_at: int
