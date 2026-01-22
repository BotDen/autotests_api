import allure

from httpx import Request

from tools.http.curl import make_curl_from_request


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
        attachment_type=allure.attachment_type.TEXT
    )
