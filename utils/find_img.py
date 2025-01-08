import os
import pyautogui
from pyscreeze import Box

def find_img(name: str, project_name: str = None, box: Box = None, confidence: float = 0.8) -> Box | None:
    try:
        region = None
        if box:
            region = [box.left, box.top, box.width, box.height]

        # Dynamically set the path based on the project name
        path_imgs_compare_dir = ""
        if project_name:
            path_imgs_compare_dir = os.path.abspath(os.path.join("projects", project_name, "imgs_compare"))
        else:
            path_imgs_compare_dir = os.path.abspath(os.path.join("imgs_compare"))

        img_path = os.path.join(path_imgs_compare_dir, name)

        return pyautogui.locateOnScreen(img_path, region=region, confidence=confidence)
    except Exception as e:
        pass
