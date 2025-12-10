from pydantic import EmailStr, Field

from api_client.base_pydantic_model import BasePydanticModel
from tools.fakers import fake


class TokenSchema(BasePydanticModel):
    """
    Описание структуры аутентификационных токенов.
    """
    token_type: str = Field(alias="tokenType")
    access_token: str = Field(alias="accessToken")
    refresh_token: str = Field(alias="refreshToken")


class LoginRequestSchema(BasePydanticModel):
    """
    Описание структуры запроса на аутентификацию.
    """
    email: EmailStr = Field(default_factory=fake.get_email)
    password: str = Field(default_factory=fake.get_password)


class LoginResponseSchema(BasePydanticModel):
    """
    Описание структуры ответа аутентификации.
    """
    token: TokenSchema


class RefreshTokenRequestSchema(BasePydanticModel):
    """
    Описание структуры запроса для обновления токена.
    """
    refresh_token: str = Field(alias="refreshToken", default_factory=fake.get_sentence)
