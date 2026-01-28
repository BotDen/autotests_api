import allure

from api_client.users.user_schema import (
    CreateUserRequestSchema,
    CreateUserResponseSchema,
    GetUserResponseSchema,
    UserSchema,
)
from tools.assertions.base import assert_equal
from tools.logger import get_logger


logger = get_logger("USER_ASSERTIONS")


@allure.step("Check create user response")
def assert_create_user_response(request: CreateUserRequestSchema, response: CreateUserResponseSchema):
    """
    Проверка, что ответ на создание пользователя соответствует запросу
    :param request: Исходный запрос на создание пользователя
    :param response: Фактический ответ после создания пользователя
    :raises AssertionError: Если хотя бы одно поле не совпадет
    """
    logger.info("Check create user response")
    assert_equal(actual=response.user.email, expected=request.email, name="email")
    assert_equal(actual=response.user.first_name, expected=request.first_name, name="first_name")
    assert_equal(actual=response.user.last_name, expected=request.last_name, name="last_name")
    assert_equal(actual=response.user.middle_name, expected=request.middle_name, name="middle_name")


@allure.step("Check user")
def assert_user(actual: UserSchema, expected: UserSchema):
    """
    Проверка, что данные созданного пользователя соответствуют входным данным
    :param actual: Фактические данные пользователя
    :param expected: Ожидаемые данные пользователя
    :raises AssertionError: Если хотя бы одно поле не совпало
    """
    logger.info("Check user")
    assert_equal(actual=actual.id, expected=expected.id, name="id")
    assert_equal(actual=actual.email, expected=expected.email, name="email")
    assert_equal(actual=actual.first_name, expected=expected.first_name, name="first_name")
    assert_equal(actual=actual.last_name, expected=expected.last_name, name="last_name")
    assert_equal(actual=actual.middle_name, expected=expected.middle_name, name="middle_name")


@allure.step("Check get user response")
def assert_get_user_response(
    get_user_response: GetUserResponseSchema,
    create_user_response: CreateUserResponseSchema,
):
    """
    Проверка, что ответ на получение пользователя корректный
    :param get_user_response: Ответ полученные на запрос пользователя
    :param create_user_response: Ответ полученные при создании пользователя
    :return:
    """
    logger.info("Check get user response")
    assert_user(actual=get_user_response.user, expected=create_user_response.user)
