from httpx import Response

from api_client.api_client import APIClient
from api_client.exercises.exercise_schema import (
    CreateExerciseRequestSchema,
    ExerciseResponseSchema,
    ExercisesQueryRequestSchema,
    UpdateExerciseRequestSchema,
)
from api_client.private_http_builder import AuthenticationUserSchema, get_private_http_client


class ExercisesClient(APIClient):
    """
    Клиент для работы с api/v1/exercises
    """
    def get_exercises_api(self, query: ExercisesQueryRequestSchema) -> Response:
        """
        Метод получения списка упражнений в курсе
        :param query: ID курса
        :return: Ответ сервера в виде объекта httpx.Response
        """
        return self.get(url="/api/v1/exercises", params=query.model_dump(by_alias=True))

    def create_exercise_api(self, request: CreateExerciseRequestSchema) -> Response:
        """
        Метод создания упражнения
        :param request: Словарь с title, courseId, maxScore, minScore, orderIndex, description, estimatedTime
        :return: Ответ сервера в виде объекта httpx.Response
        """
        return self.post(url="/api/v1/exercises", json=request.model_dump(by_alias=True))

    def get_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод получения упражнения
        :param exercise_id: ID упражнения
        :return: Ответ сервера в виде объекта httpx.Response
        """
        return self.get(url=f"/api/v1/exercises/{exercise_id}")

    def update_exercise_api(self, exercise_id: str, request: UpdateExerciseRequestSchema) -> Response:
        """
        Метод обновления упражнения
        :param exercise_id: ID упражнения
        :param request: Словарь с title, maxScore, minScore, orderIndex, description, estimatedTime
        :return: Ответ сервера в виде объекта httpx.Response
        """
        return self.patch(url=f"/api/v1/exercises/{exercise_id}", json=request.model_dump(by_alias=True))

    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод удаления упражнения
        :param exercise_id: ID упражнения
        :return: Ответ сервера в виде объекта httpx.Response
        """
        return self.delete(url=f"/api/v1/exercises/{exercise_id}")

    def get_exercises(self, request: ExercisesQueryRequestSchema) -> ExerciseResponseSchema:
        """
        Метод получения упражнений с возвратом объекта в виде json
        :param request: ID курса
        :return: Ответ от сервера в виде json объекта
        """
        response = self.get_exercises_api(request)
        return ExerciseResponseSchema.model_validate_json(response.text)

    def get_exercise(self, exercise_id: str) -> ExerciseResponseSchema:
        """
        Метод получения упражнения с возвратом объекта в виде json
        :param exercise_id: ID упражнения
        :return: Ответ от сервера в виде json объекта
        """
        response = self.get_exercise_api(exercise_id)
        return ExerciseResponseSchema.model_validate_json(response.text)

    def create_exercise(self, request: CreateExerciseRequestSchema) -> ExerciseResponseSchema:
        """
        Метод создания упражнения с возвратом объекта в виде json
        :param request: Словарь с title, courseId, maxScore, minScore, orderIndex, description, estimatedTime
        :return: Ответ от сервера в виде json объекта
        """
        response = self.create_exercise_api(request)
        return ExerciseResponseSchema.model_validate_json(response.text)

    def update_exercise(self, exercise_id: str, request: UpdateExerciseRequestSchema) -> ExerciseResponseSchema:
        """
        Метод обновления упражнения с возвратом объекта в виде json
        :param exercise_id: ID упражнения
        :param request: Словарь с title, courseId, maxScore, minScore, orderIndex, description, estimatedTime
        :return: Ответ от сервера в виде json объекта
        """
        response = self.update_exercise_api(exercise_id, request)
        return ExerciseResponseSchema.model_validate_json(response.text)


def get_private_exercises_client(user: AuthenticationUserSchema) -> ExercisesClient:
    """
    Функция создаёт экземпляр ExercisesClient с уже настроенным HTTP-клиентом.
    :return: Готовый к использованию ExercisesClient.
    """
    return ExercisesClient(client=get_private_http_client(user))
