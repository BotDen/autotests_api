from pydantic import Field

from api_client.base_pydantic_model import BasePydanticModel


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


class ExercisesQueryRequestSchema(BasePydanticModel):
    """
    Описание структуры запроса на получение списка упражнений
    """
    course_id: str = Field(alias="courseId")


class CreateExerciseRequestSchema(BasePydanticModel):
    """
    Описание структуры запроса создание упражнения
    """
    title: str
    course_id:  str = Field(alias="courseId")
    max_score: int | None = Field(alias="maxScore")
    min_score: int | None = Field(alias="minScore")
    order_index: int | None = Field(alias="orderIndex")
    description: str
    estimated_time: str | None = Field(alias="estimatedTime")


class ExerciseResponseSchema(BasePydanticModel):
    """
    Описание структуры ответа при создании упражнения
    """
    exercise: list[ExerciseSchema]


class UpdateExerciseRequestSchema(BasePydanticModel):
    """
    Описание структуры запроса на обновление упражнения
    """
    title: str | None
    max_score: int | None = Field(alias="maxScore")
    min_score: int | None = Field(alias="minScore")
    order_index: int | None = Field(alias="orderIndex")
    description: str | None
    estimated_time: str | None = Field(alias="estimatedTime")
