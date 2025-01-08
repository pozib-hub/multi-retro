import time
import pyautogui

from utils.clicks import click_img_center
from logger_config import setup_logger

from .utils.check_quota import check_quota 

logging = setup_logger()

def Kong(profile, window, pause_flag):
    try:
        profile_name = profile['name']
        profile_delay_click = profile.get("projects", {}).get("Kong", {}).get('delay_click', 0.09)

        # Находим центр экрана
        screen_width, screen_height = window.size
        center_x = screen_width // 2
        center_y = screen_height // 2

        # Открыть новую вкладку
        pyautogui.hotkey('ctrl', 't')
        time.sleep(1)  # Подождать немного дольше для стабильности

        pyautogui.hotkey('ctrl', 'l') 
        time.sleep(1)

        # Ввести URL и перейти на сайт
        pyautogui.write('https://www.apex.exchange/kong')  
        time.sleep(1)
        
        pyautogui.press('enter')  # Нажать Enter
        time.sleep(15)  # Ждем загрузки страницы

        left_clicks, max_clicks = check_quota()

        if max_clicks == 0:
            # Значит данные не прогрузились
            pyautogui.hotkey('ctrl', 'w')
            raise ValueError(f"Kong профиля {profile_name} НЕ прогрузился.")

        logging.info(f"Kong профиля {profile_name} успешно прогрузился.")
        logging.info(f"Необходимо сделать {left_clicks} кликов c задержкой в {profile_delay_click}")

        check_interval = 180 # Время проверки # 3 минуты (180 секунд)
        start_time = time.time() # Время начала выполнения кликов, нужно для проверки между кликами
        prev_left_clicks = left_clicks  # Нужно для проверки между кликами

        # Выполняем клики
        for _ in range(left_clicks):
            if pause_flag.is_set():
                logging.info("Пауза задачи Kong.")
            while pause_flag.is_set():
                time.sleep(1)

            pyautogui.click(center_x, center_y)  # Кликаем в центре экрана
            time.sleep(profile_delay_click)  # Ждем указанное время

            # Проверяем, прошло ли 3 минуты
            elapsed_time = time.time() - start_time
            if elapsed_time >= check_interval:
                # Проверяем сколько кликов осталось по квоте
                temp_left_clicks = check_quota()

                # Выполняем проверку, а проходят ли клики, тк бывает ситуация, что клики перестают засчитываться
                if prev_left_clicks == temp_left_clicks:
                    raise ValueError("Клики не засчитываются. Закрываем профиль.")
                
                # Обновляем время начала для следующей проверки
                start_time = time.time()
                # Запоминаем текущее количество кликов
                prev_left_clicks = temp_left_clicks 

    except Exception as e:
        logging.error("Error: Kong %s.", e)

    finally:    
        time.sleep(1)
        pyautogui.hotkey('ctrl', 'w')

