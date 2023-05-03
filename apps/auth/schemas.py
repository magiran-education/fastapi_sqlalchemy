from fastapi_users import schemas


# ниже в классах дописываем кастомные поля. Стандартные поля уже наследуются.

class UserRead(schemas.BaseUser[int]):
    username: str
    role_id: int


class UserCreate(schemas.BaseUserCreate):
    username: str
    role_id: int


class UserUpdate(schemas.BaseUserUpdate):
    username: str
    role_id: int
