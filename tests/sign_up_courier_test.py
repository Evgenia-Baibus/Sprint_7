import allure
import pytest
import requests
from urls import Urls
from data import AnswerMessage
from helpers import CourierData, Courier


class TestSignUpCourier:

    @allure.title('Проверка успешного cоздания курьера')
    @allure.description('Отправляем запрос и проверяем, что курьера можно создать')
    def test_courier_creation_success(self, courier):
        response = courier["response"]

        assert response.status_code == 201 and response.json() == {'ok': True}

    @allure.title('Проверка невозможности создания двух одинаковых курьеров ')
    @allure.description('Отправляем запрос и проверяем, что нельзя создать двух одинаковых курьеров')
    def test_courier_creation_failure_for_already_registered(self, courier):
        response_courier_already_registered = Courier.register_courier_and_get_courier_data()["response"]

        assert response_courier_already_registered.status_code == 409 and response_courier_already_registered.json()['message'] == AnswerMessage.message_sign_up_409

    @allure.title('Проверка возвращения ошибки, если не указан логин или пароль')
    @allure.description('Отправляем запрос и проверяем, что если логина или пароля нет, запрос возвращает ошибку')
    @pytest.mark.parametrize('data', [CourierData.data_without_login, CourierData.data_without_password])
    def test_courier_creation_failure_without_login_or_passport(self, data):
        response = requests.post(Urls.COURIER, data=data)

        assert response.status_code == 400 and response.json()['message'] == AnswerMessage.message_sign_up_400

    @allure.title('Проверка возвращения правильного кода ответа при успешной регистрации')
    @allure.description('Отправляем запрос и проверяем, что запрос возвращает правильный код ответа')
    def test_courier_creation_with_correct_status_code(self, courier):
        response = courier["response"]

        assert response.status_code == 201

    @allure.title("Проверка возвращения корректного тела ответа при успешной регистрации")
    @allure.description('Отправляем запрос и проверяем, что успешный запрос возвращает {"ok":true}')
    def test_courier_creation_with_correct_response_body(self, courier):
        response = courier["response"]

        assert response.json() == {'ok': True}

    @allure.title('Проверка возвращений ошибки, если указан логин уже зарегистрированного пользователя')
    @allure.description('Отправляем запрос и проверяем, что если создать пользователя с логином, который уже есть, возвращается ошибка')
    def test_courier_creation_failure_with_existing_login(self):
        response_courier_with_existing_login = requests.post(Urls.COURIER, data=CourierData.data_with_existing_login)

        assert response_courier_with_existing_login.status_code == 409 and response_courier_with_existing_login.json()['message'] == AnswerMessage.message_sign_up_409
