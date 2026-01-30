from typing import Self

from pydantic import BaseModel, HttpUrl, FilePath, DirectoryPath
from pydantic_settings import BaseSettings, SettingsConfigDict


class HTTPClientConfig(BaseModel):
    url: HttpUrl
    timeout: float

    @property
    def client_url(self) -> str:
        return str(self.url)


class TestDataConfig(BaseModel):
    image_path: FilePath


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        extra="allow",
        env_file=".env",  # Указываем, из какого файла читать настройки
        env_file_encoding="utf-8",  # Указываем кодировку файла
        env_nested_delimiter=".",  # Указываем разделитель для вложенных переменных
    )

    test_data: TestDataConfig
    http_client: HTTPClientConfig
    allure_results_dir: DirectoryPath  # Добавили новое поле

    # # Добавляем метод инициализации
    # @classmethod
    # def initialize(cls) -> Self:  # Возвращает объект класса Settings
    #     allure_results_dir = DirectoryPath("./allure-results")  # Создаем объект пути к папке
    #     allure_results_dir.mkdir(exist_ok=True)  # Создаем папку allure-results, если она не существует
    #
    #     return Settings(allure_results_dir=allure_results_dir)


settings = Settings()
settings.allure_results_dir.mkdir(exist_ok=True)
print(settings)
