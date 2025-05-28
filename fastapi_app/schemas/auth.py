from pydantic import BaseModel, ConfigDict
from pydantic import EmailStr


# ==========Base models=========#
class UserBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    email: EmailStr


class UserRead(UserBase):
    id: int
    is_active: bool
    is_superuser: bool
    is_verified: bool


class UserInDB(UserRead):
    hashed_password: bytes


# ==============================#


# =========Request models========#
class UserCreateRequest(UserBase):
    password: str


class UserLoginRequest(UserBase):
    password: str


# =============================#


# =========Response models=======#
class UserResponse(UserRead):
    pass


# ===============================#
