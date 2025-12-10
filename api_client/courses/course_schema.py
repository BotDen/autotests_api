from pydantic import Field

from api_client.base_pydantic_model import BasePydanticModel
from api_client.files.file_schema import FileSchema
from api_client.users.user_schema import UserSchema


class CourseSchema(BasePydanticModel):
    """
    Описание структуры объекта Course
    """
    id: str
    title: str
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    description: str
    preview_file: FileSchema = Field(alias="previewFile")
    estimated_time: str = Field(alias="estimatedTime")
    created_by_user: UserSchema = Field(alias="createdByUser")


class GetCoursesQueryRequestSchema(BasePydanticModel):
    """
    Описание структуры запроса на получение списка курсов.
    """
    user_id: str = Field(alias="userId")


class CreateCourseRequestSchema(BasePydanticModel):
    """
    Описание структуры запроса на создание курса.
    """
    title: str
    max_score: int | None = Field(alias="maxScore")
    min_score: int | None = Field(alias="minScore")
    description: str
    estimated_time: str | None = Field(alias="estimatedTime")
    preview_file_id: str = Field(alias="previewFileId")
    created_by_user_id: str = Field(alias="createdByUserId")


class CreatedCourseResponseSchema(BasePydanticModel):
    """
    Описание структуры ответа при создании курса
    """
    course: CourseSchema


class UpdateCourseRequestSchema(BasePydanticModel):
    """
    Описание структуры запроса на обновление курса.
    """
    title: str | None
    max_score: int | None = Field(alias="maxScore")
    min_score: int | None = Field(alias="minScore")
    description: str | None
    estimated_time: str | None = Field(alias="estimatedTime")
