import pytest

from api_client.base_pydantic_model import BasePydanticModel
from api_client.files.file_schema import UploadFileRequestSchema, UploadFileResponseSchema
from api_client.files.files_client import FilesClient, get_private_file_client
from fixtures.users import UserFixture


class FileFixture(BasePydanticModel):
    request: UploadFileRequestSchema
    response: UploadFileResponseSchema


@pytest.fixture
def files_client(function_user: UserFixture) -> FilesClient:
    return get_private_file_client(function_user.authentication_user)


@pytest.fixture
def function_file(files_client: FilesClient) -> FileFixture:
    request = UploadFileRequestSchema(upload_file="./test_data/files/chubaka.jpg")
    response = files_client.upload_file(request=request)
    return FileFixture(request=request, response=response)
