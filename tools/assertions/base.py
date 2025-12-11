from typing import Any


def assert_status_code(actual: int, expected: int):
    """
    Проверяет, что фактический статус код ответа соответствует ожидаемому
    :param actual: Фактический статус код
    :param expected: Ожидаемый статус код
    :raises AssertionError: Если статус коды не совпадают
    """
    assert actual == expected, (
        f"Некорректный статус код "
        f"Ожидаемый статус код: {expected} "
        f"Фактический статус код: {actual} "
    )

def assert_equal(actual: Any, expected: Any, name: str):
    """
    Базовый метод проверки фактического значения с ожидаемым
    :param actual: Фактическое значение
    :param expected: Ожидаемое значение
    :param name: Имея проверяемого значения
    :raises AssertionError: Если фактическое значение не равно ожидаемому
    """
    assert actual == expected, (
        f"Некорректное значение {name} "
        f"Ожидаемое значение {actual} "
        f"Фактическое значение {expected} "
    )

def assert_is_true(actual: Any, name: str):
    """
    Проверка, что фактическое значение является истинным
    :param actual: Фактическое значение
    :param name: Название элемента
    :raises AssertionError: Если фактическое значение лож
    """
    assert actual, (
        f"Некорректное значение: {name} "
        f"Ожидалось true но получено false"
    )
