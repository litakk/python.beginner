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
# 
# SYNTAX - пишем только большими буквами а содержимое маленькими
# SYNTAX - под  каждым кодом пишем в конце  ; 
# ПОТОМ СОЗДАЕМ СЕРВЕР 127.0.0.1 И В НЕМ СОЗДАЕМ ТАБЛИЦУ А ЗАТЕМ КОНТРОЛИРУЕМ



# =================================================================================



# ADD - Добавить в таблицу новую запись
# add at least 5 cars to the table
# each should be unique
# =================================================================================
# UPDATE - Обновить запись в таблице
# update the price of the car with id 3 to 12345
# RU: обновить цену автомобиля с id 3 на 12345
# =================================================================================
# ALTER - Изменить структуру таблицы
# add a column to the table called 'sold'
# RU: добавить в таблицу колонку 'sold' (продано) *BOOLEAN*
#     тип данных - boolean (логический тип данных)
# =================================================================================
# UPDATE again  - Обновить запись в таблице
# update the sold status of the car with id 4 to True
# RU: обновить статус продажи автомобиля с id 4 на True
# =================================================================================
# DELETE - Удалить запись из таблицы
# delete the car with id 5 from the table
# RU: удалить автомобиль с id 5 из таблицы

# =================================================================================

# CREATE TABLE users (
#     id SERIAL PRIMARY KEY,
#     name VARCHAR(255),
#     email VARCHAR(255),
#     password VARCHAR(255) NOT NULL UNIQUE DEFAULT '12345' 
# );

# ====================================

# Insert data
# ДЛЯ СОЗДАНИЯ ОДНОЙ ТАБЛИЦЫ :
# INSERT INTO users (name, email, password) 
# VALUES ('John Doe', 'test@gmail.com', '12345');

# ДЛЯ СОЗДАНИЯ НЕСКОЛЬКИХ СРАЗУ 
# INSERT INTO users (name, email, password)
# VALUES ,
#     ('John Doe', 'test2@gmail.com', '12'),
#     ('Jane Doe 2', 'test3@gmail.com', '123'),
#     ('Jack Doe 3', 'test4@gmail.com', '1234');