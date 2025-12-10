from pydantic import HttpUrl

from api_client.base_pydantic_model import BasePydanticModel


class FileSchema(BasePydanticModel):
    """
    Описание структуры объекта File
    """
    id: str
    filename: str
    directory: str
    url: HttpUrl


class UploadFileRequestSchema(BasePydanticModel):
    """
    Описание структуры запроса на создание файла.
    """
    filename: str
    directory: str
    upload_file: str


class UploadFileResponseSchema(BasePydanticModel):
    """
    Описание структуры ответа при загрузке файла
    """
    file: FileSchema
