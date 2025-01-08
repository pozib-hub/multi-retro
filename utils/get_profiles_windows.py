import psutil
import re
import pygetwindow as gw
import ctypes
from typing import List, Dict, Any

_pattern_find_id_profile = r'\\browser_profiles\\(\d+)\\data_dir'

# Функция для получения PID из HWnd
def _get_pid_from_hwnd(hwnd: int) -> int:
    try:
        pid = ctypes.c_ulong()
        tid = ctypes.windll.user32.GetWindowThreadProcessId(hwnd, ctypes.byref(pid))
        return pid.value  # Возвращаем значение PID
    except Exception as e:
        print(f"Ошибка при получении PID: {e}")
        return None
    
def get_profiles_ids_with_antys() -> List[Dict[str, Any]]:
    list: List[Dict[str, Any]] = []

    # Проходим по всем запущенным процессам
    for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
        if proc.info['name'] and 'anty' in proc.info['name'].lower():
            if proc.info['cmdline']:
                for arg in proc.info['cmdline']:
                    if '--user-data-dir=' in arg:
                        match = re.search(_pattern_find_id_profile, arg)
                        if match:
                            profile_id = match.group(1)  # Найденные цифры профиля
                            pid = proc.info['pid']  # Получаем PID процесса

                            # Используем pygetwindow для поиска окон по PID
                            windows = gw.getAllWindows()
                            for window in windows:
                                window_pid = _get_pid_from_hwnd(window._hWnd)  # Получаем PID по HWnd
                                if window_pid == pid:  # Сравниваем PID
                                    list.append({ "id": profile_id, "window": window })
    return list

def get_profile_id_with_chrome():
    # Проходим по всем окнам
    for window in gw.getAllWindows():
        # Проверяем, есть ли в заголовке окна "chrome"
        if 'chrome' in window.title.lower():
            return { "id": "0", "window": window }
    return None
