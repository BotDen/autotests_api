import allure
from httpx import Response

from api_client.api_client import APIClient
from api_client.courses.course_schema import (
    CreateCourseRequestSchema,
    CreatedCourseResponseSchema,
    GetCoursesQueryRequestSchema,
    UpdateCourseRequestSchema,
)
from api_client.private_http_builder import AuthenticationUserSchema, get_private_http_client
from tools.routes import APIRoutes


class CoursesClient(APIClient):
    """
    Клиент для работы с /api/v1/courses
    """

    @allure.step("Get courses")
    def get_courses_user_api(self, query: GetCoursesQueryRequestSchema) -> Response:
        """
        Метод получения списка курсов.
        :param query: Словарь с userId.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(url=f"{APIRoutes.COURSES}", params=query.model_dump(by_alias=True))

    @allure.step("Get course by course_id {course_id}")
    def get_course_api(self, course_id: str) -> Response:
        """
        Метод получения курса.
        :param course_id: Идентификатор курса.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(url=f"{APIRoutes.COURSES}/{course_id}")

    @allure.step("Get new course")
    def create_course_api(self, request: CreateCourseRequestSchema) -> Response:
        """
        Метод создания курса
        :param request: Словарь с title, maxScore, minScore, description, estimatedTime,
        previewFileId, createdByUserId.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post(url=f"{APIRoutes.COURSES}", json=request.model_dump(by_alias=True))

    @allure.step("Update course by course_id {course_id}")
    def update_course_api(self, course_id: str, request: UpdateCourseRequestSchema) -> Response:
        """
        Метод обновления курса.
        :param course_id: Идентификатор курса.
        :param request: Словарь с title, maxScore, minScore, description, estimatedTime.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(url=f"{APIRoutes.COURSES}/{course_id}", json=request.model_dump(by_alias=True))

    @allure.step("Delete course by course_id {course_id}")
    def delete_course_api(self, course_id: str) -> Response:
        """
        Метод удаления курса.
        :param course_id: Идентификатор курса.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(url=f"{APIRoutes.COURSES}/{course_id}")

    def create_course(self, request: CreateCourseRequestSchema) -> CreatedCourseResponseSchema:
        """
        Метод создания курса возвращающий объект json
        :param request: Словарь с title, maxScore, minScore, description, estimatedTime,
        previewFileId, createdByUserId.
        :return: Ответ от сервера в виде json
        """
        response = self.create_course_api(request=request)
        return CreatedCourseResponseSchema.model_validate_json(response.text)


def get_private_courses_client(user: AuthenticationUserSchema) -> CoursesClient:
    """
    Функция создаёт экземпляр CoursesClient с уже настроенным HTTP-клиентом.
    :return: Готовый к использованию CoursesClient.
    """
    return CoursesClient(client=get_private_http_client(user))
