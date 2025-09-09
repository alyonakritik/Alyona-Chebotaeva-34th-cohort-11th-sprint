# Алена Чеботаева, 34-я когорта — Финальный проект. Инженер по тестированию плюс.

# Импортируем тестовые данные для создания заказа.
from data import user_orders
# Импортируем функции для отправки POST и GET запросов.
from sender_stand_request import post_request, get_request
# Импортируем путь к API для создания заказа.
from configuration import CREATE_USER_ORDERS

# Функция для проверки создания заказа.


def test_create_order_returns_201():
    # 1. Отправляем POST-запрос на создание нового заказа.
    response = post_request(CREATE_USER_ORDERS, json=user_orders)
    # 2. Проверяем, что заказ успешно создан (ожидаем код 201).
    assert response.status_code == 201, f"Ожидали 201, получили {response.status_code}"
    print("Заказ создан")

# Функция для проверки получения заказа по трек-номеру.


def test_get_order_by_track_returns_200():
    # 1. Сначала создаём заказ, чтобы получить его трек-номер.
    create_response = post_request(CREATE_USER_ORDERS, json=user_orders)
    track = create_response.json().get("track")
    # 2. Отправляем GET-запрос для получения заказа по трек-номеру.
    get_response = get_request("/api/v1/orders/track", params={"t": track})
    # 3. Проверяем, что сервер вернул успешный код 200.
    assert get_response.status_code == 200, f"Ожидали 200, получили {get_response.status_code}"
    print(f"Трек номер заказа: {track}")
