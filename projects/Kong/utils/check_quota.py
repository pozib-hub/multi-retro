import re
import pyautogui
import pytesseract 

def check_quota():
    # Делаем скриншот всего экрана
    screenshot = pyautogui.screenshot()

    # Используем pytesseract для распознавания текста на скриншоте
    text = pytesseract.image_to_string(screenshot)

    # Ищем строку с форматом "10 000/10 000" или "9,280/10,000"
    match = re.search(r'(\d{1,3}(?:[ ,]\d{3})*)\s*/\s*(\d{1,3}(?:[ ,]\d{3})*)', text)
    current = 0
    max_points = 0
    if match:
        # Убираем пробелы и запятые перед преобразованием в целые числа
        current = int(match.group(1).replace(',', '').replace(' ', ''))
        max_points = int(match.group(2).replace(',', '').replace(' ', ''))

    return current, max_points