
import time
import pyautogui
import logging

from utils.clicks import click_img_center
from logger_config import setup_logger

from utils.find_img import find_img

logging = setup_logger()

def closure_find(fn):
    return lambda name, *args, **kwargs: fn(name, "Bera_faucet", *args, **kwargs)

find_img_bera = closure_find(find_img)

def Bera_faucet(profile, window, pause_flag):
    try:
        profile_address_eth = profile.get("address", {}).get("eth")

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
        pyautogui.write('https://bartio.faucet.berachain.com/#dapps')  
        time.sleep(1)
        
        pyautogui.press('enter')  # Нажать Enter
        time.sleep(5)  # Ждем загрузки страницы

        def after_load_page():
            pyautogui.scroll(1000)
            time.sleep(2)

            pyautogui.click(center_x, center_y)  # Кликаем в центре экрана
            time.sleep(2)

            # page_loaded
            isLoadedPage = find_img_bera("page_loaded.png")

            if not isLoadedPage:
                pyautogui.hotkey('ctrl', 'w')
                raise ValueError("Страница не загрузилась.")

            pyautogui.press('tab')
            time.sleep(1)

            pyautogui.write(profile_address_eth)
            time.sleep(3) 

            check_box_captcha = find_img_bera("captcha_ready.png")
            click_img_center(check_box_captcha)
            time.sleep(3)

        after_load_page()

        isCompeteCaptcha = find_img_bera("captcha_complete.png")

        count_attempts_pass_captcha = 0
        while not isCompeteCaptcha and count_attempts_pass_captcha != 7:
            pyautogui.press('f5')
            time.sleep(3)
            after_load_page()
            count_attempts_pass_captcha += 1
            isCompeteCaptcha = find_img_bera("captcha_complete.png")
            
        if not isCompeteCaptcha:
            pyautogui.hotkey('ctrl', 'w')
            raise ValueError("Error: Ошибка прохождения капчи.")
        
        btn_drip_tokens = find_img_bera("btn_drip_tokens.png")
        click_img_center(btn_drip_tokens)

    except Exception as e:
        logging.error("Error: Bera_faucet %s.", e)

    finally:
        time.sleep(1)
        pyautogui.hotkey('ctrl', 'w')
