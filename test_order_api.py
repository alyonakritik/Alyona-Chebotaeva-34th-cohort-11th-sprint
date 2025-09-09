# Алена Чеботаева, 34-я когорта — Финальный проект. Инженер по тестированию плюс.

# Импортируем тестовые данные для создания заказа.
from data import user_orders
# Импортируем функции для отправки POST и GET запросов.
from sender_stand_request import post_request, get_request
# Импортируем путь к API для создания заказа.
from configuration import CREATE_USER_ORDERS


def test_create_and_get_order():
    # 1. Отправляем POST-запрос на создание нового заказа.
    create_response = post_request(CREATE_USER_ORDERS, json=user_orders)

    # 2. Проверяем, что заказ успешно создан.
    assert create_response.status_code == 201, f"Ожидали 201, получили {create_response.status_code}"

    # 3. Получаем уникальный номер трека заказа из ответа сервера
    order_track = create_response.json().get("track")
    # Проверяем, что номер трека действительно есть в ответе.
    assert order_track is not None, "В ответе нет номера трека заказа"
    # Выводим номер трека заказа в консоль.
    print(f"Номер заказа: {order_track}")

    # 4. Отправляем GET-запрос на получение информации о заказе по его треку.
    get_response = get_request(
        "/api/v1/orders/track", params={"t": order_track})

    # 5. Проверяем, что сервер вернул успешный код 200.
    assert get_response.status_code == 200, f"Ожидали 200, получили {get_response.status_code}"
    # Выводим сообщение в консоль, что данные заказа получены успешно.
    print("Данные по заказу успешно получены, статус 200")
