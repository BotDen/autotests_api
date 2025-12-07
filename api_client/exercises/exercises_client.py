from typing import TypedDict

from httpx import Response

from api_client.api_client import APIClient


class ExercisesQueryRequestDict(TypedDict):
    """
    Описание структуры запроса на получение списка упражнений
    """
    courseId: str


class CreateExerciseRequestDict(TypedDict):
    """
    Описание структуры запроса создание упражнения
    """
    title: str
    courseId:  str
    maxScore: int | None
    minScore: int | None
    orderIndex: int | None
    description: str
    estimatedTime: str | None


class UpdateExerciseRequestDict(TypedDict):
    """
    Описание структуры запроса на обновление упражнения
    """
    title: str | None
    maxScore: int | None
    minScore: int | None
    orderIndex: int | None
    description: str | None
    estimatedTime: str | None


class ExercisesClient(APIClient):
    """
    Клиент для работы с api/v1/exercises
    """
    def get_exercises_in_course_api(self, query: ExercisesQueryRequestDict) -> Response:
        """
        Метод получения списка упражнений в курсе
        :param query: ID курса
        :return: Ответ сервера в виде объекта httpx.Response
        """
        return self.get(url="/api/v1/exercises", params=query)

    def create_exercise_api(self, request: CreateExerciseRequestDict) -> Response:
        """
        Метод создания упражнения
        :param request: Словарь с title, courseId, maxScore, minScore, orderIndex, description, estimatedTime
        :return: Ответ сервера в виде объекта httpx.Response
        """
        return self.post(url="/api/v1/exercises", json=request)

    def get_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод получения упражнения
        :param exercise_id: ID упражнения
        :return: Ответ сервера в виде объекта httpx.Response
        """
        return self.get(url=f"/api/v1/exercises/{exercise_id}")

    def update_exercise_api(self, exercise_id: str, request: UpdateExerciseRequestDict) -> Response:
        """
        Метод обновления упражнения
        :param exercise_id: ID упражнения
        :param request: Словарь с title, maxScore, minScore, orderIndex, description, estimatedTime
        :return: Ответ сервера в виде объекта httpx.Response
        """
        return self.patch(url=f"/api/v1/exercises/{exercise_id}", json=request)

    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод удаления упражнения
        :param exercise_id: ID упражнения
        :return: Ответ сервера в виде объекта httpx.Response
        """
        return self.delete(url=f"/api/v1/exercises/{exercise_id}")
