import time
import pyautogui
import logging

from utils.clicks import click_img_center
from logger_config import setup_logger

from utils.find_img import find_img

logging = setup_logger()

def closure_find(fn):
    return lambda name, *args, **kwargs: fn(name, "Apex", *args, **kwargs)

find_img_apex = closure_find(find_img)


def Apex(profile, window, pause_flag):
    try:
        profile_name = profile['name']

        # Открыть новую вкладку
        pyautogui.hotkey('ctrl', 't')
        time.sleep(1)  # Подождать немного дольше для стабильности

        pyautogui.hotkey('ctrl', 'l') 
        time.sleep(1)

        # Ввести URL и перейти на сайт
        pyautogui.write('https://omni.apex.exchange/points')  
        time.sleep(1)
        
        pyautogui.press('enter')  # Нажать Enter
        time.sleep(10)  # Ждем загрузки страницы

        btn_connect_wallet = find_img_apex("btn_connect_wallet.png")
        if btn_connect_wallet:
            click_img_center(btn_connect_wallet)
            time.sleep(5)

            btn_metamask = find_img_apex("btn_metamask.png")
            click_img_center(btn_metamask)
            time.sleep(5)

            btn_rabby_in_okx = find_img_apex("btn_rabby_in_okx.png")
            click_img_center(btn_rabby_in_okx)
            time.sleep(5)

        btn_check_in = find_img_apex("btn_check_in.png")
        click_img_center(btn_check_in)

    except Exception as e:
        logging.error("Error: Apex %s.", e)

    finally:
        time.sleep(1)
        pyautogui.hotkey('ctrl', 'w')
