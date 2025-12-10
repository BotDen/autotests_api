from pydantic import BaseModel, ConfigDict


class BasePydanticModel(BaseModel):
    """
    Базовая модель для генерации моделей pydantic в проекте
    """
    model_config = ConfigDict(populate_by_name=True)
