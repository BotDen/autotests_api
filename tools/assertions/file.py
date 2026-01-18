from api_client.errors_schema import InternalErrorResponseSchema, ValidationErrorResponseSchema, ValidationErrorSchema
from api_client.files.file_schema import (
    FileSchema,
    GetFileResponseSchema,
    UploadFileRequestSchema,
    UploadFileResponseSchema,
)
from tools.assertions.base import assert_equal
from tools.assertions.errors import assert_internal_error_response, assert_validation_error_response


def assert_upload_file_response(
    actual: UploadFileResponseSchema,
    expected: UploadFileRequestSchema,
):
    """
    Проверка, что файл успешно загружен
    :param actual: Тело запроса на загрузку файла
    :param expected: Тело ответа после загрузки файла
    :raises AssertionError: Если хотя бы одно поле не совпало
    """
    expect_url = f"http://localhost:8000/static/{expected.directory}/{expected.filename}"
    assert_equal(str(actual.file.url), expect_url, "url")
    assert_equal(actual.file.filename, expected.filename, "filename")
    assert_equal(actual.file.directory, expected.directory, "directory")


def assert_file(actual: FileSchema, expected: FileSchema):
    """
    Проверка атрибутов файла
    :param actual: Фактические значения полей
    :param expected: Ожидаемые значения полей
    :raises AssertionError: Если хотя бы одно поле не совпало
    """
    assert_equal(actual.id, expected.id, "id")
    assert_equal(actual.url, expected.url, "url")
    assert_equal(actual.filename, expected.filename, "filename")
    assert_equal(actual.directory, expected.directory, "directory")


def assert_get_file_response(
    get_file_response: GetFileResponseSchema,
    upload_file_response: UploadFileResponseSchema,
):
    """
    Проверка, что загруженные файл соответствует загружаемому файлу
    :param get_file_response: Ответ на запрос файла
    :param upload_file_response: Ответ после загрузки файла
    :raises AssertionError: Если хотя бы одно поле не совпало
    """
    assert_file(get_file_response.file, upload_file_response.file)


def assert_upload_file_with_empty_filename_response(actual: ValidationErrorResponseSchema):
    """
    Проверяет, что ответ на создание файла с пустым именем файла соответствует ожидаемой валидационной ошибке.

    :param actual: Ответ от API с ошибкой валидации, который необходимо проверить.
    :raises AssertionError: Если фактический ответ не соответствует ожидаемому.
    """
    expected_error = ValidationErrorResponseSchema(
        detail=[
            ValidationErrorSchema(
                type="string_too_short",
                input="",
                context={"min_length": 1},
                message="String should have at least 1 character",
                location=["body", "filename"],
            ),
        ],
    )
    assert_validation_error_response(actual, expected_error)


def assert_upload_file_with_empty_directory_response(actual: ValidationErrorResponseSchema):
    """
    Проверяет, что ответ на создание файла с пустым значением директории соответствует ожидаемой валидационной ошибке.

    :param actual: Ответ от API с ошибкой валидации, который необходимо проверить.
    :raises AssertionError: Если фактический ответ не соответствует ожидаемому.
    """
    expected_error = ValidationErrorResponseSchema(
        detail=[
            ValidationErrorSchema(
                type="string_too_short",
                input="",
                context={"min_length": 1},
                message="String should have at least 1 character",
                location=["body", "directory"],
            ),
        ],
    )
    assert_validation_error_response(actual, expected_error)


def assert_file_not_found_response(actual: InternalErrorResponseSchema):
    """
    Функция для проверки ошибки, если файл не найден на сервере.

    :param actual: Фактический ответ.
    :raises AssertionError: Если фактический ответ не соответствует ошибке "File not found"
    """
    # Ожидает сообщение об ошибке, если файл не найден
    expected = InternalErrorResponseSchema(details="File not found")
    # Используем раннее созданную функцию для проверки внутренней ошибки
    assert_internal_error_response(actual, expected)


def assert_get_file_with_incorrect_file_id_response(actual: ValidationErrorResponseSchema):
    """
    Функция для проверки ошибки, при запросе файла с невалидным id

    :param actual: Фактический ответ.
    :raises AssertionError: Если фактический ответ не соответствует ошибке "File not found"
    """
    expected_error = ValidationErrorResponseSchema(
        detail=[
            ValidationErrorSchema(
                type="uuid_parsing",
                location=["path", "file_id"],
                message="Input should be a valid UUID, invalid character: expected an optional prefix of "
                        "`urn:uuid:` followed by [0-9a-fA-F-], found `i` at 1",
                input="incorrect_file_id",
                context={"error": "invalid character: expected an optional prefix of `urn:uuid:`"
                                  " followed by [0-9a-fA-F-], found `i` at 1"}
            ),
        ],
    )

    assert_validation_error_response(actual, expected_error)
