# Автотест API сервиса заказов

## Что проверяет тест
1. Создание заказа (`POST /api/v1/orders`)
2. Сохранение номера трека заказа
3. Получение заказа по треку (`GET /api/v1/orders/track?t=<track>`)
4. Проверка, что код ответа равен `200`

Ошибки при запросах записываются в файл:
/var/www/backend/logs/error.log

## Структура проекта
- `data.py` — тестовые данные  
- `configuration.py` — базовый URL, заголовки, путь к логам  
- `sender_stand_request.py` — функции для запросов (POST/GET, с логами)  
- `test_order_api.py` — автотест создания и проверки заказа  
- `.gitignore` — исключения для git  

## Запуск теста
```bash
pytest -s -v test_order_api.py::test_get_order_by_track_returns_200 # Трек номер заказа.
pytest -s -v test_order_api.py::test_create_order_returns_201 # Заказ сделан.
pytest -s -v test_order_api.py # Запустить все тесты.
