from typing import Any, Sized

import allure

from tools.logger import get_logger


logger = get_logger("BASE_ASSERTIONS")


@allure.step("Check that response status code equals expected {expected}")
def assert_status_code(actual: int, expected: int):
    """
    Проверяет, что фактический статус код ответа соответствует ожидаемому
    :param actual: Фактический статус код
    :param expected: Ожидаемый статус код
    :raises AssertionError: Если статус коды не совпадают
    """
    logger.info(f"Check that response status code equals expected {expected}")
    assert actual == expected, (
        f"Некорректный статус код "
        f"Ожидаемый статус код: {expected} "
        f"Фактический статус код: {actual} "
    )


@allure.step("Check that {name} equals expected {expected}")
def assert_equal(actual: Any, expected: Any, name: str):
    """
    Базовый метод проверки фактического значения с ожидаемым
    :param actual: Фактическое значение
    :param expected: Ожидаемое значение
    :param name: Имея проверяемого значения
    :raises AssertionError: Если фактическое значение не равно ожидаемому
    """
    logger.info(f"Check that '{name}' equals expected {expected}")
    assert actual == expected, (
        f"Некорректное значение {name} "
        f"Ожидаемое значение {actual} "
        f"Фактическое значение {expected} "
    )


@allure.step("Check that {name} is True")
def assert_is_true(actual: Any, name: str):
    """
    Проверка, что фактическое значение является истинным
    :param actual: Фактическое значение
    :param name: Название элемента
    :raises AssertionError: Если фактическое значение лож
    """
    logger.info(f"Check that '{name}' is True")
    assert actual, (
        f"Некорректное значение: {name} "
        f"Ожидалось true но получено false"
    )


def assert_lens(actual: Sized, expected: Sized, name: str):
    """
    Проверяет, что длины двух объектов совпадают.

    :param name: Название проверяемого объекта.
    :param actual: Фактический объект.
    :param expected: Ожидаемый объект.
    :raises AssertionError: Если длины не совпадают.
    """
    with allure.step(f"Check that lens of {name} equals to {len(expected)}"):
        logger.info(f"Check that lens of '{name}' equals to {len(expected)}")
        assert len(actual) == len(expected), (
            f"Некорректная длина объекта {name} "
            f"Фактическая длина объекта: {len(actual)} "
            f"Ожидаемая длина объекта: {len(expected)} "
        )
