import logging


def get_logger(name: str) -> logging.Logger:
    # Инициализация логгера с указанием имени
    logger = logging.getLogger(name)
    # Устанавливаем уровень логирования для логгера DEBUG, чтобы он обрабатывал все сообщения
    logger.setLevel(logging.DEBUG)

    # Создаем обработчик, который будет выводить логи в консоль
    handler = logging.StreamHandler()
    # Устанавливаем уровень логирования для обработчика DEBUG, чтобы он обрабатывал все сообщения
    handler.setLevel(logging.DEBUG)

    # Задаем форматирование лог-сообщений: включаем время, имя логгера, уровень и сообщение
    formatter = logging.Formatter("%(asctime)s | %(name)s | %(levelname)s | %(message)s")
    # Применяем форматер к обработчику
    handler.setFormatter(formatter)
    # Применяем обработчик к логгеру
    logger.addHandler(handler)

    return logger
