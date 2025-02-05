import json
import allure
import pytest
import requests
from data import OrderData
from urls import Urls

class TestOrderScooter:
    @allure.title('Проверка создания заказа самоката c разными значениями цвета')
    @allure.description('Отправляем запрос и проверяем, что можно указать разные значения цвета самоката')
    @pytest.mark.parametrize('color', [['BLACK'], ['GREY'], ['BLACK', 'GREY'], ['']])
    def test_order_scooter_success_with_different_various_colors(self, color):
        payload = OrderData.data
        payload['color'] = color
        data = json.dumps(payload)
        response = requests.post(Urls.ORDERS, data=data)

        assert response.status_code == 201 and "track" in response.json()

    @allure.title('Проверка, что при создании самоката тело ответа содержит "track"')
    @allure.description('Отправляем запрос и проверяем, что тело ответа содержит "track"')
    def test_order_scooter_success_with_track_in_response_body(self):
        data = json.dumps(OrderData.data)
        response = requests.post(Urls.ORDERS, data=data)

        assert "track" in response.json()