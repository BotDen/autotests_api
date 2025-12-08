from typing import TypedDict

from httpx import Response

from api_client.api_client import APIClient
from api_client.private_http_builder import AuthenticationUserDict, get_private_http_client


class Exercise(TypedDict):
    """
    Описание структуры объекта Exercise
    """
    id: str
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str


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


class ExerciseResponseDict(TypedDict):
    """
    Описание структуры ответа при создании упражнения
    """
    exercise: list[Exercise]


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
    def get_exercises_api(self, query: ExercisesQueryRequestDict) -> Response:
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

    def get_exercises(self, request: ExercisesQueryRequestDict) -> ExerciseResponseDict:
        """
        Метод получения упражнений с возвратом объекта в виде json
        :param request: ID курса
        :return: Ответ от сервера в виде json объекта
        """
        response = self.get_exercises_api(request)
        return response.json()

    def get_exercise(self, exercise_id: str) -> ExerciseResponseDict:
        """
        Метод получения упражнения с возвратом объекта в виде json
        :param exercise_id: ID упражнения
        :return: Ответ от сервера в виде json объекта
        """
        response = self.get_exercise_api(exercise_id)
        return response.json()

    def create_exercise(self, request: CreateExerciseRequestDict) -> ExerciseResponseDict:
        """
        Метод создания упражнения с возвратом объекта в виде json
        :param request: Словарь с title, courseId, maxScore, minScore, orderIndex, description, estimatedTime
        :return: Ответ от сервера в виде json объекта
        """
        response = self.create_exercise_api(request)
        return response.json()

    def update_exercise(self, exercise_id: str, request: UpdateExerciseRequestDict) -> ExerciseResponseDict:
        """
        Метод обновления упражнения с возвратом объекта в виде json
        :param exercise_id: ID упражнения
        :param request: Словарь с title, courseId, maxScore, minScore, orderIndex, description, estimatedTime
        :return: Ответ от сервера в виде json объекта
        """
        response = self.update_exercise_api(exercise_id, request)
        return response.json()


def get_private_exercises_client(user: AuthenticationUserDict) -> ExercisesClient:
    """
    Функция создаёт экземпляр ExercisesClient с уже настроенным HTTP-клиентом.
    :return: Готовый к использованию ExercisesClient.
    """
    return ExercisesClient(client=get_private_http_client(user))
