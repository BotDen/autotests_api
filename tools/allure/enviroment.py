import platform
import sys

from config import settings


def create_allure_environment_file():
    # Создаем список из элементов в формате key=value
    items = [f"{key}={value}" for key, value in settings.model_dump().items()]
    items.append(f"os_info={platform.system()}, {platform.release()}")
    items.append(f"python={sys.version}")
    # Собираем все элементы в единую строку с переносом
    properties = "\n".join(items)

    # Открываем файл ./allure-results/environment.properties на запись
    with open(
        settings.allure_results_dir.joinpath("environment.properties"), "w+"
    ) as file:  # w+ запись файла, если нет такого то будет создан новый
        file.write(properties)
