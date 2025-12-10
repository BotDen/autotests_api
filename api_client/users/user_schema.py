from pydantic import Field

from api_client.base_pydantic_model import BasePydanticModel


class UserSchema(BasePydanticModel):
    """
    Описание структуры объекта User
    """
    id: str
    email: str
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")


class CreateUserRequestSchema(BasePydanticModel):
    """
    Описание структуры запроса для создания пользователя
    """
    email: str
    password: str
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")


class CreateUserResponseSchema(BasePydanticModel):
    """
    Описание структуры ответа при создании пользователя
    """
    user: UserSchema


class UpdateUserRequestSchema(BasePydanticModel):
    """
    Описание структуры запроса на обновление пользователя.
    """
    email: str | None
    last_name: str | None = Field(alias="lastName")
    firs_name: str | None = Field(alias="firstName")
    middle_name: str | None = Field(alias="middleName")


class GetUserResponseSchema(BasePydanticModel):
    user: UserSchema
