import logging

logger = logging.getLogger(__name__)

def setup_logger():
    if not logger.hasHandlers():  # Проверяем, есть ли уже обработчики
        # Очищаем файл логов при запуске
        # with open('app.log', 'w'):
        #     pass  # Просто открываем файл в режиме записи, чтобы очистить его

        logger.setLevel(logging.INFO)

        # Создаем обработчики
        file_handler = logging.FileHandler('app.log')
        stream_handler = logging.StreamHandler()

        # Устанавливаем формат логирования
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        stream_handler.setFormatter(formatter)

        # Добавляем обработчики к логгеру
        logger.addHandler(file_handler)
        logger.addHandler(stream_handler)

    return logger
