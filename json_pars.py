from json.decoder import JSONDecodeError
import json
import requests

str_pars_json = '{"User" : "Hellow, world"}'
obj = json.loads(str_pars_json)

key = "User"
if key in obj:
    print(obj['User'])
else:
    print(f"Ключа {key} в JSON нет")

responce = requests.get("https://playground.learnqa.ru/api/get_text")
print(responce.text)

try:
    parsed_response_text = responce.json()
    print(parsed_response_text)
except JSONDecodeError as ex:
    print(f"Response in not a JSON format {ex}")