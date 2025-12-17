from functools import lru_cache

from httpx import Client
from pydantic import EmailStr

from api_client.authentication.authentication_client import get_authentication_client
from api_client.authentication.authentication_schema import LoginRequestSchema
from api_client.base_pydantic_model import BasePydanticModel


class AuthenticationUserSchema(BasePydanticModel, frozen=True):
    email: EmailStr
    password: str


@lru_cache(maxsize=None)
def get_private_http_client(user: AuthenticationUserSchema) -> Client:
    """
    Функция создаёт экземпляр httpx.Client с аутентификацией пользователя.
    :param user: Объект AuthenticationUserSchema с email и паролем пользователя.
    :return: Готовый к использованию объект httpx.Client с установленным заголовком Authorization.
    """
    # Инициализируем AuthenticationClient для аутентификации
    authentication_client = get_authentication_client()

    # Инициализация запроса на аутентификацию
    login_request = LoginRequestSchema(email=user.email, password=user.password)
    login_response = authentication_client.login(login_request)

    return Client(
        timeout=5,
        base_url="http://localhost:8000",
        headers={"Authorization": f"Bearer {login_response.token.access_token}"}
    )
