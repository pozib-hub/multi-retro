import os
import pyautogui
from pyscreeze import Box

path_imgs_compare_dir = os.path.abspath(os.path.join("projects", "Mint", "imgs_compare"))

def find_img(name: str, box: Box = None, confidence: float = 0.8) -> Box | None:
    try:
        region = None
        if box:
            region = [box.left, box.top, box.width, box.height]

        img_path = os.path.join(path_imgs_compare_dir, name)
        return pyautogui.locateOnScreen(img_path, region=region, confidence=confidence)
    except Exception as e:
        pass