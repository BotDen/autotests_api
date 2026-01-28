import allure

from httpx import Request, Response

from tools.logger import get_logger
from tools.http.curl import make_curl_from_request


# Инициализируем логгер один раз на весь модуль
logger = get_logger("HTTP_CLIENT")


def curl_event_hooks(request: Request):
    """
    Event hook для автоматического прикрепления cURL команды к Allure отчету
    :param request: HTTP запрос переданный в httpx клиент
    """
    # Генерируем команду cURL из объекта запроса
    curl_command = make_curl_from_request(request)

    # Прикрепляем сгенерированную cURL команду к отчету Allure
    allure.attach(
        body=curl_command,
        name="cURL_command",
        attachment_type=allure.attachment_type.TEXT,
    )


def log_request_event_hook(request: Request):
    """
    Event hook для автоматического логирования запроса
    :param request: HTTP запрос переданный в httpx клиент
    """
    # Пишем в лог информационное сообщение о запроса
    logger.info(f"Make {request.method} request to {request.url}")


def log_response_event_hook(response: Response):
    """
    Event hook для автоматического логирования ответа
    :param response: HTTP ответ переданный в httpx клиент
    """
    # Пишем в лог информационное сообщение об ответе
    logger.info(f"Got response {response.status_code} {response.reason_phrase} from {response.url}")
