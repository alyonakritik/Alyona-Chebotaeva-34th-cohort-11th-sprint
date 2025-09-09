# Импортируем библиотеку для работы с HTTP-запросами.
import requests
# Импортируем настройки проекта.
from configuration import base_url, headers, log_file_path


# Функция для отправки POST-запроса на API.
# endpoint - путь к методу API.
def post_request(endpoint, json=None):
    try:
        # Выполняем POST-запрос.
        response = requests.post(
            f"{base_url}{endpoint}", headers=headers, json=json)
        return response
    except requests.RequestException as e:
        # Если произошла ошибка запроса, записываем её в файл логов.
        with open(log_file_path, "a") as f:
            f.write(f"POST {endpoint} error: {e}\n")
        # Повторно выбрасываем исключение для остановки теста или обработки.
        raise


# Функция для отправки GET-запроса на API.
# endpoint - путь к методу API.
def get_request(endpoint, params=None):
    try:
        # Выполняем GET-запрос.
        response = requests.get(
            f"{base_url}{endpoint}", headers=headers, params=params)
        return response
    except requests.RequestException as e:
        # Если произошла ошибка запроса, записываем её в файл логов.
        with open(log_file_path, "a") as f:
            f.write(f"GET {endpoint} error: {e}\n")
        # Повторно выбрасываем исключение для остановки теста или обработки.
        raise
