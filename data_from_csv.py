import psycopg2
import csv

# подключение к БД
conn = psycopg2.connect(host="localhost", database="simple", user="postgres", password="postgres")

# открытие файла csv
with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # пропуск заголовка
    
    # запись данных в таблицу
    with conn:
        with conn.cursor() as cur:
            for row in reader:
                cur.execute(
                    "INSERT INTO users(name, age, email) VALUES (%s, %s, %s)",
                    (row[0], row[1], row[2])
                )

# закрытие соединения с БД
conn.close()