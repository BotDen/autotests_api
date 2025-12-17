from api_client.users.user_schema import (
    CreateUserRequestSchema, CreateUserResponseSchema, GetUserResponseSchema,
    UserSchema,
)
from tools.assertions.base import assert_equal


def assert_create_user_response(request: CreateUserRequestSchema, response: CreateUserResponseSchema):
    """
    Проверка, что ответ на создание пользователя соответствует запросу
    :param request: Исходный запрос на создание пользователя
    :param response: Фактический ответ после создания пользователя
    :raises AssertionError: Если хотя бы одно поле не совпадет
    """
    assert_equal(actual=response.user.email, expected=request.email, name="email")
    assert_equal(actual=response.user.first_name, expected=request.first_name, name="first_name")
    assert_equal(actual=response.user.last_name, expected=request.last_name, name="last_name")
    assert_equal(actual=response.user.middle_name, expected=request.middle_name, name="middle_name")

def assert_user(actual: UserSchema, expected: UserSchema):
    """

    :param actual:
    :param expected:
    :raises AssertionError:
    """
    assert_equal(actual=actual.id, expected=expected.id, name="id")
    assert_equal(actual=actual.email, expected=expected.email, name="email")
    assert_equal(actual=actual.first_name, expected=expected.first_name, name="first_name")
    assert_equal(actual=actual.last_name, expected=expected.last_name, name="last_name")
    assert_equal(actual=actual.middle_name, expected=expected.middle_name, name="middle_name")

def assert_get_user_response(
    get_user_response: GetUserResponseSchema,
    create_user_response: CreateUserResponseSchema
):
    assert_user(actual=get_user_response.user, expected=create_user_response.user)
