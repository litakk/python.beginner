# УРОК - 1

# БАЗА ДАННЫХ -  ЕСТЬ 2 ТИПА БАЗЫ ДАННЫХ
# JSON - КЛЮЧ И ЗНАЧЕНИЕ
# RELATIONAL DB
# МОЖЕТ СОЕДИНЯТЬСЯ С ДРУГОЙ СТРАНИЦЕЙ - ИМЕТЬ ВЗАИМОСВЯЗЬ
# НЕНУЖНЫЕ БАЗЫ ДАННЫХ - JSON.DB AND MANGO.DB

# RELATIONAL DB - ПОЛЬЗУЕМСЯ ЧЕРЕЗ ID. EXAMPLE: ДЛЯ ТОГО ЧТО БЫ СОВМЕЩАТЬ 2 ТАБЛИЦЫ
# PSQL - POST - ДЕРЖИТ RELATIONAL DB/

# ЛЮБАЯ БАЗА ДАННЫХ ДОЛЖНА НАХОДИТЬСЯ НА СЕРВЕРЕ - СЕРВЕР МОЖЕТ БЫТЬ НА КОМПЬЮТЕРЕ ИЛИ НА АМАЗОНЕ

# ПОСЛЕ СКАЧИВАНИЯ МЫ ВКЛЮЧАЕМ ФУНКЦИЮ POSTGRES  
# https://www.enterprisedb.com/downloads/postgres-postgresql-downloads
# ДАЛЕЕ В ПОИСКЕ РАСШИРЕНИЙ НА VS ПИШЕМ PostgreSQL

# ====================================

# SYNTAX - пишем только большими буквами а содержимое маленькими
# SYNTAX - под  каждым кодом пишем в конце  ; 
# ПОТОМ СОЗДАЕМ СЕРВЕР 127.0.0.1 И В НЕМ СОЗДАЕМ ТАБЛИЦУ А ЗАТЕМ КОНТРОЛИРУЕМ

#  CREATE TABLE 

#  CREATE TABLE persons (
    #  id SERIAL PRIMARY KEY,
    #  name VARCHAR(255),
    #  email VARCHAR(255),
    #  password VARCHAR(255) NOT NULL UNIQUE DEFAULT '12345' 
#  );

#  - - - - - - - - - - - - - - - - - - - - - - - - - 

#  ДОБАВИТЬ ОДНУ СТРОКУ ИНФОРМАЦИИ 

#  INSERT INTO persons (name, email, password) 
#  VALUES ('John Doe', 'test@gmail.com', '12345');

#  - - - - - - - - - - - - - - - - - - - - - - - - - 

#  ДОБАВИТЬ СРАЗУ НЕСКОЛЬКО СТРОК ИНФОРМАЦИИ

#  INSERT INTO persons (name, email, password)
#  VALUES 
    #  ('John Doe', 'test2@gmail.com', '12'),
    #  ('Jane Doe 2', 'test3@gmail.com', '123'),
    #  ('Jack Doe 3', 'test4@gmail.com', '1234');

#  - - - - - - - - - - - - - - - - - - - - - - - - - 

#  ПОСМОТРЕТЬ РЕЗУЛЬТАТ
#  SELECT * FROM users;

#  - - - - - - - - - - - - - - - - - - - - - - - - - 

# ОБНОВИТЬ ДАННЫЕ
# UPDATE users SET name = 'Jane Doe' WHERE id = 1

#  - - - - - - - - - - - - - - - - - - - - - - - - - 

# ИЗМЕНИТЬ ТАБЛИЦУ
# ALTER TABLE users ADD COLUMN age INT

#  - - - - - - - - - - - - - - - - - - - - - - - - - 

# УДАЛИТЬ ДАННЫЕ
# DELETE FROM users WHERE id = 1

#  - - - - - - - - - - - - - - - - - - - - - - - - - 


# ADD - Добавить в таблицу новую запись
# =================================================================================
# UPDATE - Обновить запись в таблице
# обновить цену автомобиля с id 3 на 12345
# =================================================================================
# ALTER - Изменить структуру таблицы
# добавить в таблицу колонку 'sold' (продано) *BOOLEAN* тип данных - boolean (логический тип данных)
# =================================================================================
# UPDATE - Обновить запись в таблице
# RU: обновить статус продажи автомобиля с id 4 на True
# =================================================================================
# DELETE - Удалить запись из таблицы
# RU: удалить автомобиль с id 5 из таблицы

# =================================================================================

# VARCHAR => используется для хранения строк и текста.
#     INT => используется для хранения целых чисел.
#     SERIAL => используется для автоматического увеличения значения.
#     PRIMARY KEY => используется для установки первичного ключа (он идентичен обычному идентификатору)
#     NULL => используется для установки поля как пустого.
#     NOT NULL => используется для установки поля по мере необходимости
#     UNIQUE => используется для установки поля как уникального.
#     DEFAULT => используется для установки значения по умолчанию (например: DEFAULT '...')

# =================================================================================

# УРОК 2 УРОК 2 УРОК 2 УРОК 2 УРОК 2 УРОК 2 УРОК 2 УРОК 2 УРОК 2 УРОК 2 УРОК 2 УРОК 2 УРОК 2 УРОК 2
# УРОК 2 УРОК 2 УРОК 2 УРОК 2 УРОК 2 УРОК 2 УРОК 2 УРОК 2 УРОК 2 УРОК 2 УРОК 2 УРОК 2 УРОК 2 УРОК 2
# УРОК 2 УРОК 2 УРОК 2 УРОК 2 УРОК 2 УРОК 2 УРОК 2 УРОК 2 УРОК 2 УРОК 2 УРОК 2 УРОК 2 УРОК 2 УРОК 2

# Data types
# Boolean (TRUE/FALSE) например: CREATE TABLE customers (name TEXT, is_active BOOLEAN)
# Типы символов (CHAR, VARCHAR, TEXT) Основное различие между CHAR и VARCHAR заключается в том,
# что CHAR имеет фиксированную длину, а VARCHAR — переменную. Тип TEXT используется для хранения более длинных строк.

#  - - - - - - - - - - - - - - - - - - - - - - - - - 

# ПОДТЕКСТ -
# Он не имеет фиксированной длины.
# Разница между фиксированной и переменной длиной заключается в том, что фиксированная длина обрабатывается быстрее,
# чем переменная. И места занимает меньше.
# Сходство фиксированной и переменной длины заключается в том, что они оба хранят строки любой длины.

#  - - - - - - - - - - - - - - - - - - - - - - - - - 

# CHAR - САМАЯ БЫСТРАЯ - И места занимает меньше - CHAR 
#   CHAR (фиксированная длина)          максимум символов 255
#       пример: CHAR(10) 'Hello'
#           CREATE TABLE customers (name CHAR(10), address CHAR(10))
#  - - - - - - - - - - - - - - - - - - - - - - - - - 
#   VARCHAR (переменная длина)    максимум символов 65535
#       пример: VARCHAR(10) 'Hello'
#  - - - - - - - - - - - - - - - - - - - - - - - - - 
#   TEXT (переменная не ограничена)    максимум символов 65535
#       пример: TEXT 'Hello'
#           CREATE TABLE customers (name TEXT, address TEXT)
#  - - - - - - - - - - - - - - - - - - - - - - - - - 
#  - - - - - - - - - - - - - - - - - - - - - - - - - 
#  - - - - - - - - - - - - - - - - - - - - - - - - - 

# Числовые типы (INTEGER, BIGINT, DECIMAL, NUMERIC) INTEGER (целые числа) 
# максимальное количество символов 10 например: INTEGER 2147483647    
#  - - - - - - - - - - - - - - - - - - - - - - - - - 
# BIGINT (большие целые числа) 
# максимальное количество символов 19 например: BIGINT 9223372036854775807
#  - - - - - - - - - - - - - - - - - - - - - - - - - 
# DECIMAL (фиксированная точность)
# максимальное количество символов 131072 например:
# DECIMAL(3, 2) 999,99 
#  - - - - - - - - - - - - - - - - - - - - - - - - - 
# NUMERIC (переменная точность), максимальное количество символов 131072,
# например: NUMERIC(5,2) 999,99.
#  - - - - - - - - - - - - - - - - - - - - - - - - - 
#  - - - - - - - - - - - - - - - - - - - - - - - - - 
#  - - - - - - - - - - - - - - - - - - - - - - - - - 

# Типы даты/времени (DATE, TIME, TIMESTAMP)
# DATE (сохраняет только дату) максимум символов 10 например: DATE '2018-01-01' 
#  - - - - - - - - - - - - - - - - - - - - - - - - - 
# TIME (сохраняет только время) максимум 8 символов например: TIME '12:00:00'
#  - - - - - - - - - - - - - - - - - - - - - - - - - 
# TIMESTAMP (Сохраняет дату и время) максимум символов 26, например: TIMESTAMP '2018-01-01 12:00:00'

#  - - - - - - - - - - - - - - - - - - - - - - - - - 
#  - - - - - - - - - - - - - - - - - - - - - - - - - 
# CREATE TABLE users (last_login TIMESTAMP)
# INSERT INTO ... (last_login) 
# VALUES ('2018-01-01 12:00:00') || (NOW())

#  - - - - - - - - - - - - - - - - - - - - - - - - - 

# ИНТЕРВАЛ (хранит периоды времени) 
# СИНТАКСИС: ИНТЕРВАЛ 'значение' ЕДИНИЦЫ: год, месяц, день, час, минута, секунда, неделя  
# например: '1 год 2 месяца 2 дня ...'

#  - - - - - - - - - - - - - - - - - - - - - - - - - 

# SELECT * FROM orders WHERE order_date > NOW() - INTERVAL '30 days';
# Заказы, сделанные за последние 30 дней

# ex 2:
# CREATE TABLE events (
#    id SERIAL PRIMARY KEY,
#    event_name VARCHAR(255) NOT NULL,
#    start_time TIMESTAMP NOT NULL,
#    duration INTERVAL NOT NULL
# );
# INSERT INTO events (event_name, start_time, duration)
# VALUES (
#          'Birthday Party', 
#          TIMESTAMP '2024-01-01 12:00:00', 
#          INTERVAL '2 hours'
#       );

#  - - - - - - - - - - - - - - - - - - - - - - - - - 
#  - - - - - - - - - - - - - - - - - - - - - - - - - 

# NOT NULL => CREATE TABLE customers (name TEXT NOT NULL)
# UNIQUE => CREATE TABLE customers (name TEXT UNIQUE)
# PRIMARY KEY => CREATE TABLE customers (id SERIAL PRIMARY KEY, name TEXT)
# FOREIGN KEY => CREATE TABLE customers (id SERIAL PRIMARY KEY, name TEXT) 
# Разница между ПЕРВИЧНЫМ КЛЮЧОМ и ВНЕШНИМ КЛЮЧОМ заключается в том, что
# ПЕРВИЧНЫЙ КЛЮЧ используется для уникальной идентификации строки в таблице.
# FOREIGN KEY используется для ссылки на столбец в ДРУГОЙ ТАБЛИЦЕ.
# CHECK => CREATE TABLE customers (name TEXT, age INTEGER CHECK (age >= 18))
# EXCLUDE => SELECT * FROM users EXCLUDE age = 18; => 
# Это ограничение используется для исключения данных из таблицы.
# Например, если у нас есть таблица клиентов, и мы хотим исключить клиентов с тем же именем и возрастом.

#  - - - - - - - - - - - - - - - - - - - - - - - - - 
#  - - - - - - - - - - - - - - - - - - - - - - - - - 
#  - - - - - - - - - - - - - - - - - - - - - - - - - 

# Операторы в предложении WHERE
#  Равно => в Python у нас было ==
# < Меньше чем
# > Больше чем
# <= Меньше или равно
# = Больше или равно

# <> Не равно => в Python мы используем != пример: SELECT * FROM customer WHERE name <> 'John'
# != Не равно
# LIKE Проверьте, соответствует ли значение шаблону (с учетом регистра), например: SELECT * FROM customer WHERE name LIKE 'John%' => это вернет всех клиентов, имя которых начинается с John (% означает любое количество символов после John).
# ILIKE Проверьте, соответствует ли значение шаблону (без учета регистра), например: SELECT * FROM customer WHERE name ILIKE 'John%'
# И Логическое И пример: ВЫБРАТЬ * ИЗ клиентов, ГДЕ имя ILIKE «Джон%» И возраст > 18
# ИЛИ Логическое ИЛИ например: ВЫБРАТЬ * ОТ клиентов ГДЕ имя ILIKE 'Джон%' ИЛИ ​​возраст > 18
# IN Проверьте, находится ли значение в диапазоне значений, например: SELECT * FROM customer WHERE age IN [18, 19, 20] ИЛИ возраст > 30
# МЕЖДУ Проверьте, находится ли значение в диапазоне значений, например: ВЫБРАТЬ * ОТ клиентов ГДЕ возраст ОТ 18 ДО 30
# IS NULL Проверьте, является ли значение NULL, например: SELECT * FROM customer WHERE age IS NULL
# НЕ Дает отрицательный результат, например. НЕ НРАВИТСЯ, НЕ В, НЕ МЕЖДУ например: ВЫБРАТЬ * ОТ клиентов ГДЕ возраст НЕ МЕЖДУ 18 ДО 30
# Distinct и Limit и их разновидности.
# DISTINCT Выберите только отдельные (разные) значения, например: ВЫБЕРИТЕ ОТЛИЧНОЕ имя FROM клиентов.
# => это вернет все отдельные имена из таблицы клиентов, что означает, что если есть два клиента с одинаковым именем, будет возвращен только один из них.
# COUNT Подсчитайте количество возвращенных строк, например: SELECT COUNT(DISTINCT age) FROM customer => это вернет количество различных возрастов из таблицы клиентов.
# LIMIT Ограничить количество возвращаемых строк, например: SELECT * FROM customer LIMIT 10 => это вернет только 10 строк из таблицы клиентов.
# OFFSET Пропустить количество строк перед тем, как начать возвращать строки, например: SELECT * FROM customer LIMIT 10 OFFSET 10 => это вернет 10 строк из таблицы клиентов, начиная с 10-й строки.
# FETCH Ограничение количества возвращаемых строк FETCH и LIMIT LIMIT аналогичен FETCH, но более гибок. LIMIT можно использовать с OFFSET, но FETCH нельзя использовать.

# пример: SELECT * FROM customer FETCH FIRST 10 ROWS ONLY => это вернет только 10 строк из таблицы клиентов.

# =================================================================================
# =================================================================================
# =================================================================================

# УРОК 3 УРОК 3 УРОК 3 УРОК 3 УРОК 3 УРОК 3 УРОК 3 УРОК 3 УРОК 3 УРОК 3 УРОК 3 УРОК 3 УРОК 3 УРОК 3
# УРОК 3 УРОК 3 УРОК 3 УРОК 3 УРОК 3 УРОК 3 УРОК 3 УРОК 3 УРОК 3 УРОК 3 УРОК 3 УРОК 3 УРОК 3 УРОК 3
# УРОК 3 УРОК 3 УРОК 3 УРОК 3 УРОК 3 УРОК 3 УРОК 3 УРОК 3 УРОК 3 УРОК 3 УРОК 3 УРОК 3 УРОК 3 УРОК 3

# Элементы синтаксиса - Продолжение второго урока

# CREATE TABLE Customers (
#   id SERIAL PRIMARY KEY,
#   name VARCHAR(255) NOT NULL,
#   email VARCHAR(255) NOT NULL
# );
# CREATE TABLE Orders (
#   id SERIAL PRIMARY KEY,
#   order_date DATE NOT NULL,
#   total DECIMAL(10,2) NOT NULL,
#   customer_id INTEGER NOT NULL,
#   FOREIGN KEY (customer_id) REFERENCES Customers (id)
# );
# INSERT INTO Customers (name, email)
# VALUES ('John Doe', 'test@mail.com');

# INSERT INTO Orders (order_date, total, customer_id)
# VALUES ('2022-01-01', 100.00, 1);

# INSERT INTO Orders (order_date, total, customer_id)
# VALUES ('2022-02-01', 150.00, 1);

# SELECT * FROM Customers;
# SELECT * FROM Orders;


# =================================================================================
# =================================================================================

# Допустим, у нас есть две таблицы: Студенты и Курсы.
# Каждый студент может записаться на несколько курсов, поэтому мы хотим создать
# связь между двумя таблицами с использованием ограничения FOREIGN KEY.

# CREATE TABLE Students (
#   id SERIAL PRIMARY KEY,
#   name VARCHAR(255) NOT NULL,
#   email почта VARCHAR(255) NOT NULL
# );

# CREATE TABLE Course (
#   id SERIAL PRIMARY KEY,
#   name VARCHAR(255) NOT NULL,
#   instructor VARCHAR(255) NOT NULL
# );

# CREATE TABLE 
#   id SERIAL PRIMARY KEY,
#   Student_id ЦЕЛОЕ ЧИСЛО, НЕ НУЛЕВОЕ,
#   Course_id ЦЕЛОЕ ЧИСЛО, НЕ НУЛЕВОЕ,
#   ВНЕШНИЙ КЛЮЧ (student_id) ССЫЛКИ Студенты (id),
#   ВНЕШНИЙ КЛЮЧ (course_id) ССЫЛКИ Курсы (id)
# );

# INSERT INTO Курсы (имя, преподаватель)
# ЦЕННОСТИ («Математика», «Мистер Смит»),
#        («Наука», «Миссис Смит»),
#        («Английский», «Мистер Джонс»);

# ВСТАВИТЬ В Студентов (имя, адрес электронной почты)
# ЗНАЧЕНИЯ («Джон Смит», «test@mail.com»),
#         («Мэтью», «test2@mail.com»);

# ВЫБРАТЬ * ИЗ студентов;

# INSERT INTO Зачисления (student_id, Course_id)
# ЦЕННОСТИ
#       (1, 1),
#       (1, 2),
#       (1, 3);
# ВЫБРАТЬ * ИЗ регистрации;

# Это означает, что студент с идентификатором 1 зачислен на курс с идентификатором 1.


# =================================================================================
# =================================================================================
# =================================================================================
# =================================================================================


# MAX() - Возвращает максимальное значение в наборе значений
# =================================================================================
# SELECT MAX(price) FROM products;
# MIN() - Возвращает минимальное значение в наборе значений
# =================================================================================
# SELECT MIN(price) FROM products;
# AVG() - Возвращает среднее значение в наборе значений
# =================================================================================
# SELECT AVG(price) FROM products;
# SUM() - Возвращает сумму всех или отдельных значений в наборе значений.
# =================================================================================
# SELECT SUM(price) FROM products;
# COUNT() - Возвращает количество строк, соответствующих заданному критерию
# COUNT(DISTINCT) - Возвращает количество различных строк, соответствующих заданному критерию.
# =================================================================================
# SELECT COUNT(*) FROM products;
# SELECT COUNT(DISTINCT price) FROM products;
# ROUND() - Округляет число до указанного количества десятичных знаков
# =================================================================================

# SYNTAX:  ВЫБЕРИТЕ РАУНД(column_name, number_of_decimal_places) FROM table_name;

# SELECT ROUND(price, 2) FROM products;
# Это вернет столбец цен, округленный до двух десятичных знаков.
# ex:
#    price  = 10.1234
#    result = 10.12
# CONCAT() - Добавляет два или более выражений вместе
# =================================================================================
# SELECT CONCAT(first_name, ' ', last_name) AS Full_Name FROM customers;
# UNION - Объединяет результат двух или более операторов SELECT.
# =================================================================================
# Запросы в объединении должны соответствовать следующим правилам:
# Они должны иметь одинаковое количество столбцов
# Столбцы должны иметь одинаковые типы данных
# Столбцы должны быть в одном порядке
# =================================================================================
# ПРИМЕЧАНИЕ. Оператор UNION по умолчанию выбирает только отдельные значения.
# Чтобы разрешить дублирование значений, используйте оператор UNION ALL.
# SELECT * FROM customers;
# SELECT * FROM students;
# =================================================================================
# SELECT name, email FROM customers
# UNION
# SELECT name, email FROM students;
# UNION ALL - Объединяет результат двух или более операторов SELECT, но он не удаляет повторяющиеся строки
# =================================================================================
# SELECT first_name, last_name FROM customers
# UNION ALL
# SELECT first_name, last_name FROM employees;
# ORDER BY - Сортирует набор результатов по возрастанию или убыванию.
# =================================================================================
# SELECT * FROM customers ORDER BY first_name;
# SELECT * FROM customers ORDER BY first_name DESC;
# GROUP BY - Группирует строки с одинаковыми значениями в итоговые строки.
# =================================================================================
# SELECT * FROM customers GROUP BY first_name;

# <!
# *Merging two or more columns*

# ```sql
# Допустим, у нас есть таблица со следующими данными:

# Customers TABLE
# ___________________________________________________
# id | name  | surname | full_name | email
# 1  | John  | test1   |          | John@test.com
# 2  | Mary  | test2   |          | Mary@test.com
# 3  | Peter | test3   |          | Peter@test.com
# ___________________________________________________

# Мы хотим добавить новый столбец с именем Full_name и заполнить его именем и фамилией.
# Мы можем сделать это с помощью функции CONCAT()

# ALTER TABLE customers ADD COLUMN full_name VARCHAR(255);
# UPDATE customers SET full_name = CONCAT(name, ', email: ', email);

# =================================================================================
# =================================================================================
# =================================================================================

# УРОК 4 УРОК 4 УРОК 4 УРОК 4 УРОК 4 УРОК 4 УРОК 4 УРОК 4 УРОК 4 УРОК 4 УРОК 4 УРОК 4 УРОК 4 УРОК 4 УРОК 4 
# УРОК 4 УРОК 4 УРОК 4 УРОК 4 УРОК 4 УРОК 4 УРОК 4 УРОК 4 УРОК 4 УРОК 4 УРОК 4 УРОК 4 УРОК 4 УРОК 4 УРОК 4 
# УРОК 4 УРОК 4 УРОК 4 УРОК 4 УРОК 4 УРОК 4 УРОК 4 УРОК 4 УРОК 4 УРОК 4 УРОК 4 УРОК 4 УРОК 4 УРОК 4 УРОК 4 

# PYTHON + PSQL
# CREATE INDEX index_name
# ON table_name (column1, column2, ...);

# CREATE INDEX users_names_inx
# ON users (name) WHERE name IS 'Alex%';

# Делая это, мы сообщаем базе данных создать индекс для таблицы table_name, 
# и этот индекс будет основан на column1, column2, ... columns.


# =================================================================================
# =================================================================================


# Для работы с postgresql нам необходимо установить psycopg2-binary
# pip install psycopg2-binary
import os
import faker
import psycopg2
import requests

# Connecting to the database
conn = psycopg2.connect(
    user="postgres",
    password="qweqweqwe",
    host="localhost",
    port="5432",
    database="postgres"
)
# This is for autocommiting the changes
# It means that we don't need to commit every time
# to save the changes in the database
# Otherwise, we need to commit every time when we
# change something by using conn.commit()
conn.autocommit = True

# This is the cursor
cur = conn.cursor()

# Creating the table
cur.execute('''
CREATE TABLE IF NOT EXISTS users(
    id SERIAL PRIMARY KEY,
    birthdate DATE NOT NULL,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    bio TEXT
);
''')
cur.execute('''INSERT INTO table_name 
    VALUES (...)
''')  # - to insert data into the table

# ========================================================
# Insert 10000 rows of people into users table
# Each should have name, email, password, country
# Use faker to insert all the data
fake = faker.Faker()
for i in range(10):
    cur.execute('''
        INSERT INTO users 
        (birthdate, first_name, last_name, email, bio) 
        VALUES (%s, %s, %s, %s, %s);
        ''', (
        fake.date(),       # - generates 'YYYY-MM-DD'
        fake.first_name(), # - generates first name
        fake.last_name(),
        fake.email(),
        fake.text()
    ))
# ========================================================
# To write a code "pg_dump -U postgres -h localhost -p 5432 -F c -f база.psql postgres"
# to create a backup of the database with the help of python
def save_db_at_this_point():
    os.system('pg_dump -U postgres -h localhost -p 5432 -F c -f db.psql postgres')
# ========================================================
# To print the table in the terminal
cur.execute('''SELECT * FROM users;''')
rows = cur.fetchone()

if rows:
    print(rows)
else:
    print("No rows returned.")
# ========================================================
# .com - commercial
# .org - organization
# .net - network
# .gov - government
# .ru  - Russia
# .ua  - Ukraine
# .uz  - Uzbekistan
# .us  - United States# To work with postgresql we need to install psycopg2-binary
# pip install psycopg2-binary
import os
import faker
import psycopg2
import requests

# Connecting to the database
conn = psycopg2.connect(
    user="postgres",
    password="qweqweqwe",
    host="localhost",
    port="5432",
    database="postgres"
)
# This is for autocommiting the changes
# It means that we don't need to commit every time
# to save the changes in the database
# Otherwise, we need to commit every time when we
# change something by using conn.commit()
conn.autocommit = True

# This is the cursor
cur = conn.cursor()

# Creating the table
cur.execute('''
CREATE TABLE IF NOT EXISTS users(
    id SERIAL PRIMARY KEY,
    birthdate DATE NOT NULL,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    bio TEXT
);
''')
cur.execute('''INSERT INTO table_name 
    VALUES (...)
''')  # - to insert data into the table

# ========================================================
# Insert 10000 rows of people into users table
# Each should have name, email, password, country
# Use faker to insert all the data
fake = faker.Faker()
for i in range(10):
    cur.execute('''
        INSERT INTO users 
        (birthdate, first_name, last_name, email, bio) 
        VALUES (%s, %s, %s, %s, %s);
        ''', (
        fake.date(),       # - generates 'YYYY-MM-DD'
        fake.first_name(), # - generates first name
        fake.last_name(),
        fake.email(),
        fake.text()
    ))
# ========================================================
# To write a code "pg_dump -U postgres -h localhost -p 5432 -F c -f база.psql postgres"
# to create a backup of the database with the help of python
def save_db_at_this_point():
    os.system('pg_dump -U postgres -h localhost -p 5432 -F c -f db.psql postgres')
# ========================================================
# To print the table in the terminal
cur.execute('''SELECT * FROM users;''')
rows = cur.fetchone()

if rows:
    print(rows)
else:
    print("No rows returned.")
# ========================================================
# .com - commercial
# .org - organization
# .net - network
# .gov - government
# .ru  - Russia
# .ua  - Ukraine
# .uz  - Uzbekistan
# .us  - United States