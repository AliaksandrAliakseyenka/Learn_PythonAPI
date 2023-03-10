import requests
from ..lib.base_case import BaseCase
from ..lib.assertions import Assertions

class TestUserRegister(BaseCase):

    def test_create_user_with_existing_email(self):
        data = {
            "password": "123",
            "username": "learnqa",
            "firstName": "learnqa",
            "lastName": "learnqa",
            "email": "vinkotov@example.com"

        }
        url = "https://playground.learnqa.ru/api/user/"
        response = requests.post(url, data=data)

        print("\n")
        print(f"status code: {response.status_code}")
        print(f"response: {response.content}")
