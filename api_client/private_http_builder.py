from typing import TypedDict

from httpx import Client

from api_client.authentication.authentication_client import LoginRequestDict, get_authentication_client


class AuthenticationUserDict(TypedDict):
    email: str
    password: str


def get_private_http_client(user: AuthenticationUserDict) -> Client:
    """
    Функция создаёт экземпляр httpx.Client с аутентификацией пользователя.
    :param user: Объект AuthenticationUserSchema с email и паролем пользователя.
    :return: Готовый к использованию объект httpx.Client с установленным заголовком Authorization.
    """
    # Инициализируем AuthenticationClient для аутентификации
    authentication_client = get_authentication_client()

    # Инициализация запроса на аутентификацию
    login_request = LoginRequestDict(email=user["email"], password=user["password"])
    login_response = authentication_client.login(login_request)

    return Client(
        headers={"Authorization": f"Bearer {login_response["token"]["accessToken"]}"}
    )
