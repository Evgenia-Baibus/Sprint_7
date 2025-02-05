# Автотесты API для сервиса [Яндекс.Самокат](https://qa-scooter.praktikum-services.ru/)

Сервис [Яндекс.Самокат](https://qa-scooter.praktikum-services.ru) - это сайт для аренды самоката.

Его документация: [API](qa-scooter.praktikum-services.ru/docs/).


## Структура проекта 

* [tests](tests) - директория с тестами
* [tests](tests/sign_up_courier_test.py) - файл с проверками регистрации курьера
* [tests](tests/sign_in_courier_test.py) - файл с проверками логина курьера
* [test](tests/orders_list_test.py) - файл с проверками списка заказов
* [test](tests/order_scooter_test.py) - файл с проверками создания заказа
* [data.py](data.py) - файл с данными заказа и курьера
* [urls.py](urls.py) - файл с эндроинтами
* [allure_results](allure_results) - каталог с отчетом тестирования
* [conftest.py](conftest.py) - файл с фикстурами
* [helpers.py](helpers.py) - файл с вспомогательными методами и классами

## Запуск тестов

Для запуска тестов выполнить:
```bash
pytest
```