from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from constans import path_chromeDriver


def connect_dolphin(response_json, additional_options):
    # Пример response который вернул сервер
    # response_json = {'success': True, 'automation': {'port': 60860, 'wsEndpoint': '/devtools/...'}}
    
    # Получаем порт на котором открыт профиль
    port = str(response_json["automation"]["port"])
    
    # Создание пути к драйверу
    chrome_path = Service(path_chromeDriver)
    options = webdriver.ChromeOptions()
    
    # Проверка наличия дополнительных опций и их добавление, если они существуют
    if additional_options:
        for key, value in additional_options.items():
            options.add_argument(f"--{key}={value}")
    
    # Подключение веб-драйвера к существующему экземпляру, запущенному на нашем порту
    # debugger_address = "debugger" относится к порту отладки Chrome.
    options.debugger_address = "127.0.0.1:" + port
    
    # Инициализация должна быть после options.debugger_address для запуска связи и подключения.
    driver = webdriver.Chrome(service=chrome_path, options=options)
    
    return driver