import requests
from faker import Faker

from urls import Urls


class CourierDataGenerator:

    @staticmethod
    def generate_valid_courier_data():
        fake = Faker()

        login = fake.user_name()
        password = fake.password(length=10)
        first_name = fake.first_name()

        return {
            "login": login,
            "password": password,
            "firstName": first_name
        }

    @staticmethod
    def generate_courier_date_without_passport_field():
        fake = Faker()

        login = fake.user_name()
        first_name = fake.first_name()

        return {
            "login": login,
            "password": "",
            "firstName": first_name
        }


    @staticmethod
    def generate_courier_date_without_login_field():
        fake = Faker()

        password = fake.password(length=10)
        first_name = fake.first_name()

        return {
            "password": password,
            "firstName": first_name
        }


class CourierData:
    data_with_incorrect_login = {
        "login": 'ebaibus111',
        "password": 'password12'
    }

    data_with_incorrect_password = {
        "login": 'ebaibus',
        "password": 'password1234'
    }

    data_with_existing_login = {
        "login": 'alexei_97',
        "password": 'hello111',
        "firstName": 'gtreds'
    }

    valid_data = CourierDataGenerator.generate_valid_courier_data()

    data_without_password = CourierDataGenerator.generate_courier_date_without_passport_field()

    data_without_login = CourierDataGenerator.generate_courier_date_without_login_field()


class Courier:
    @staticmethod
    def register_courier_and_get_courier_data():
        data = CourierData.valid_data
        response = requests.post(Urls.COURIER, data=data)
        return {"data": data, "response": response }

    @staticmethod
    def login_courier_and_get_courier_data(courier_data):
        response = requests.post(Urls.COURIER_LOGIN, data=courier_data)
        return response

    @staticmethod
    def delete_courier(courier_id):
        data = {"id": courier_id }
        response = requests.delete(f'{Urls.COURIER}/{courier_id}', data=data)
        return response
