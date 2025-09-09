# Импортируем библиотеку для работы с HTTP-запросами.
import requests
# Импортируем настройки проекта.
from configuration import base_url, headers

# Функция для отправки POST-запроса на API.


def post_request(endpoint, json=None):
    return requests.post(f"{base_url}{endpoint}", headers=headers, json=json)

# Функция для отправки GET-запроса на API.


def get_request(endpoint, params=None):
    return requests.get(f"{base_url}{endpoint}", headers=headers, params=params)
