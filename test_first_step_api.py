import requests


class TestFirstStepApi:

    def test_check_status_code(self):
        url = "https://playground.learnqa.ru/api/hello"
        name = "Alex"
        data = {"name": name}

        response = requests.get(url, params=data)
        assert response.status_code == 200, "Wrong response code status"

        response_dict = response.json()
        assert "answer" in response_dict, "There in no field 'answer' in the response"

        expected_response_text = f"Hello, {name}"
        actual_response_text = response_dict["answer"]
        assert actual_response_text == expected_response_text, "Actual text in the response in not correct"