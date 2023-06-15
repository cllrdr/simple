import requests
import json
import psycopg2

# подключение к БД
conn = psycopg2.connect(host="localhost", database="simple", user="postgres", password="postgres")

def get_json_from_url(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

url = 'http://localhost/data.json'
data = get_json_from_url(url)
if data is not None:
    # Обрабатываем данные в нужном формате
    with open('data.json') as j:
        data = json.load(j)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users(name, age, email) VALUES (%s, %s, %s)",
                   (data['name'], data['age'], data['email'])
                   )
    conn.commit()
    conn.close()
else:
    print('Ошибка загрузки данных')