import requests

def load_json2(url):
    with requests.Session() as s:
        response = s.get(url)
    response.raise_for_status()
    return response.json()

print(load_json2('http://localhost/data.json'))