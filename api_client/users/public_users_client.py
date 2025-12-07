from typing import TypedDict

from httpx import Response

from api_client.api_client import APIClient


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
