import os
import requests

from typing import Optional, Dict, Union, List

Params = Dict[str, Union[int, str, List[str]]]

from dotenv import load_dotenv
# Загружаем переменные окружения из .env файла
load_dotenv()

def build_query(params: Optional[Params] = None) -> str:
    """Функция для построения строки запроса."""
    if not params:
        return ""

    query = "?"

    for key, value in params.items():
        if isinstance(value, list):
            # Логика для работы с массивом (списком)
            query += f"{key}={'&'.join([f'{key}={v}' for v in value])}&"
        else:
            query += f"{key}={value}&"

    return query.rstrip("&")  # Удаляем последний &

class HttpClient:
    def __init__(self):
        token = os.getenv("API_TOKEN", "")
        
        self.default_headers = {
            'Authorization': f"Bearer {token}",  # Извлекаем токен из переменной окружения
            'Content-Type': 'application/json'
        }
    
    def get(self, url: str, params: Optional[Params] = None, **kwargs):
        url_with_params = url + build_query(params)

        print(url_with_params)

        """Выполняем GET запрос с заданными заголовками."""
        headers = {**self.default_headers, **(kwargs.get('headers') or {})}
        response = requests.get(url, headers=headers)
        return response

    # def post(self, url: str, data=None, json=None, **kwargs):
    #     """Выполняем POST запрос с заданными заголовками."""
    #     headers = {**self.default_headers, **(kwargs.get('headers') or {})}
    #     return self.session.post(url, data=data, json=json, headers=headers, **kwargs)