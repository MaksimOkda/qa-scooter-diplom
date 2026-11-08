# Максим Петрущенков, 49-я когорта — Финальный проект. Инженер по тестированию плюс

import datetime
import sender_stand_request
import data

def test_get_order_by_track_success():
    # Копия тела запроса для нового заказа:
    current_body = data.new_order.copy()
    
    # Динамическое изменение даты заказа на следующий день от текущей
    tomorrow = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime("%Y-%m-%d")
    current_body["deliveryDate"] = tomorrow
    
    # Запрос на создание заказа
    response = sender_stand_request.post_new_order(current_body)
    
    # Сохранение номера трека из созданного заказа в track_number
    track_number = response.json()["track"]
    
    # Запрос на получение заказа по track_number
    order_response = sender_stand_request.get_order_by_track(track_number)
    
    # Проверка, что код ответа равен 200
    assert order_response.status_code == 200