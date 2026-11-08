# Заголовки для HTTP-запроса, тело запроса будет в формате JSON

headers = {
    "Content-Type": "application/json"
}

# Тело для создание нового заказа

new_order = {
    "firstName": "Яна",
    "lastName": "Петрова",
    "address": "Арбат",
    "metroStation": 49,
    "phone": "89213332211",
    "rentTime": 5,
    "deliveryDate": "2026-10-18",
    "comment": "Привет",
    "color": ["BLACK"]
}