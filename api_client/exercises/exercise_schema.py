from pydantic import Field

from api_client.base_pydantic_model import BasePydanticModel
from tools.fakers import fake


class ExerciseSchema(BasePydanticModel):
    """
    Описание структуры объекта Exercise
    """
    id: str
    title: str
    course_id: str = Field(alias="courseId")
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    order_index: int = Field(alias="orderIndex")
    description: str
    estimated_time: str = Field(alias="estimatedTime")


class GetExercisesRequestSchema(BasePydanticModel):
    """
    Описание структуры запроса на получение списка упражнений
    """
    course_id: str = Field(alias="courseId")


class CreateExerciseRequestSchema(BasePydanticModel):
    """
    Описание структуры запроса создание упражнения
    """
    title: str = Field(default_factory=fake.get_sentence)
    course_id:  str = Field(alias="courseId")
    max_score: int | None = Field(alias="maxScore", default_factory=fake.get_max_score)
    min_score: int | None = Field(alias="minScore", default_factory=fake.get_min_score)
    order_index: int | None = Field(alias="orderIndex", default_factory=fake.get_integer)
    description: str = Field(default_factory=fake.get_text)
    estimated_time: str | None = Field(alias="estimatedTime", default_factory=fake.get_estimated_time)


class CreateExerciseResponseSchema(BasePydanticModel):
    """
    Описание структуры ответа при создании упражнения
    """
    exercise: ExerciseSchema


class UpdateExerciseRequestSchema(BasePydanticModel):
    """
    Описание структуры запроса на обновление упражнения
    """
    title: str | None = Field(default_factory=fake.get_sentence)
    max_score: int | None = Field(alias="maxScore", default_factory=fake.get_max_score)
    min_score: int | None = Field(alias="minScore", default_factory=fake.get_min_score)
    order_index: int | None = Field(alias="orderIndex", default_factory=fake.get_integer)
    description: str | None = Field(default_factory=fake.get_text)
    estimated_time: str | None = Field(alias="estimatedTime", default_factory=fake.get_estimated_time)


class UpdateExerciseResponseSchema(BasePydanticModel):
    """
    Описание структуры ответа на обновление упражнения
    """
    exercise: ExerciseSchema


class GetExercisesResponseSchema(BasePydanticModel):
    """
    Описание структуры ответа на запрос упражнений
    """
    exercises: list[ExerciseSchema]
