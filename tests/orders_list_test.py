import allure
import requests
from urls import Urls

class TestOrdersList:
    @allure.title('Проверка получения списка заказов')
    @allure.description('Отправляем запрос и проверяем, что в тело ответа возвращается список заказов')
    def test_success_getting_orders_list(self):
        response = requests.get(Urls.ORDERS)
        orders = response.json()["orders"]

        assert type(orders) == list
