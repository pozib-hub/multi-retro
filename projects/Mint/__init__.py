import time
import pyautogui
import logging

from utils.clicks import click_img_center
from logger_config import setup_logger

from utils.find_img import find_img

logging = setup_logger()

def closure_find(fn):
    return lambda name, *args, **kwargs: fn(name, "Mint", *args, **kwargs)

find_img_mint = closure_find(find_img)


def Mint(profile, window, pause_flag):
    try:
        # Открыть новую вкладку
        pyautogui.hotkey('ctrl', 't')
        time.sleep(1)  # Подождать немного дольше для стабильности

        pyautogui.hotkey('ctrl', 'l') 
        time.sleep(1)

        # Ввести URL и перейти на сайт
        pyautogui.write('https://www.mintchain.io/mint-forest')  
        time.sleep(1)
        
        pyautogui.press('enter')  # Нажать Enter
        time.sleep(10)  # Ждем загрузки страницы

        btn_connect_wallet = find_img_mint("btn_connect_wallet.png")
        if btn_connect_wallet:
            click_img_center(btn_connect_wallet)
            time.sleep(5)

            btn_connect_rabby = find_img_mint("btn_connect_rabby.png")
            click_img_center(btn_connect_rabby)
            time.sleep(5)

            if not btn_connect_rabby:
                btn_connect_rabby = find_img_mint("btn_connect_rabby_2.png")
                click_img_center(btn_connect_rabby)
                time.sleep(5)

            # i.page_loading.png
                # перезагрузить страницу и все по новой
            # click_img_center(page_loading)

            btn_sign_rabby = find_img_mint("btn_sign_rabby.png")
            click_img_center(btn_sign_rabby)
            time.sleep(5)

            btn_connect_confirm = find_img_mint("btn_connect_confirm.png")
            click_img_center(btn_connect_confirm)
            time.sleep(5)

        points_500 = find_img_mint("points_500.png", None, 0.75)
        click_img_center(points_500)
        time.sleep(1)

        btn_select_500_points = find_img_mint("btn_select_500_points.png")
        click_img_center(btn_select_500_points)
        time.sleep(1)

        points_25 = find_img("points_25.png", None, 0.75)
        while points_25:
            click_img_center(points_25)
            time.sleep(1)
            points_25 = find_img("points_25.png", None, 0.75)

    except Exception as e:
        logging.error("Error: Mint %s.", e)

    finally:
        time.sleep(1)
        pyautogui.hotkey('ctrl', 'w')
