import requests

payload = {"login": "secret_login", "password": "secret_pass"}

response = requests.post("https://playground.learnqa.ru/api/get_auth_cookie",
                         data=payload)

print(f"Check: \n{dict(response.cookies)}\n{response.status_code}\n{dict(response.headers)}")

cookies_value = response.cookies.get('auth_cookie')

get_cookies = {}
if cookies_value is not None:
    get_cookies.update({'auth_cookie': cookies_value})

responce_two = requests.post(
    "https://playground.learnqa.ru/api/check_auth_cookie", cookies=get_cookies)

print(responce_two.text, responce_two.status_code)