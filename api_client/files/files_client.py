import allure
from httpx import Response
from api_client.api_client import APIClient
from api_client.files.file_schema import UploadFileRequestSchema, UploadFileResponseSchema
from api_client.private_http_builder import AuthenticationUserSchema, get_private_http_client


class FilesClient(APIClient):
    @allure.step("Get file by file_id {file_id}")
    def get_file_api(self, file_id: str) -> Response:
        """
        Метод получения файла.
        :param file_id: Идентификатор файла.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(url=f"/api/v1/files/{file_id}")

    @allure.step("Delete file by file_id {file_id}")
    def delete_file_api(self, file_id: str) -> Response:
        """
        Метод удаления файла.
        :param file_id: Идентификатор файла.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(url=f"/api/v1/files/{file_id}")

    @allure.step("Upload file")
    def upload_file_api(self, request: UploadFileRequestSchema) -> Response:
        """
        Метод создания файла.
        :param request: Словарь с filename, directory, upload_file.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post(
            url=f"/api/v1/files",
            data=request.model_dump(by_alias=True, exclude={"upload_file"}),
            files={"upload_file": open(request.upload_file.read_bytes())},
        )

    def upload_file(self, request: UploadFileRequestSchema) -> UploadFileResponseSchema:
        """
        Метод загрузки файла с возвратом ответа в виде json
        :param request: Словарь с filename, directory, upload_file.
        :return: Ответ от сервера в виде json объекта
        """
        response = self.upload_file_api(request=request)
        return UploadFileResponseSchema.model_validate_json(response.text)


def get_private_file_client(user: AuthenticationUserSchema) -> FilesClient:
    """
    Функция создаёт экземпляр FilesClient с уже настроенным HTTP-клиентом.
    :return: Готовый к использованию FilesClient.
    """
    return FilesClient(client=get_private_http_client(user))
