import copy
import pytesseract 
import time
import os

from apscheduler.schedulers.background import BackgroundScheduler
from queue import PriorityQueue

from projects.Bera_faucet import Bera_faucet
from projects.Apex import Apex
from projects.Mint import Mint
from projects.Kong import Kong

from utils.hot_keys import listener_hot_keys
from utils.get_profiles_windows import get_profile_id_with_chrome, get_profiles_ids_with_antys
from utils.language_layout import get_keyboard_layout, switch_to_english
from utils.scheduler import scheduled_add_tasks, scheduler_save_tasks, scheduler_load_tasks, scheduler_init_tasks, task_queue

from constants import profiles, script_dir, exclude_profiles_by_project

from logger_config import setup_logger

import threading
import keyboard

logging = setup_logger()

layout = get_keyboard_layout()
if layout != "en":
    switch_to_english()

#  вынести установку tesseract

# Путь к Tesseract, если требуется (на Windows):
pytesseract.pytesseract.tesseract_cmd = os.path.join(script_dir, "tesseract", "tesseract.exe") 


# Общая переменная для управления паузой и продолжением
pause_flag = threading.Event()

# Функция для переключения паузы и продолжения
def toggle_pause():
    if pause_flag.is_set():
        pause_flag.clear()
        logging.info("Продолжение выполнения задач.")
    else:
        pause_flag.set()
        logging.info("Выполнение задач приостановлено.")

# Назначаем хоткей Alt+W для функции toggle_pause
keyboard.add_hotkey('alt+w', toggle_pause)

listener_hot_keys()

tasks_cron_12_hour = [
    (2, Bera_faucet),
    (3, Apex)
]

tasks_interval_4_hour = [
    (20, Kong)
]

# Планировщик для выполнения задач каждые 4 часа и ежедневно в 9 утра
scheduler = BackgroundScheduler()
scheduler.add_job(scheduled_add_tasks, 'interval', hours=4, args=[tasks_interval_4_hour])
scheduler.add_job(scheduled_add_tasks, 'cron', hour=16, minute=10, args=[tasks_cron_12_hour])
scheduler.start()

scheduler_load_tasks() # Загрузка состояния очереди при старте программы

scheduler_init_tasks([(20, Kong)])


def get_all_profiles_ids_with_windows():
    # Поиск main профиля с запущенным Chrome
    main_profile_with_chrome = get_profile_id_with_chrome()

    # Получаем все профили с запущенным анитком
    profiles_ids_with_antys = get_profiles_ids_with_antys()

    # Создаем объединенный список
    all_profiles_ids_with_windows = profiles_ids_with_antys.copy()

    if main_profile_with_chrome:
        all_profiles_ids_with_windows.append(main_profile_with_chrome)

    # Сортируем list по order из profiles
    sorted_all_profiles_ids_with_windows = sorted(
        all_profiles_ids_with_windows,
        key=lambda x: int(profiles[x['id']]['order'])
    )

    return sorted_all_profiles_ids_with_windows

def main():
    passage = 0
    while True:
        # Если стоит флаг паузы, ждем, пока он не снимется
        while pause_flag.is_set():
            time.sleep(1)  # Избегаем перегрузки процессора при ожидании


        if task_queue.empty():
            time.sleep(60)  # Проверять наличие задач каждые 60 секунд
            continue

        layout = get_keyboard_layout()
        if layout != "en":
            switch_to_english()

        logging.info("Задачи в очереди: %s", [task[1].__name__ for task in list(task_queue.queue)])
        logging.info("")

        passage += 1

        logging.info("Проход %s начат", passage)
        

        sorted_all_profiles_ids_with_windows = get_all_profiles_ids_with_windows()

        current_passage_tasks = PriorityQueue()
        current_passage_tasks.queue = copy.deepcopy(task_queue.queue)
        # Список выполненных задач, которые нужно удалить после выполнения для всех профилей
        completed_tasks = []

        # Итерируемся по всем окнам хрома-профилям
        for profile_with_window in sorted_all_profiles_ids_with_windows:
            while pause_flag.is_set():
                time.sleep(1)  # Ожидание, если стоит пауза


            # Получаем окно
            window = profile_with_window['window']
            # Получаем профиль по идентификатору
            profile = profiles[profile_with_window['id']]

            profile_id = profile_with_window['id']
            profile_name = profiles[profile_id]['name']

            # Открываем окно (хром) для текущего профиля
            window.activate()
            window.maximize()
            logging.info("----------------------------------------")
            logging.info("Окно с профилем %s развернуто.", profile_name)
            time.sleep(1)

            is_exclude_profile = False

            # Проходим по всем задачам, которые нужно выполнить в текущем профиле
            for priority, task, task_time in current_passage_tasks.queue:
                _task = (priority, task, task_time)
                task_name = task.__name__

                while pause_flag.is_set():
                    time.sleep(1)  # Ожидание, если стоит пауза

                # Проверяем, исключен ли профиль для этой задачи
                if task_name in exclude_profiles_by_project and profile_name in exclude_profiles_by_project[task_name]:
                    completed_tasks.append(_task)  # Добавляем выполненную задачу в список
                    is_exclude_profile = True
                    continue
                
                logging.info("Выполняем задачу %s ...", task_name)

                task(profile, window, pause_flag)  # Выполняем метод с профилем и окном
                completed_tasks.append(_task)  # Добавляем выполненную задачу в список
                logging.info("Задача %s выполнена", task_name)

            try:
                # После выполнения всех задач для текущего профиля закрываем окно (хром)
                window.minimize()
            except Exception:
                logging.error("Error: Не удалось минимизировать окно %s.", profile_name)
            finally:
                logging.info("----------------------------------------")
                logging.info("")

        # Удаление только тех задач, которые были выполнены во всех профилях
        for completed_task in completed_tasks:
            for task in list(task_queue.queue):
                if task == completed_task:
                    task_queue.queue.remove(task)
                    logging.info("Задача %s с временной меткой %s удалена из очереди.", completed_task[1].__name__, completed_task[2])

        scheduler_save_tasks()  # Сохраняем текущее состояние после завершения круга     

        logging.info("Проход %s закончен", passage)
        logging.info("")

if __name__ == "__main__":
    main()