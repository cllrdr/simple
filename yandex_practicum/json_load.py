import requests

def load_json(url):
    response = requests.get(url)
    return response.json()

print(load_json('http://localhost/data.json'))
