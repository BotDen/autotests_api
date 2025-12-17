import pytest

from api_client.base_pydantic_model import BasePydanticModel
from api_client.exercises.exercise_schema import CreateExerciseRequestSchema, CreateExerciseResponseSchema
from api_client.exercises.exercises_client import ExercisesClient, get_private_exercises_client
from fixtures.courses import CourseFixture
from fixtures.users import UserFixture


class ExerciseFixture(BasePydanticModel):
    request: CreateExerciseRequestSchema
    response: CreateExerciseResponseSchema


@pytest.fixture
def exercise_client(function_user: UserFixture) -> ExercisesClient:
    return get_private_exercises_client(function_user.authentication_user)


@pytest.fixture
def function_exercise(function_course: CourseFixture, exercise_client: ExercisesClient) -> ExerciseFixture:
    request = CreateExerciseRequestSchema(courseId=function_course.response.course.id, orderIndex=1)
    response = exercise_client.create_exercise(request)
    return ExerciseFixture(request=request, response=response)
