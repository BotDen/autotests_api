from typing import TypedDict
from httpx import Response
from api_client.api_client import APIClient
from api_client.private_http_builder import AuthenticationUserDict, get_private_http_client


class File(TypedDict):
    """
    Описание структуры объекта File
    """
    id: str
    filename: str
    directory: str
    url: str


class UploadFileRequestDict(TypedDict):
    """
    Описание структуры запроса на создание файла.
    """
    filename: str
    directory: str
    upload_file: str


class UploadFileResponseDict(TypedDict):
    """
    Описание структуры ответа при загрузке файла
    """
    file: File


class FilesClient(APIClient):
    def get_file_api(self, file_id: str) -> Response:
        """
        Метод получения файла.
        :param file_id: Идентификатор файла.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(url=f"/api/v1/file/{file_id}")

    def delete_file_api(self, file_id: str) -> Response:
        """
        Метод удаления файла.
        :param file_id: Идентификатор файла.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(url=f"/api/v1/file/{file_id}")

    def upload_file_api(self, request: UploadFileRequestDict) -> Response:
        """
        Метод создания файла.
        :param request: Словарь с filename, directory, upload_file.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post(
            url=f"/api/v1/files",
            data=request,
            files={"upload_file": open(request["upload_file"], "rb")},
        )

    def upload_file(self, request: UploadFileRequestDict) -> UploadFileResponseDict:
        """
        Метод загрузки файла с возвратом ответа в виде json
        :param request: Словарь с filename, directory, upload_file.
        :return: Ответ от сервера в виде json объекта
        """
        response = self.upload_file_api(request=request)
        return response.json()


def get_private_file_client(user: AuthenticationUserDict) -> FilesClient:
    """
    Функция создаёт экземпляр FilesClient с уже настроенным HTTP-клиентом.
    :return: Готовый к использованию FilesClient.
    """
    return FilesClient(client=get_private_http_client(user))
