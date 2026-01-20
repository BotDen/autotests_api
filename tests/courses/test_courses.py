from http import HTTPStatus

import allure
import pytest

from api_client.courses.course_schema import (
    CreateCourseRequestSchema,
    CreatedCourseResponseSchema,
    GetCoursesQueryRequestSchema,
    GetCoursesResponseSchema,
    UpdateCourseRequestSchema,
    UpdateCourseResponseSchema,
)
from api_client.courses.courses_client import CoursesClient
from fixtures.courses import CourseFixture
from fixtures.files import FileFixture
from fixtures.users import UserFixture
from tools.allure.epic import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.tags import AllureTag
from tools.assertions.base import assert_status_code
from tools.assertions.courses import (
    assert_create_course_response,
    assert_get_courses_response,
    assert_update_course_response,
)
from tools.assertions.schema import validate_json_schema


@pytest.mark.courses
@pytest.mark.regression
@allure.epic(AllureEpic.ADMINISTRATION)
@allure.feature(AllureFeature.COURSES)
class TestCourses:
    @allure.title("Update course")
    @allure.tag(AllureTag.UPDATE_ENTITY)
    def test_update_course(self, courses_client: CoursesClient, function_course: CourseFixture):
        # Формируем данные для обновления
        request = UpdateCourseRequestSchema()
        # Отправляем запрос на обновление курса
        response = courses_client.update_course_api(course_id=function_course.response.course.id, request=request)
        # Преобразуем JSON-ответ в объект схемы
        response_data = UpdateCourseResponseSchema.model_validate_json(response.text)

        # Проверяем статус код ответа
        assert_status_code(response.status_code, HTTPStatus.OK)
        # Проверяем, что данные в ответе соответствуют запросу
        assert_update_course_response(request, response_data)

        # Валидация json схемы ответа
        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.title("Get courses")
    @allure.tag(AllureTag.GET_ENTITY)
    def test_get_courses(
        self,
        courses_client: CoursesClient,
        function_course: CourseFixture,
        function_user: UserFixture,
    ):
        # Формируем параметры запроса, передавая user_id
        query = GetCoursesQueryRequestSchema(user_id=function_user.response.user.id)
        # Отправляем запрос на получение списка курсов
        response = courses_client.get_courses_user_api(query)
        # Десериализуем JSON-ответ в Pydantic-модель
        response_data = GetCoursesResponseSchema.model_validate_json(response.text)

        # Проверяем, что код ответа 200 OK
        assert_status_code(response.status_code, HTTPStatus.OK)
        # Проверяем, что список курсов соответствует ранее созданным курсам
        assert_get_courses_response(response_data, [function_course.response])

        # Проверяем соответствие JSON-ответ схеме
        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.title("Create course")
    @allure.tag(AllureTag.CREATE_ENTITY)
    def test_create_course(
        self,
        courses_client: CoursesClient,
        function_user: UserFixture,
        function_file: FileFixture,
    ):
        request = CreateCourseRequestSchema(
            previewFileId=function_file.response.file.id,
            createdByUserId=function_user.response.user.id,
        )
        response = courses_client.create_course_api(request)
        response_data = CreatedCourseResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_create_course_response(response_data, request)

        validate_json_schema(response.json(), response_data.model_json_schema())
