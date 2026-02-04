import allure
from httpx import Response

from api_client.api_client import APIClient
from api_client.api_coverage import tracker
from api_client.exercises.exercise_schema import (
    CreateExerciseRequestSchema,
    CreateExerciseResponseSchema,
    GetExercisesRequestSchema,
    UpdateExerciseRequestSchema,
)
from api_client.private_http_builder import AuthenticationUserSchema, get_private_http_client
from tools.routes import APIRoutes


class ExercisesClient(APIClient):
    """
    Клиент для работы с api/v1/exercises
    """

    @allure.step("Get exercises")
    @tracker.track_coverage_httpx(f"{APIRoutes.EXERCISES}")
    def get_exercises_api(self, query: GetExercisesRequestSchema) -> Response:
        """
        Метод получения списка упражнений в курсе
        :param query: ID курса
        :return: Ответ сервера в виде объекта httpx.Response
        """
        return self.get(url=f"{APIRoutes.EXERCISES}", params=query.model_dump(by_alias=True))

    @allure.step("Create new exercise")
    @tracker.track_coverage_httpx(f"{APIRoutes.EXERCISES}")
    def create_exercise_api(self, request: CreateExerciseRequestSchema) -> Response:
        """
        Метод создания упражнения
        :param request: Словарь с title, courseId, maxScore, minScore, orderIndex, description, estimatedTime
        :return: Ответ сервера в виде объекта httpx.Response
        """
        return self.post(url=f"{APIRoutes.EXERCISES}", json=request.model_dump(by_alias=True))

    @allure.step("Get exercise by exercise_id {exercise_id}")
    @tracker.track_coverage_httpx(f"{APIRoutes.EXERCISES}/{{exercise_id}}")
    def get_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод получения упражнения
        :param exercise_id: ID упражнения
        :return: Ответ сервера в виде объекта httpx.Response
        """
        return self.get(url=f"{APIRoutes.EXERCISES}/{exercise_id}")

    @allure.step("Update exercise by exercise_id {exercise_id}")
    @tracker.track_coverage_httpx(f"{APIRoutes.EXERCISES}/{{exercise_id}}")
    def update_exercise_api(self, exercise_id: str, request: UpdateExerciseRequestSchema) -> Response:
        """
        Метод обновления упражнения
        :param exercise_id: ID упражнения
        :param request: Словарь с title, maxScore, minScore, orderIndex, description, estimatedTime
        :return: Ответ сервера в виде объекта httpx.Response
        """
        return self.patch(url=f"{APIRoutes.EXERCISES}/{exercise_id}", json=request.model_dump(by_alias=True))

    @allure.step("Delete exercise by exercise_id {exercise_id}")
    @tracker.track_coverage_httpx(f"{APIRoutes.EXERCISES}/{{exercise_id}}")
    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод удаления упражнения
        :param exercise_id: ID упражнения
        :return: Ответ сервера в виде объекта httpx.Response
        """
        return self.delete(url=f"{APIRoutes.EXERCISES}/{exercise_id}")

    def get_exercises(self, request: GetExercisesRequestSchema) -> CreateExerciseResponseSchema:
        """
        Метод получения упражнений с возвратом объекта в виде json
        :param request: ID курса
        :return: Ответ от сервера в виде json объекта
        """
        response = self.get_exercises_api(request)
        return CreateExerciseResponseSchema.model_validate_json(response.text)

    def get_exercise(self, exercise_id: str) -> CreateExerciseResponseSchema:
        """
        Метод получения упражнения с возвратом объекта в виде json
        :param exercise_id: ID упражнения
        :return: Ответ от сервера в виде json объекта
        """
        response = self.get_exercise_api(exercise_id)
        return CreateExerciseResponseSchema.model_validate_json(response.text)

    def create_exercise(self, request: CreateExerciseRequestSchema) -> CreateExerciseResponseSchema:
        """
        Метод создания упражнения с возвратом объекта в виде json
        :param request: Словарь с title, courseId, maxScore, minScore, orderIndex, description, estimatedTime
        :return: Ответ от сервера в виде json объекта
        """
        response = self.create_exercise_api(request)
        return CreateExerciseResponseSchema.model_validate_json(response.text)

    def update_exercise(self, exercise_id: str, request: UpdateExerciseRequestSchema) -> CreateExerciseResponseSchema:
        """
        Метод обновления упражнения с возвратом объекта в виде json
        :param exercise_id: ID упражнения
        :param request: Словарь с title, courseId, maxScore, minScore, orderIndex, description, estimatedTime
        :return: Ответ от сервера в виде json объекта
        """
        response = self.update_exercise_api(exercise_id, request)
        return CreateExerciseResponseSchema.model_validate_json(response.text)


def get_private_exercises_client(user: AuthenticationUserSchema) -> ExercisesClient:
    """
    Функция создаёт экземпляр ExercisesClient с уже настроенным HTTP-клиентом.
    :return: Готовый к использованию ExercisesClient.
    """
    return ExercisesClient(client=get_private_http_client(user))
