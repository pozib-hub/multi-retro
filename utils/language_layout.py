# Загружаем пользовательскую библиотеку
import ctypes

user32 = ctypes.WinDLL('user32', use_last_error=True)

def switch_to_english():
    # Английская раскладка (США) (0x0409 - English (US))
    ENGLISH_LAYOUT = '00000409'
    # Загружаем английскую раскладку клавиатуры
    user32.LoadKeyboardLayoutW(ENGLISH_LAYOUT, 1)
    # Переключаем текущую раскладку на английскую
    user32.SendMessageW(user32.GetForegroundWindow(), 0x0050, 0, int(ENGLISH_LAYOUT, 16))

def get_keyboard_layout():
    # Получаем идентификатор потока активного окна
    hkl = user32.GetKeyboardLayout(0)

    layout = hkl & 0xFFFF

    if layout == 0x0409:
        return "en"
    elif layout == 0x0419:
        return "ru"
    else:
        return hex(layout)