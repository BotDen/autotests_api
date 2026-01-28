import pytest

from tools.allure.enviroment import create_allure_environment_file


@pytest.fixture(scope="session", autouse=True)
def save_allure_environment_file():
    # До начало автотестов ни чего не делаем
    yield
    # После завершения автотестов создаем файл environment.properties
    create_allure_environment_file()
