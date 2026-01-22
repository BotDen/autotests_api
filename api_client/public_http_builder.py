from httpx import Client

from api_client.event_hooks import curl_event_hooks


def get_public_http_client() -> Client:
    """
    Функция создает экземпляр httpx.Client с базовыми настройками
    :return: Готовый к использованию объект httpx.Client
    """
    return Client(
        timeout=5,
        base_url="http://localhost:8000",
        event_hooks={"request": [curl_event_hooks]},
    )
