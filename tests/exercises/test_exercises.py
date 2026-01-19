from http import HTTPStatus

import pytest

from api_client.errors_schema import InternalErrorResponseSchema
from api_client.exercises.exercise_schema import (
    CreateExerciseRequestSchema,
    CreateExerciseResponseSchema,
    GetExerciseResponseSchema, GetExercisesRequestSchema, GetExercisesResponseSchema,
    UpdateExerciseRequestSchema,
    UpdateExerciseResponseSchema,
)
from api_client.exercises.exercises_client import ExercisesClient
from fixtures.courses import CourseFixture
from fixtures.exercises import ExerciseFixture
from tools.assertions.base import assert_status_code
from tools.assertions.exercises import (
    assert_create_exercise_response,
    assert_exercise_not_found_response,
    assert_get_exercise_response,
    assert_get_exercises_response, assert_update_exercise_response,
)
from tools.assertions.schema import validate_json_schema


@pytest.mark.exercises
@pytest.mark.regression
class TestExercises:
    def test_create_exercise(
        self,
        exercise_client: ExercisesClient,
        function_course: CourseFixture,
    ):
        # 1. Создаем курс в который будем добавлять упражнение
        request = CreateExerciseRequestSchema(courseId=function_course.response.course.id)
        # 2. Создаем упражнение
        response = exercise_client.create_exercise_api(request)
        response_data = CreateExerciseResponseSchema.model_validate_json(response.text)

        # 3. Проверяем статус код ответа 200
        assert_status_code(response.status_code, HTTPStatus.OK)
        # 4. Проверяем данные созданного упражнения с данными запроса
        assert_create_exercise_response(response_data, request)

        # 5. Проверяем соответствие JSON-ответа схеме
        validate_json_schema(response.json(), response_data.model_json_schema())

    def test_get_exercise(
        self,
        exercise_client: ExercisesClient,
        function_exercise: ExerciseFixture,
    ):
        # 2. Запрашиваем упражнения
        response = exercise_client.get_exercise_api(function_exercise.response.exercise.id)
        response_data = GetExerciseResponseSchema.model_validate_json(response.text)

        # 3. Проверяем статус код ответа 200
        assert_status_code(response.status_code, HTTPStatus.OK)
        # 4. Проверяем данные полученных упражнений с данными при создании упражнений
        assert_get_exercise_response(response_data, function_exercise.response)

        # 5. Проверяем соответствие JSON-ответа схеме
        validate_json_schema(response.json(), response_data.model_json_schema())

    def test_update_exercise(
        self,
        exercise_client: ExercisesClient,
        function_exercise: ExerciseFixture,
    ):
        # Генерация данных для обновления
        request = UpdateExerciseRequestSchema()
        # Выполняем запрос на обновление
        response = exercise_client.update_exercise_api(
            exercise_id=function_exercise.response.exercise.id,
            request=request,
        )
        response_data = UpdateExerciseResponseSchema.model_validate_json(response.text)

        # Проверяем статус код ответа 200
        assert_status_code(response.status_code, HTTPStatus.OK)
        # Проверяем соответствие данных обновленного упражнения с исходными данными
        assert_update_exercise_response(response_data, request)

        # Проверяем что JSON-ответ соответствует схеме
        validate_json_schema(response.json(), response_data.model_json_schema())

    def test_delete_exercise(
        self,
        exercise_client: ExercisesClient,
        function_exercise: ExerciseFixture,
    ):
        delete_response = exercise_client.delete_exercise_api(exercise_id=function_exercise.response.exercise.id)

        assert_status_code(delete_response.status_code, HTTPStatus.OK)

        get_response = exercise_client.get_exercise_api(function_exercise.response.exercise.id)
        get_response_data = InternalErrorResponseSchema.model_validate_json(get_response.text)

        assert_status_code(get_response.status_code, HTTPStatus.NOT_FOUND)
        assert_exercise_not_found_response(get_response_data)

        validate_json_schema(get_response.json(), get_response_data.model_json_schema())

    def test_get_exercises(
        self,
        exercise_client: ExercisesClient,
        function_exercise: ExerciseFixture,
    ):
        query = GetExercisesRequestSchema(courseId=function_exercise.response.exercise.course_id)

        response = exercise_client.get_exercises_api(query=query)
        response_data = GetExercisesResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_get_exercises_response(response_data, [function_exercise.response])

        validate_json_schema(response.json(), response_data.model_json_schema())
