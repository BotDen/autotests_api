from api_client.errors_schema import InternalErrorResponseSchema
from api_client.exercises.exercise_schema import (
    CreateExerciseRequestSchema,
    CreateExerciseResponseSchema,
    ExerciseSchema,
    GetExerciseResponseSchema, GetExercisesResponseSchema,
    UpdateExerciseRequestSchema,
    UpdateExerciseResponseSchema,
)
from tools.assertions.base import assert_equal, assert_lens
from tools.assertions.errors import assert_internal_error_response


def assert_exercise(actual: ExerciseSchema, expected: ExerciseSchema):
    """
    Проверка, что фактические данные упражнения соответствуют ожидаемым
    :param actual: Фактические данные упражнения
    :param expected: Ожидаемые данные упражнения
    :return AssertionError: Если хотя бы одно поле не совпало
    """
    assert_equal(actual.title, expected.title, "title")
    assert_equal(actual.course_id, expected.course_id, "course_id")
    assert_equal(actual.max_score, expected.max_score, "max_score")
    assert_equal(actual.min_score, expected.min_score, "min_score")
    assert_equal(actual.order_index, expected.order_index, "order_index")
    assert_equal(actual.description, expected.description, "description")
    assert_equal(actual.estimated_time, expected.estimated_time, "estimated_time")


def assert_create_exercise_response(
    response: CreateExerciseResponseSchema,
    request: CreateExerciseRequestSchema,
):
    """
    Проверяет, что ответ на создание упражнения соответствует запросу
    :param response: Ответ API с данными созданного упражнения
    :param request: Исходный запрос на создание упражнения
    :return AssertionError: Если хотя бы одно поле не соответствует
    """
    assert_equal(response.exercise.title, request.title, "title")
    assert_equal(response.exercise.course_id, request.course_id, "course_id")
    assert_equal(response.exercise.max_score, request.max_score, "max_score")
    assert_equal(response.exercise.min_score, request.min_score, "min_score")
    assert_equal(response.exercise.description, request.description, "description")
    assert_equal(response.exercise.estimated_time, request.estimated_time, "estimated_time")
    assert_equal(response.exercise.order_index, request.order_index, "order_index")


def assert_get_exercises_response(
    get_exercises_response: GetExercisesResponseSchema,
    create_exercises_response: list[CreateExerciseResponseSchema],
):
    """
    Проверка, что ответ на получение упражнений соответствует ответу на их создание
    :param get_exercises_response: Ответ API при запросе списка упражнений
    :param create_exercises_response: Список API ответов при создании упражнений
    :return AssertionError: Если данные упражнения не совпадают
    """
    assert_lens(get_exercises_response.exercises, create_exercises_response, "exercises")

    for index, create_exercises_response in enumerate(create_exercises_response):
        assert_exercise(get_exercises_response.exercises[index], create_exercises_response.exercise)


def assert_get_exercise_response(
    get_exercise_response: GetExerciseResponseSchema,
    create_exercises_response: CreateExerciseResponseSchema,
):
    """
    Проверка, что ответ на получение упражнений соответствует ответу на их создание
    :param get_exercise_response: Ответ API при запросе списка упражнений
    :param create_exercises_response: Список API ответов при создании упражнений
    :return AssertionError: Если данные упражнения не совпадают
    """
    assert_exercise(get_exercise_response.exercise, create_exercises_response.exercise)


def assert_update_exercise_response(
    response: UpdateExerciseResponseSchema,
    request: UpdateExerciseRequestSchema,
):
    """
    Проверка, что ответа на обновление упражнения соответствует запросу
    :param response: Ответ API после обновления упражнения
    :param request: Исходный запрос на обновление упражнения
    :return AssertionError: Если хотя бы одно поле не совпало
    """
    assert_equal(response.exercise.title, request.title, "title")
    assert_equal(response.exercise.max_score, request.max_score, "max_score")
    assert_equal(response.exercise.min_score, request.min_score, "min_score")
    assert_equal(response.exercise.order_index, request.order_index, "order_index")
    assert_equal(response.exercise.description, request.description, "description")
    assert_equal(response.exercise.estimated_time, request.estimated_time, "estimated_time")

def assert_exercise_not_found_response(actual: InternalErrorResponseSchema):
    """
    Функция для проверки ошибки, если упражнение не найдено на сервере
    :param actual: Фактический ответ от сервера
    :return AssertionError: Если фактический ответ не соответствует "Exercise not found"
    """
    expected = InternalErrorResponseSchema(detail="Exercise not found")
    assert_internal_error_response(actual, expected)
