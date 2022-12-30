import json

str_pars_json = '{"User" : "Hellow, world"}'
obj = json.loads(str_pars_json)

key = "User"
if key in obj:
    print(obj['User'])
else:
    print(f"Ключа {key} в JSON нет")