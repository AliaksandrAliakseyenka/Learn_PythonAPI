from tkinter import NO
from urllib import response
import requests

payload = {"login": "secret_login", "password": "secret_pass"}

response = requests.post("https://playground.learnqa.ru/api/get_auth_cookie",
                         data=payload)

print(dict(response.cookies), response.text, response.status_code,
      dict(response.headers))

cookies_value = response.cookies.get('auth_cookie')

get_cookie = {}
if cookies_value is not None:
    get_cookie.update({'auth_cookie': cookies_value})

responce_two = requests.post(
    "https://playground.learnqa.ru/api/check_auth_cookie", cookies=get_cookie)

print(responce_two.text, responce_two.status_code)
