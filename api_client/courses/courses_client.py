from typing import TypedDict

from httpx import Response

from api_client.api_client import APIClient
from api_client.files.files_client import File
from api_client.private_http_builder import AuthenticationUserDict, get_private_http_client
from api_client.users.public_users_client import UserDict


class Course(TypedDict):
    """
    Описание структуры объекта Course
    """
    id: str
    title: str
    maxScore: int
    minScore: int
    description: str
    previewFile: File
    estimatedTime: str
    createdByUser: UserDict


class GetCoursesQueryRequestDict(TypedDict):
    """
    Описание структуры запроса на получение списка курсов.
    """
    userId: str


class CreateCourseRequestDict(TypedDict):
    """
    Описание структуры запроса на создание курса.
    """
    title: str
    maxScore: int | None
    minScore: int | None
    description: str
    estimatedTime: str | None
    previewFileId: str
    createdByUserId: str


class CreatedCourseResponseDict(TypedDict):
    """
    Описание структуры ответа при создании курса
    """
    course: Course


class UpdateCourseRequestDict(TypedDict):
    """
    Описание структуры запроса на обновление курса.
    """
    title: str | None
    maxScore: int | None
    minScore: int | None
    description: str | None
    estimatedTime: str | None


class CoursesClient(APIClient):
    """
    Клиент для работы с /api/v1/courses
    """

    def get_courses_user_api(self, query: GetCoursesQueryRequestDict) -> Response:
        """
        Метод получения списка курсов.
        :param query: Словарь с userId.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(url="api/v1/courses", params=query)

    def create_course_api(self, request: CreateCourseRequestDict) -> Response:
        """
        Метод создания курса
        :param request: Словарь с title, maxScore, minScore, description, estimatedTime,
        previewFileId, createdByUserId.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post(url="api/v1/courses", json=request)

    def get_course_api(self, course_id: str) -> Response:
        """
        Метод получения курса.
        :param course_id: Идентификатор курса.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(url=f"api/v1/courses/{course_id}")

    def update_course_api(self, course_id: str, request: UpdateCourseRequestDict) -> Response:
        """
        Метод обновления курса.
        :param course_id: Идентификатор курса.
        :param request: Словарь с title, maxScore, minScore, description, estimatedTime.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(url=f"api/v1/courses/{course_id}", json=request)

    def delete_course_api(self, course_id: str) -> Response:
        """
        Метод удаления курса.
        :param course_id: Идентификатор курса.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(url=f"api/v1/courses/{course_id}")

    def create_course(self, request: CreateCourseRequestDict) -> CreatedCourseResponseDict:
        """
        Метод создания курса возвращающий объект json
        :param request: Словарь с title, maxScore, minScore, description, estimatedTime,
        previewFileId, createdByUserId.
        :return: Ответ от сервера в виде json
        """
        response = self.create_course_api(request=request)
        return response.json()


def get_private_courses_client(user: AuthenticationUserDict) -> CoursesClient:
    """
    Функция создаёт экземпляр CoursesClient с уже настроенным HTTP-клиентом.
    :return: Готовый к использованию CoursesClient.
    """
    return CoursesClient(client=get_private_http_client(user))
