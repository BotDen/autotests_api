import pytest

from api_client.base_pydantic_model import BasePydanticModel
from api_client.courses.course_schema import CreateCourseRequestSchema, CreatedCourseResponseSchema
from api_client.courses.courses_client import CoursesClient, get_private_courses_client
from fixtures.files import FileFixture
from fixtures.users import UserFixture


class CourseFixture(BasePydanticModel):
    request: CreateCourseRequestSchema
    response: CreatedCourseResponseSchema


@pytest.fixture
def courses_client(function_user: UserFixture) -> CoursesClient:
    return get_private_courses_client(function_user.authentication_user)


@pytest.fixture
def function_course(
    courses_client: CoursesClient,
    function_user: UserFixture,
    function_file: FileFixture,
) -> CourseFixture:
    request = CreateCourseRequestSchema(
        previewFileId=function_file.response.file.id,
        createdByUserId=function_user.response.user.id,
    )
    response = courses_client.create_course(request=request)
    return CourseFixture(request=request, response=response)
