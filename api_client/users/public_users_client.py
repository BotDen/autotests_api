from typing import TypedDict

from httpx import Response

from api_client.api_client import APIClient
from api_client.public_http_builder import get_public_http_client



class UserDict(TypedDict):
    """
    Описание структуры объекта User
    """
    id: str
    email:str
    lastName: str
    firstName: str
    middleName: str


class CreateUserRequestDict(TypedDict):
    """
    Описание структуры запроса для создания пользователя
    """
    email: str
    password: str
    lastName: str
    firstName: str
    middleName: str


class CreatedUserResponseDict(TypedDict):
    """
    Описание структуры ответа при создании пользователя
    """
    user: UserDict


class PublicUsersClient(APIClient):
    """
    Клиент для работы с api/v1/users
    """
    def create_user_api(self, request: CreateUserRequestDict) -> Response:
        """
        Метод создания нового пользователя
        :param request: Словарь с email, password, lastName, firstName, middleName
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post(url="api/v1/users", json=request)

    def create_user(self, request: CreateUserRequestDict) -> CreatedUserResponseDict:
        """
        Метод создания пользователя с возвратом объекта в виде json
        :param request: Словарь с email, password, lastName, firstName, middleName
        :return: Ответ от сервера в виде json объекта
        """
        response = self.create_user_api(request)
        return response.json()


# Добавляем builder для PublicUserClient
def get_public_users_client() -> PublicUsersClient:
    """
    Функция создаёт экземпляр PublicUsersClient с уже настроенным HTTP-клиентом.
    :return: Готовый к использованию PublicUsersClient.
    """
    return PublicUsersClient(client=get_public_http_client())
