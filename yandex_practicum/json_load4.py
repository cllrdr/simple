import json
from urllib3 import PoolManager

def load_json4(url):
    manager = PoolManager(10)
    response = manager.request('GET', url)
    payload = response.data.decode()

    return json.loads(payload)

print(load_json4('http://localhost/data.json'))