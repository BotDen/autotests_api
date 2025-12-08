from typing import TypedDict

from httpx import Response

from api_client.api_client import APIClient
from api_client.public_http_builder import get_public_http_client


class CreateUserRequestDict(TypedDict):
    """
    Описание структуры запроса для создания пользователя
    """
    email: str
    password: str
    lastName: str
    firstName: str
    middleName: str


class PublicUsersClient(APIClient):
    """
    Клиент для работы с api/v1/users
    """
    def create_user_api(self, request: CreateUserRequestDict) -> Response:
        """
        Метод создания нового пользователя
        :param request: Словарь с телом запроса
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post(url="api/v1/users", json=request)


# Добавляем builder для PublicUserClient
def get_public_users_client() -> PublicUsersClient:
    """
    Функция создаёт экземпляр PublicUsersClient с уже настроенным HTTP-клиентом.
    :return: Готовый к использованию PublicUsersClient.
    """
    return PublicUsersClient(client=get_public_http_client())
