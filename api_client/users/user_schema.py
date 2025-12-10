from pydantic import EmailStr, Field

from api_client.base_pydantic_model import BasePydanticModel
from tools.fakers import fake


class UserSchema(BasePydanticModel):
    """
    Описание структуры объекта User
    """
    id: str
    email: EmailStr
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")


class CreateUserRequestSchema(BasePydanticModel):
    """
    Описание структуры запроса для создания пользователя
    """
    email: EmailStr = Field(default_factory=fake.get_email)
    password: str = Field(default_factory=fake.get_password)
    last_name: str = Field(alias="lastName", default_factory=fake.get_last_name)
    first_name: str = Field(alias="firstName", default_factory=fake.get_first_name)
    middle_name: str = Field(alias="middleName", default_factory=fake.get_middle_name)


class CreateUserResponseSchema(BasePydanticModel):
    """
    Описание структуры ответа при создании пользователя
    """
    user: UserSchema


class UpdateUserRequestSchema(BasePydanticModel):
    """
    Описание структуры запроса на обновление пользователя.
    """
    email: EmailStr | None = Field(default_factory=fake.get_email)
    last_name: str | None = Field(alias="lastName", default_factory=fake.get_last_name)
    firs_name: str | None = Field(alias="firstName", default_factory=fake.get_first_name)
    middle_name: str | None = Field(alias="middleName", default_factory=fake.get_middle_name)


class GetUserResponseSchema(BasePydanticModel):
    user: UserSchema
