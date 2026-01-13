from typing import Any

from pydantic import Field

from api_client.base_pydantic_model import BasePydanticModel


class ValidationErrorSchema(BasePydanticModel):
    """
    Модель, описывающая структуру ошибки валидации API.
    """
    type: str
    input: Any
    context: dict[str, Any] = Field(alias="ctx")
    message: str = Field(alias="msg")
    location: list[str] = Field(alias="loc")


class ValidationErrorResponseSchema(BasePydanticModel):
    """
    Модель, описывающая структуру ответа API с ошибкой валидации.
    """
    details: list[ValidationErrorSchema] = Field(alias="detail")


class InternalErrorResponseSchema(BasePydanticModel):
    """
    Модель для описания внутренней ошибки
    """
    details: str = Field(alias="detail")
