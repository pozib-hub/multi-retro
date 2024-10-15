import os
from datetime import datetime, timedelta

from dotenv import load_dotenv
# Загружаем переменные окружения из .env файла
load_dotenv()


def check_token_expiration_date():
    # Получаем дату генерации токена из переменной окружения
    date_generate_token_str = os.getenv("DATE_GENERATE_TOKEN", "")
    if not date_generate_token_str:
        raise ValueError("Дата генерации токена не указана")

    # Преобразуем строку в объект datetime
    try:
        date_generate_token = datetime.strptime(date_generate_token_str, "%Y:%m:%d")
    except ValueError:
        raise ValueError("Неверный формат даты. Ожидается формат: YYYY:MM:DD")

    # Определяем срок действия токена, например 365 дней
    token_lifetime = timedelta(days=365)

    # Рассчитываем дату истечения срока действия токена
    expiration_date = date_generate_token + token_lifetime

    # Рассчитываем оставшееся время до истечения срока действия
    remaining_time = expiration_date - datetime.now()

    # Выводим остаток времени до истечения срока действия токена
    if remaining_time.days >= 0:
        print(f"Токен авторизации будет просрочен через: {remaining_time.days} дней")
    else:
        print("Токен авторизации уже просрочен.")