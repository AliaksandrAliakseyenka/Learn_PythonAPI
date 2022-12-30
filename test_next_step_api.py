from unicodedata import name
from urllib import response
import pytest
import requests


class TestNextStepAPI:
    #параметризованные тесты
    names = [("Vitalii"), ("Alex"), ("Lena"), ("Gosha"), ("")]

    @pytest.mark.parametrize('name', names)
    def test_check_status_code(self, name):
        url = "https://playground.learnqa.ru/api/hello"
        data = {"name": name}

        response = requests.get(url, params=data)
        assert response.status_code == 200, "Wrong response code status"

        response_dict = response.json()
        assert "answer" in response_dict, "There in no field 'answer' in the response"
 
        if len(name) == 0:
            expected_response_text = "Hello, someone"
        else:
            expected_response_text = f"Hello, {name}"

        actual_response_text = response_dict["answer"]
        assert actual_response_text == expected_response_text, "Actual text in the response in not correct"