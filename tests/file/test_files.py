from http import HTTPStatus

import allure
import pytest

from api_client.errors_schema import InternalErrorResponseSchema, ValidationErrorResponseSchema
from api_client.files.file_schema import GetFileResponseSchema, UploadFileRequestSchema, UploadFileResponseSchema
from api_client.files.files_client import FilesClient
from config import settings
from fixtures.files import FileFixture
from tools.allure.epic import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from tools.allure.tags import AllureTag
from tools.assertions.base import assert_status_code
from tools.assertions.file import (
    assert_file_not_found_response,
    assert_get_file_response,
    assert_get_file_with_incorrect_file_id_response,
    assert_upload_file_response,
    assert_upload_file_with_empty_directory_response,
    assert_upload_file_with_empty_filename_response,
)
from tools.assertions.schema import validate_json_schema
from allure_commons.types import Severity


@pytest.mark.files
@pytest.mark.regression
@allure.epic(AllureEpic.LMS)
@allure.parent_suite(AllureEpic.LMS)
@allure.feature(AllureFeature.FILES)
@allure.suite(AllureFeature.FILES)
class TestsFiles:
    @allure.title("Upload file")
    @allure.tag(AllureTag.CREATE_ENTITY)
    @allure.story(AllureStory.CREATE_ENTITY)
    @allure.sub_suite(AllureStory.CREATE_ENTITY)
    @allure.severity(Severity.CRITICAL)
    def test_upload_file(self, files_client: FilesClient):
        request = UploadFileRequestSchema(upload_file=settings.test_data.file_path)
        response = files_client.upload_file_api(request)
        response_data = UploadFileResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_upload_file_response(response_data, request)

        validate_json_schema(instance=response.json(), schema=response_data.model_json_schema())

    @allure.title("Get file")
    @allure.tag(AllureTag.GET_ENTITIES)
    @allure.severity(Severity.NORMAL)
    def test_get_file(self, files_client: FilesClient, function_file: FileFixture):
        response = files_client.get_file_api(function_file.response.file.id)
        response_data = GetFileResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_get_file_response(response_data, function_file.response)

        validate_json_schema(instance=response.json(), schema=response_data.model_json_schema())

    @allure.title("Upload file with empty file name")
    @allure.tag(AllureTag.VALIDATE_ENTITY)
    @allure.severity(Severity.NORMAL)
    def test_upload_file_with_empty_filename(self, files_client: FilesClient):
        request = UploadFileRequestSchema(
            filename="",
            upload_file=settings.test_data.file_path,
        )
        response = files_client.upload_file_api(request)
        response_data = ValidationErrorResponseSchema.model_validate_json(response.text)

        # Проверяем, что код ответа соответствует ожиданиям (422 - Unprocessable Entity)
        assert_status_code(response.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)
        # Проверяем, что ответ API соответствует ожидаемой валидационной ошибке
        assert_upload_file_with_empty_filename_response(response_data)

        # Дополнительная проверка структуры JSON, чтобы убедиться, что схема валидационного ответа не изменилась
        validate_json_schema(instance=response.json(), schema=response_data.model_json_schema())

    @allure.title("Upload file with empty directory")
    @allure.tag(AllureTag.VALIDATE_ENTITY)
    @allure.severity(Severity.NORMAL)
    def test_upload_file_with_empty_directory(self, files_client: FilesClient):
        request = UploadFileRequestSchema(
            directory="",
            upload_file=settings.test_data.file_path,
        )
        response = files_client.upload_file_api(request)
        response_data = ValidationErrorResponseSchema.model_validate_json(response.text)

        # Проверяем, что код ответа соответствует ожиданиям (422 - Unprocessable Entity)
        assert_status_code(response.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)
        # Проверяем, что ответ API соответствует ожидаемой валидационной ошибке
        assert_upload_file_with_empty_directory_response(response_data)

        # Дополнительная проверка структуры JSON, чтобы убедиться, что схема валидационного ответа не изменилась
        validate_json_schema(instance=response.json(), schema=response_data.model_json_schema())

    @allure.title("Delete file")
    @allure.tag(AllureTag.DELETE_ENTITY)
    @allure.severity(Severity.MINOR)
    def test_delete_file(self, files_client: FilesClient, function_file: FileFixture):
        # 1. Удаляем файл
        delete_response = files_client.delete_file_api(function_file.response.file.id)
        # 2. Проверяем, что файл успешно удален (статус 200 ОК)
        assert_status_code(delete_response.status_code, HTTPStatus.OK)

        # 3. Пытаемся получить удаленный файл
        get_response = files_client.get_file_api(function_file.response.file.id)
        get_response_data = InternalErrorResponseSchema.model_validate_json(get_response.text)

        # 4. Проверяем, что сервер вернул 404 Not Found
        assert_status_code(get_response.status_code, HTTPStatus.NOT_FOUND)
        # 5. Проверяем, что в ответе содержится ошибка "File not found"
        assert_file_not_found_response(get_response_data)

        # 6. Проверяем, что ответ соответствует схеме
        validate_json_schema(get_response.json(), get_response_data.model_json_schema())

    @allure.title("Get file with incorrect file id")
    @allure.tag(AllureTag.VALIDATE_ENTITY)
    @allure.severity(Severity.MINOR)
    def test_get_file_with_incorrect_file_id(self, files_client: FilesClient, function_file: FileFixture):
        # 1. Запрос файла с невалидным айди
        response = files_client.get_file_api("incorrect_file_id")
        # 2. Получение модели ответа
        response_data = ValidationErrorResponseSchema.model_validate_json(response.text)
        # 3. Проверка статуса кода 422
        assert_status_code(response.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)
        # 4. Проверка соответствие ошибки File not found
        assert_get_file_with_incorrect_file_id_response(response_data)
        # 5. Проверка, что ответ соответствует схеме
        validate_json_schema(response.json(), response_data.model_json_schema())
