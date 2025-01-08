from pyscreeze import Box
import pyautogui

def click_img_center(img: Box):
    if not img:
        return
    
    x, y = pyautogui.center(img)
    pyautogui.click(x, y)
