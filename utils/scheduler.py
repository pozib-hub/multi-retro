import json
import os
import time
from queue import PriorityQueue
from typing import List, Tuple, Callable

from projects.Bera_faucet import Bera_faucet
from projects.Apex import Apex
from projects.Mint import Mint
from projects.Kong import Kong
from logger_config import setup_logger

logging = setup_logger()

STATE_FILE = 'task_state.json'

# Очередь задач с приоритетами
task_queue = PriorityQueue()

task_map = {
    "Bera_faucet": Bera_faucet,
    "Kong": Kong,
    "Apex": Apex,
    "Mint": Mint
}

def scheduler_save_tasks():
    """Сохраняем задачи в файл с приоритетом, именем задачи и временной меткой."""
    with open(STATE_FILE, 'w') as f:
        json.dump([(task[0], task[1].__name__, task[2]) for task in list(task_queue.queue)], f)

def scheduled_add_tasks(tasks: List[Tuple[int, Callable[[], None]]]) -> None:
    """Добавляем новые задачи с временной меткой."""
    current_time = time.time()

    for task in tasks:
        # Добавляем текущую временную метку для каждой задачи
        task_queue.put((task[0], task[1], current_time))

    scheduler_save_tasks()
    logging.info("Tasks: %s добавлены в очередь на выполнение", ', '.join([task[1].__name__ for task in tasks]))

def scheduler_load_tasks():
    """Загружаем задачи из сохранённого состояния."""
    if os.path.exists(STATE_FILE) and os.path.getsize(STATE_FILE) > 0:
        with open(STATE_FILE, 'r') as f:
            task_data = json.load(f)
            for priority, task_name, task_time in task_data:
                task_queue.put((priority, task_map[task_name], task_time))

THREE_HOURS_IN_SECONDS = 3 * 60 * 60  # Время в секундах, равное 3 часам
def scheduler_init_tasks(tasks: List[Tuple[int, Callable[[], None]]]):
    """Инициализация задач, добавление только новых, если временная метка старше 3 часов."""
    current_time = time.time()
    existing_tasks = {task[1]: task[2] for task in list(task_queue.queue)}  # Словарь {задача: временная метка}

    # Добавляем только те задачи, которые либо отсутствуют, либо были добавлены более 3 часов назад
    new_tasks = [
        (task[0], task[1], current_time)
        for task in tasks
        if task[1] not in existing_tasks or (current_time - existing_tasks[task[1]]) >= THREE_HOURS_IN_SECONDS
    ]
            

    for task in new_tasks:
        task_queue.put(task)

    scheduler_save_tasks()
