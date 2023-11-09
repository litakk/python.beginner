# first = int(input('Введите первое число: '))
# second = int(input('Введите второе число: '))
# operator = input('Введите значение: Плюс: + , Минус: - , Умножить: * , Разделить: / . ')
#     # - - - - - - - - - - - - 
# result = 0
#     # - - - - - - - - - - - - 
# if operator == "+":
#     result = first+second
#     # - - - - - - - - - - - - 
# elif operator == "-":
#     result = first-second
#     # - - - - - - - - - - - - 
# elif operator == "*":
#     result = first*second
#     # - - - - - - - - - - - - 
# elif operator == "/":
#     result = first/second
#     # - - - - - - - - - - - - 
# print("Ответ вашего запроса:", result)
#     # - - - - - - - - - - - - 
    
# first = int(input('Введите первое значение: '))
# second = int(input('Введите второе значение: '))
# operator = input('Введите оператор: ')

# result = 0
# match operator:
#     case "+": 
#         result = first + second
#     case "-": 
#         result = first - second
#     case "*": 
#         result = first * second
#     case "/": 
#         result = first / second
# print('Ответ вашего запроса:', result)

# one = int(input('Введите первое число '))
# two = int(input('Введите второе число '))
# opera = input("Введите значение ")
# #  - - - - - - - - - - - - - - -
# result = 0 
# if opera == "+":
#     result = one + two
# #  - - - - - - - - - - - - - - -
# elif opera == "-":
#     result = one - two
# print("Ответ вашего запроса:", result)



# import random
# target_num, guess_num = random.randint(1, 10), 0
# while target_num != guess_num:
#     guess_num = int(input('Guess a number between 1 and 10 until you get it right : '))
# print('Well guessed!')



# n=20
# for i in range(n):
#     for j in range(i):
#         print ('*', end="")
#     print('')

# for i in range(n,0,-1):
#     for j in range(i):
#         print('*', end="")
#     print('')
    


# class Person:
#     pass
# p = Person()
# setattr(p, 'name', 'Alice')
# setattr(p,'surname', 'Smith')
# print(p.name, p.surname) # Выводит "Alice"


# class MathUtils:
#     @staticmethod
#     def add(x, y):
#         return x + y    
# print(MathUtils.add(2, 3)) # Выводит 5



# class Person:
#     def say_hello(self):
#         print("Hello")

# class Student(Person):
#     def say_hello(self):
#         super().say_hello()
#         print("World")

# s = Student()
# s.say_hello() # Выводит "Hello" и "World"

#  - - - - -- - - - - - - - - - - - - -
#  - - - - -- - - - - - - - - - - - - -
#  - - - - -- - - - - - - - - - - - - -
#  - - - - -- - - - - - - - - - - - - -
#  - - - - -- - - - - - - - - - - - - -
#  - - - - -- - - - - - - - - - - - - -
# DICTIONARIES 
# Словари - это структуры данных, которые хранят данные в виде пар ключ-значение.
# x = {
#     "first": "Один",    "second": "Два",
#     "third": "Три",     "fourth": "Четыре",
#     "fifth": "Пять",    "sixth": "Шесть",
#     "seventh": "Семь",  "eighth": "Восемь",
# }
# print(x.get("fourth", "Не нашлось"))
# print(x["fourth"]) # => Четыре 
# print(x["www"]) # => # Error if not found
# ------------------------------------------------
# z = [ "Один", "Два", "Три", "Четыре", "Пять", "Шесть", "Семь" ]
# for i in z:
#     if i == "Четыре":
#         print(i)
# NOTE:
# If there are 1000 doors, when using list and seeking some of them,
# the loop we are using, opens every door one by one to check them
# But, if we use dictionary here, it directly opens the needed one.
# RU: Если есть 1000 дверей, когда мы используем <list> и ищем 
# некоторые из них, цикл, который мы используем, открывает каждую дверь
# по одной, чтобы проверить их. Но, если мы используем здесь <dict>,
# он сразу же открывает нужную.
# ------------------------------------------------
# IN JAVA-SCRIPT
# function Person(name, ..., ...) {
#     this.name = name
#     this.name = name
#     this.name = name
#     ...
# }
# let person1 = new Person(..., ..., ...)
# ------------------------------------------------
# IN PYTHON
# dict()  =>  dict(key=value, key=value, key=value)
# person = dict(name='Kamron', bemiyya=True)
# print(person)
# list()  => []
# str()   => ''
# int()   => 0
# float() => 0.0
# bool()  => False
# set()   => set()
# dict()  => {}


# # ACCESSING ITEMS ---------------------------------------------------------------------------
# dict[key]         => берёт значение по ключу
# dict.get(key)     => берёт значение по ключу
# dict.get(key, default)  => берёт значение по ключу, если его нет, то возвращает default

# Object.keys(dict) => возвращает список ключей (JS)
# dict.keys()       => возвращает список ключей

# Object.values(dict) => возвращает список ключей (JS)
# dict.values()     => возвращает список значений

# Object.entries(dict) => возвращает список ключей (JS)
# dict.items()      => возвращает список кортежей (ключ, значение)

# person1 = dict(name='Javox', bemiyya='True')
# print(person1.items())


# # ADDING ITEMS -----------------------------------------------------------------------------
# person1 = dict(name='Mirsaid', bemiyya=False)
# print(person1.items())
# person1['bemiyya'] = True
# person1['...'] = "..."
# person1[1] = 1
# print(person1.items())
# -----------------
# Update => updates the dict (changes the original)
# dict.update({key:value, key:value, key:value})
# person1.update({
#     "name": "Alex", 
#     "address": "Samarkand", 
#     "bemiyya":True
# })
# print(person1)
# -----------------
# If the key is not found, a new key:value pair is added to the dictionary.
# RU: Если ключ не найден, в словарь добавляется новая пара ключ: значение.

# But if it exists, then the value of the key is NOT updated.
# RU: Но если он существует, то значение ключа НЕ обновляется.
# dict.setdefault(key, value)
# person1 = dict(name='Mirsaid', bemiyya=False)
# person1.setdefault("address", "Tashkent")
# print(person1)


# # REMOVING ITEMS ---------------------------------------------------------------------------
# person1 = dict(name='Mirsaid', bemiyya=False)

# dict.pop(key)
# del_val = person1.pop('name')
# print("del_val: ", del_val)
# print("person1: ", person1)

# res = person1.pop('www', None)
# print("Result: ", res)
# print(person1)
# dict.pop(key, default)

# dict.popitem() => removes the last inserted item
# res = person1.popitem()
# print("Result: ", res)
# print("Remaining: ", person1)

# del dict[key]
# del person1['bemiyya']
# del person1 # deletes the whole dict
# print("Remaining: ", person1)



# # MERGE ------------------------------------------------------------------------------------
# person1 = dict(name='Mirsaid', bemiyya=False)
# person2 = dict(name="Covid", contageous=True)
# person3 = dict(name="Bemiyya", widespread=True)
# print("Before: ", person1)
# person1 |= person2
# print("After: ", person1)
# person1 |= person2 | person3
# print("After: ", person1)
# dict1.update(dict2)
# dict1 |= dict2
# dict1 |= dict2 | dict3 | dict4
# {**dict1, **dict2, **dict3, **dict4}
# print("Original: ", person1)
# result = {**person1, **person2, **person3}
# print("New: ", result)


# person2 = { "name2":"John",  "age2":20,  "surname2":"Khan",  "address2":"Samarkand" }
# person3 = {1:'a', 2:'b'}
# -----------------------------------
# person |= person2 | person3 
# -----------------------------------
# a = {**person, **person2, **person3 } 
# works like spread operator in JS
# -----------------------------------


# # OTHER METHODS ----------------------------------------------------------------------------
# dict.clear()
# dict.copy()

# for key, val in person.items():
#     person[key] = ""

# p2 = person.copy()
# p2.update({"name":"Ali"})
# print(p2)
# print(person)

# person = {
#     "name": "John",
#     "age": 20,
#     "surname": "Khan",
#     "address": "Samarkand"
# }

# dict.fromkeys(iterable, value)  -> is used to create a new dictionary from the given 
#                                    sequence of elements with a value provided by the user.
# EX: 
# fruits = ['apple', 'mango', 'banana']
# result = dict.fromkeys(fruits, 0)
# print(result)
# x = dict.fromkeys(['name', 'age'], 'unknown')
# print(x)

# # --------------------------------------------------------------------------------------------
# # --------------------------------------------------------------------------------------------
# from random import randint
# def random_dict_of_github_issue_ids(stop: int, max_count: int, start: int = 0):
#     return dict.fromkeys(
#         [str(randint(start, stop)) for _ in range(randint(0, max_count))], ""
#     )
# print(random_dict_of_github_issue_ids(100, 10))
# # --------------------------------------------------------------------------------------------
# # --------------------------------------------------------------------------------------------
# zip() function
# zip(iterator1, iterator2, ...)
# Result: ...(zip object)  =>  (1, 'a'), (2, 'b'), (3, 'c')

# itr1 = list('abcdefghijklmnopqrstuvwxyz')
# itr2 = range(len(itr1))
# zipped = zip(itr1, itr2)

# for (item, item2) in zipped:
#     print(item, item2)

# my_list1 = [1, 2, 3]
# my_list2 = ['a', 'b', 'c']
# for x, y in zip(my_list1, my_list2):
#     print(x, y) # Выводит 1 a, 2 b, 3 c

# # --------------------------------------------------------------------------------------------

# import random
# def find_number():
#     randnum = random.randint(1,10)
#     question = int(input('Enter a number between 1 and 10: '))
#     lives = 4
#     while randnum != question and lives > 0:
#         lives -= 1
#         print(f'You have {lives} lives left!')
#         question = int(input("Enter a number between 1 and 10: "))
#     print('you`re won!!!')
# find_number()

# --------------------------------------------------------------------------------------------

# def pattern(n):
#     for i in range(n):
#         print('*' * i)
#     for i in range(n, 0, -1):
#         print('*' * i)
# pattern(11)

# def сумма_кратных_чисел():
#     сумма_кратных = 0
#     for число in range(100):
#         if число % 3 == 0 or число % 5 == 0:
#             print(число)
#             сумма_кратных += число
#         print("Сумма кратных чисел равна: " + str(сумма_кратных))
# сумма_кратных_чисел()

# def draw_board(size):
#     for i in range(size):
#         print(" ---" * size)
#         print("|   " * (size+1))
#     print(" ---" * size)
# draw_board(3)

# def risunok(size):
#     for i in range(size):
#         print("---" * size)
#         print("|   " * (size + 1)) 


# первый = int(input("Введите первое число: "))
# второй = int(input("Введите второе число: "))
# оператор = input("Введите оператор: ")

# результат  = 0 

# if оператор == "+":
#    результат =  первый + второй
# elif оператор == "-":
#     результат = первый - второй
# print(результат)


# First = int(input("Введите 1 значение: "))
# Second = int(input("Введите 2 значение: "))
# Third = input("Введите оператор: ")

# result = 0
# if Third == "+":
#     result = First + Second
# elif Third == "-":
#     result = First - Second
# print(result)





# def check_key(dict, key):
#     return "Имеется" if key in dict else "Отсутствует"
# x = {'a': 1, 'b': 2}
# print(check_key(x, 'a')) 
