from pydantic import BaseModel, ConfigDict, EmailStr, Field


class UserRequestAdd(BaseModel):
    email: EmailStr
    password: str
    first_name: str | None = Field(None)
    last_name: str | None = Field(None)


class UserAdd(BaseModel):
    email: EmailStr
    hashed_password: str
    first_name: str | None = Field(None)
    last_name: str | None = Field(None)


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class User(BaseModel):
    id: int
    email: EmailStr
    first_name: str | None = Field(None)
    last_name: str | None = Field(None)

    model_config = ConfigDict(from_attributes=True)


class UserWithHashedPassword(User):
    hashed_password: str
