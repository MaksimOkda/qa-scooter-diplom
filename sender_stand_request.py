import requests
import configuration
import data

# Запрос на создание заказа
def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_NEW_ORDERS, 
                         json=body,
                         headers=data.headers)

# Запрос на получение заказа по треку заказа
def get_order_by_track(track_number):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_TRACK, 
                        params={"t": track_number})