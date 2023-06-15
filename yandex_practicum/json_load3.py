import urllib.request
import json

def load_json3(url):
    with urllib.request.urlopen(url) as response:

        if(response.getcode() != 200):
            raise urllib.error.URLError(f"Error receiving data {response.getcode()}")

        data = response.read()
        jsonData = json.loads(data)
        return jsonData
    
print(load_json3('http://localhost/data.json'))