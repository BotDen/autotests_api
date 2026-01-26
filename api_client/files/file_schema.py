from pydantic import Field, FilePath, HttpUrl

from api_client.base_pydantic_model import BasePydanticModel
from tools.fakers import fake


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
    filename: str = Field(default_factory=fake.get_uuid)
    directory: str = Field(default="test_data")
    upload_file: FilePath


class UploadFileResponseSchema(BasePydanticModel):
    """
    Описание структуры ответа при загрузке файла
    """
    file: FileSchema


class GetFileResponseSchema(BasePydanticModel):
    file: FileSchema
