import allure
import pytest
from data import CourierData, Courier

class TestSignInCourier:
    @allure.title('Проверка успешной авторизации курьера')
    @allure.description('Отправляем запрос и проверяем, что курьер может авторизоваться')
    def test_sign_in_courier_success(self, courier):
        response = Courier.login_courier_and_get_courier_data(courier["data"])

        assert response.status_code == 200 and 'id' in response.json()

    @allure.title('Проверка возвращения ошибки, если не указан логин или пароль')
    @allure.description('Отправляем запрос и проверяем, что если логина или пароля нет, то запрос возвращает ошибку')
    @pytest.mark.parametrize('data', [CourierData.data_without_login, CourierData.data_without_password])
    def test_sign_in_courier_failure_without_login_or_password(self, data):
        response = Courier.login_courier_and_get_courier_data(data)

        assert response.status_code == 400 and response.json()['message'] == 'Недостаточно данных для входа'

    @allure.title('Проверка возвращения ошибки, если указан неправильный логин или пароль')
    @allure.description('Отправляем запрос и проверяем, что если неправильно указать логин или пароль, то система вернёт ошибку')
    @pytest.mark.parametrize('data', [CourierData.data_with_incorrect_login, CourierData.data_with_incorrect_password])
    def test_sign_in_courier_failure_with_incorrect_login_or_password(self, data):
        response = Courier.login_courier_and_get_courier_data(data)

        assert response.status_code == 404 and response.json()['message'] == 'Учетная запись не найдена'

    @allure.title('Проверка получения id курьера при успешной авторизации')
    @allure.description('Отправляем запрос и проверяем, что успешный запрос возвращает id')
    def test_sign_in_courier_success_with_correct_response_id(self):
        payload = {
                "login": 'ebaibus',
                "password": 'password12'
        }

        response = Courier.login_courier_and_get_courier_data(payload)
        r = response.json()

        assert 457586 == r["id"]

