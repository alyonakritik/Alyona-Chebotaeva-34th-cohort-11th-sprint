# URL_SERVICE хранит базовый URL веб-сервиса, который используется для доступа к API или другим ресурсам.
base_url = "https://2ff6d963-77ac-4fca-b186-c6b407a712e6.serverhub.praktikum-services.ru"

# CREATE_USER_ORDERS хранит путь к API-методу для создания нового заказа.
# Этот путь будет использоваться для формирования полного URL-адреса в сочетании с базовым URL сервиса,
# когда необходимо выполнить запрос на создание заказа.
CREATE_USER_ORDERS = "/api/v1/orders"

# Заголовки для HTTP-запроса, указывающие на то, что тело запроса будет в формате JSON.
headers = {
    "Content-Type": "application/json"
}

# Файл для логов.
# log_file_path хранит путь к файлу, куда будут записываться ошибки и исключения
# возникающие при выполнении HTTP-запросов к API.
log_file_path = "/var/www/backend/logs/error.log"
