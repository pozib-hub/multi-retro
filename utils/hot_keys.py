
import keyboard
import os
import threading

def stop_script():
    # global is_running
    # is_running = False
    print("Остановка через Alt + S")
    os._exit(0)

def start_listening_close():
    print("Для остановки скрипта нажмите комбинацию Alt + S")
    keyboard.add_hotkey('alt+s', stop_script)
    keyboard.wait()  # Ожидание события горячей клавиши

def listener_hot_keys():
    """
    Запускает слушатель горячих клавиш в отдельном потоке.
    """
    # Запуск слушателя в фоновом потоке
    listener_thread = threading.Thread(target=start_listening_close)
    listener_thread.daemon = True  # Чтобы поток завершился при закрытии основного потока
    listener_thread.start()

