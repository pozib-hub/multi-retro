from typing import List

from api.connect_dolphin.connect_dolphin import connect_dolphin
from api.http_client import HttpClient
from api.profile.types import UserProfile

client = HttpClient()


def get_profiles() -> List[UserProfile]:
    url = "https://dolphin-anty-api.com/browser_profiles"

    params = {
        "page": 1,
        "limit": 50,
    }

    response = client.get(url, params)

    if response.status_code == 200:
        profiles = response.json()
        return profiles['data']  # Возвращаем список профилей
    else:
        print(f"Ошибка при получении профилей: {response.status_code}")
        return []


def open_profile_by_id(id, additional_options=None):
    # Creating URL based on connection. Passing dynamic id
    req_url = f"http://localhost:3001/v1.0/browser_profiles/{id}/start?automation=1"
    
    # Sending request and getting response from the server
    response = client.get(req_url)

    # Converting response to JSON format
    response_json = response.json()

    # Passing request info to call the driver
    driver = connect_dolphin(response_json, additional_options=additional_options)
    
    return driver