<?php
// Подключаемся к базе данных
$conn = pg_connect("host=localhost dbname=simple user=postgres password=postgres");

// Получаем данные, введенные пользователем на сайте
$name = $_POST['name'];
$age = $_POST['age'];
$email = $_POST['email'];

// Выполняем SQL-запрос для вставки данных в таблицу 
$sql = "INSERT INTO users (name, age, email) VALUES ('$name', $age, '$email')";
$result = pg_query($conn, $sql);

// Закрываем соединение с базой данных
pg_close($conn);
?>