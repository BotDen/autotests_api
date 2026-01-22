import allure

from api_client.authentication.authentication_schema import LoginResponseSchema
from tools.assertions.base import assert_equal, assert_is_true


@allure.step("Check login response")
def assert_login_response(response: LoginResponseSchema):
    """
    Проверяет корректность ответа при успешной авторизации.
    :param response: Объект ответа с токенами авторизации.
    :raises AssertionError: Если какое-либо из условий не выполняется.
    """
    assert_equal(actual=response.token.token_type, expected="bearer", name="Token type")
    assert_is_true(actual=response.token.access_token, name="Access token")
    assert_is_true(actual=response.token.refresh_token, name="Refresh token")
