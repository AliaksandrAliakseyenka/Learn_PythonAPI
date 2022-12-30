from urllib import response
import requests


class TestUserAuth:

    def test_auth_user(self):
        data = {"email": "vinkotov@example.com", "password": "1234"}

        response = requests.post(
            "https://playground.learnqa.ru/api/user/login", data=data)
        assert "auth_sid" in response.cookies, "There in no auth cookie in the response"
        assert "x-csrf-token" in response.headers, "There in no CSRF token header in the response"
        assert "user_id" in response.json(
        ), "The in no user id in the response"

        auth_sid = response.cookies.get("auth_sid")
        token = response.headers.get("x-csrf-token")
        user_id_from_auth_method = response.json()['user_id']

        response_sava_result = requests.get(
            "https://playground.learnqa.ru/api/user/auth",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid})
        assert "user_id" in response_sava_result.json(
        ), "The is no user id in the second response"
        user_id_from_check_method = response_sava_result.json()["user_id"]
        assert user_id_from_auth_method == user_id_from_check_method, "User id from auth method is not equal to user from check method"