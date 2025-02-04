import pytest
from data import Courier


@pytest.fixture
def courier():
    courier_data = Courier.register_courier_and_get_courier_data()
    sign_in_response = Courier.login_courier_and_get_courier_data(courier_data["data"])
    yield courier_data
    Courier.delete_courier(sign_in_response.json()["id"])
