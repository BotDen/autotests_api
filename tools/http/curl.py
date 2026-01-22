from httpx import Request, RequestNotRead


def make_curl_from_request(request: Request) -> str:
    """
    Функция по формированию cURL запроса из http запроса
    :param request: HTTP запрос из которого будет формироваться cURL
    :return: Строка cURL запросом, содержит метод запроса, URL, заголовки и тело (если есть)
    """
    # Создаем список с основной командой cURL, включая метод и URL
    result: list[str] = [f"curl -X '{request.method}'", f"'{request.url}'"]

    # Добавляем заголовки в формате -H "Header: Value"
    for header, value in request.headers.items():
        result.append(f"-H '{header}: {value}'")

    # Добавляем тело запроса, если оно есть
    try:
        if body := request.content:
            result.append(f"-d '{body.decode("utf-8")}'")
    except RequestNotRead:
        pass

    # Объединяем части с переносом строк, исключая завершающий '\'
    return "\\\n".join(result)
