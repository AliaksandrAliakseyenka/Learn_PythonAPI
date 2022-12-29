import requests

payload = {"name": "alex"}
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15'
}

response = requests.get("https://playground.learnqa.ru/api/hello", headers=headers, params=payload)

print(f"get text {response.text}")
print(f"get status code{response.status_code}")
print(f"get url {response.url}")
print(f"get headers {response.headers}")
print(f"get cookies {response.cookies}")
print(f"get encoding {response.encoding}")
print(f"get content {response.content}")
print(f"get in json format {response.json}")



