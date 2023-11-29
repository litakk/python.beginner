# number types  => int, float, complex
# str
# sequence =>  list, tuple, range# searching type, mapping   =>  dict  (Object in JS)
# set  =>   set, frozenset
# binary type  =>  bytes, bytearray, memoryview
# bool  => True, False
# None  => None

# =========================================================================# 0 = 0

# 1 = 1# 2 = 10
# 3 = 11# 4 = 100
# 5 = 101
# 6 = 110# 7 = 111
# 8 = 1000# 9 = 1001
# 10 = 1010# 11 = 1011
# 12 = 1100# 13 = 1101
# 14 = 1110# 15 = 1111
# 16 = 10000# ...

# =========================================================================# In JavaScript


# try {}  catch {}  =>  попробуй, если получится, а если нет то перехвати ошибку

# =========================================================================

# In Python# try: ...   except: ...  => попробуй, если получится, а если нет то пропускай ошибку
# print("Started")# try:
#     print(a)# except NameError as err:
#     print(f"Переменная не найдена. Случилась ошибка: {err}")# print("Ended")

# =========================================================================

# from typing import Union
# try:#     x = 'Hello world'
#     print(x).print(x)# except Union[NameError, TypeError]:
#     print('Переменная не объявлена')
# =========================================================================
# Types of errors# 1. SyntaxError  =>  не правильно написан код и
#                      невозможно его прочитать для питона# EX:  1. print("Hello world)
#      2. print("Hello world'))# print("Started")
# try:#     print("a)
# except:#     print(f"Переменная не найдена. Случилась ошибка:")
# print("Ended")
# ------------------------
# 2. TypeError    =>  не правильно написан код и питон не может выполнить действие
# EX:  1. print(5 + 'Hello world')#      2. print(5 + [1, 2, 3])
# print(5 + 'Hello world')# print(5 + [1, 2, 3])
# ------------------------
# 3. NameError    =>  не правильно написан код и питон не может найти переменную# EX:  1. print(x) 2. print(y)
# =========================================================================
# 2==2 ? True : False  => In JavaScript
# -------------------------------------# Ternary operator in Python
# "Yes" if condition==True else "No"# if 2==3:
#     print('Yes')# else:
#     print('No')
# ------------------------
# print("yes") if 2 == 2 else print("No")
# ------------------------
# num = 5
# # print("Ok") if num == 5 else print("Hello Bemiyya")
# =========================================================================
# Range - range(10)             
# =>  range(0, 10)# list(range(10))
# =>  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# list(range(10, 20))     # =>  [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
# list(range(10, 30, 5))  # =>  [10, 15, 20, 25]
# print(list(range(10, 31, 5))) print(list(range(10, 1, -1)))
# =========================================================================
# for num in range(50,20,-2):
#     print(num) if num % 10 == 0 else print(f'{num} Not dividble to 10')
# =========================================================================
# ERROR TYPES
# 1. SyntaxError  =>  '...  => not closed string
#     RU: - Забыли поставить закрывающую кавычку в строке.   
#     RU: - Забыли поставить двоеточие в конце def, while, for, или if выражения.
# 2. TypeError    =>  1 + '...'  =>  unsupported operand type(s) for +: 'int' and 'str'  
#     RU: - Пытаемся сложить строку с целым числом или числом с плавающей точкой.
#     RU: - Пытаемся сложить список или кортеж с целым числом или числом с плавающей точкой.
# 3. NameError    =>  x  =>  name 'x' is not defined#     - Trying to use a variable that does not exist.
#     RU: - Пытаемся использовать переменную, которая не существует.#     - Trying to use a function or method that does not exist.
#     RU: - Пытаемся использовать функцию или метод, которого не существует.
# 4. IndexError   =>  [1, 2, 3][3]  =>  list index out of range#     - Trying to access an index in a list that does not exist.
#     RU: - Пытаемся получить доступ к индексу в списке, которого не существует.
# 5. ValueError   =>  int('...')  =>  invalid literal for int() with base 10: '...'#     - Converting a string to an integer or float, but the string is not a valid number.
#     RU: - Преобразование строки в целое число или число с плавающей точкой, но строка не является допустимым числом.#     - Converting a string to a boolean, but the string is not 'True' or 'False'.
#     RU: - Преобразование строки в логическое значение, но строка не является «True» или «False».#     - Using the datetime.datetime.strptime() function with a string that does not match the specified format string.
#     RU: - Использование функции datetime.datetime.strptime () с строкой, которая не соответствует указанной строке формата.#     - Using the json.loads() function with a string that is not valid JSON.
#     RU: - Использование функции json.loads () с недопустимой строкой JSON.# print(int("w"))  # =>  ValueError: invalid literal for int() with base 10: 'w'
# 6. KeyError     =>  {'a': 1}['b']  =>  'b' =>  not in dictionary
#     - Trying to access a key in a dictionary that does not exist.
# 7. AttributeError  =>  'Hello'.append('!')  =>  'str' object has no attribute 'append'#     - Trying to use a method on a data type that does not have that method.
#     - Trying to access an attribute that does not exist.
# 8. ZeroDivisionError  =>  1 / 0  =>  division by zero#     - Trying to divide a number by zero.
# 9. ImportError  =>  import math  =>  No module named 'math'
#     - Trying to import a module that does not exist.#     import bemiyya
# 10. IndentationError  =>  def func():  =>  expected an indented block
#     - Forgetting to indent the code inside a function, while, for, or if statement.
# ============================================================================# =============================================================================
# Generators

# y = ["apple", "orange", "banana"]  # "apple|orange|banana"
# y = "|".join(y)
# print(y)

import re 
# text = "Mentioning of reD, GrEen and BLUE is prohibited"
# words_to_replace = ["red", "green", "blue"]
# new_text = re.sub(f'{"|".join(words_to_replace)}',
#                 "***",
#                 text,
#                 flags=re.IGNORECASE)
# print(new_text)

# text = 'придумаю сюда текст но щяс не хочу думать'
# text_to_replace = ['сюда', 'думать']
# new_text = re.sub(f'{"|".join(text_to_replace)}',
#                "ЗАПРЕЩЕНО!",
#                text,
#                flags=re.IGNORECASE
#                   )
# print(new_text)
# # Using a for loop to generate a list of even numbers up to 10^6
# import time
# start = time.time()
# def even_nums():
#     # result = []#     # for num in range(1000000):
#     #     result.append(num) if num % 2 == 0 else "It is ODD"#     # return result
#     for num in range(1000000):#         yield num if num % 2 == 0 else "It is ODD"

# print(even_nums())
# end = time.time()# print(f"Time taken: {round(end - start,  5)}")
# =========================================================================
# print(list(even_nums_gen))# print(round(after - before, 5))
# =========================================================================


# try: print(a)
# except: print('Переменная не найдена')

# match / case

# if HTTPS_status == 200 or HTTPS_status == 201:
#     print('OK')
# elif HTTPS_status == 404:
#     print('Not found')
# elif HTTPS_status == 301 or HTTPS_status == 302:
#     print('Redirect')
# else:
#     print('Unknown')

# ========================================================================
# HTTPS_status = 100

# match HTTPS_status:
#     case 100 | 201:
#         print('меньше 200 или больше 200')
#     case 404:
#         print('Ошибка!')
#     case 301 | 302:
#          print('Redirect')
#     case _:
#         print('Unknown')
# ========================================================================
# answer = input('Your Answer:')
# match post:
#     case 'THE TEXT':
#         print('Exactly!')
#     case _:
#         print('Eror')
# ========================================================================
# if answer == 'Питон':
#    print('В точку!')
# else:
#     print('Don`t сorrect!')
# ========================================================================
# num = 4
# print("Ok") if num == 5 else print("Hello Bemiyya")






# - - -  - - - - - - -- 
# LEARNED TODAY

# 1. Range
# 2. Lists
#   methods
#   access
#   update
#   add
#   remove
# 3. Sort   &&  sorted
# 4. reverse()  &&  reversed()

# ==========================================================================
# Sequence types
# --------------
# arr = [1, 2, 3, 4, 5]         # list
# text = "Hello world"          # string
# test_tuple = (1, 2, 3, 4, 5)  # tuple
# range()                       # range
# ==========================================================================
# range(10)              => range(0, 10)
# list(range(10))        => [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# range(10, 20)    #     => range(10, 20)
# range(10, 20, 2) #     => range(10, 20, 2)
# list(range(10, 20, 2)) => [10, 12, 14, 16, 18]
# ---------------------------------------------------------
# for (let i=0; i<10; i++) {}
# for num in range(10):
#     print(num)
#     # num = num + 1
#     num += 1
# typeof([])        =>  object
# print(type([]))   =>  <class 'list'>
# print(type([]))
# ---------------------------------------------------------
# UPDATE
# x = [1, 2, 3, 4, 5, 6]
# print(x[1:3])
# x[2] = 10
# x[1:3] = [1, 2, 3]  # такой же как:  =>  x[1:3] = 1, 2, 3
# для заполнения пробела необходимо как минимум 2 элемента
# print(x)
# x_list[...:...] = [...]   =>  обновления с... по... по [...]
# ---------------------------------------------------------




# ADD
# x = [1, 2, 3]
# print("Before: " + str(x))

# x.insert(1, "Whatever")
# x.append("Whatever")
# x.extend(["Whatever", "Whatever"])

# print("After: " + str(x))

# [].insert(position, element_to_add) => вставлять
# [].append()  =>  добавит элемент в конец листа
# [].extend()  =>  добавит элементы в конец листа









# ---------------------------------------------------------



# REMOVE
# x = [1, 2, 3]
# z = ['a', 'b', 'c']
# deleted_item = x.pop(1)
# z.remove('b')
# z.remove('w') # выдает ОШИБКУ
# print("Other elements: ", z)
# print(1 in x)
# print(5 in x)
# "..." in x   =>  проверяет есть ли элемент в листе
# [].pop()     =>  удаляет последний элемент
# [].remove()  =>  удаляет элемент по значению


# ---------------------------------------------------------
# COPY
# x = ['a', 'b', 'c']
# z = x.copy()
# z.append("smth")

# print(x)
# print(z)

# [].copy() => копирует лист
# ---------------------------------------------------------



# SORT
# x = ['w', 'b', 'a', 'c']
# names = ['John', 'Alex', 'Bob', 'Zack']
# z = [2, 11, 6, 39, 9]

# x.sort(reverse=True)
# z.sort(reverse=True)
# names.sort(reverse=True)

# print(x)
# print(z)
# print(names)

# [].sort(reverse=True)  => меняет оригинальный лист
# sorted([])             => не меняет оригинальный лист
#                  и можно присвоить новой переменной
# ---------------------------------------------------------
# REVERSE
# [].reverse() =>  меняет оригинальный лист
# z = [2, 11, 6, 39, 9]
# z.reverse()
# print(z)
# ---------------------------------------------------------
# reversed and sorted  do NOT change the original list
# перевернутый и отсортированный не меняет исходный список

# z = [2, 11, 6, 39, 9]
# x = list(reversed(z))
# a = sorted(z)
# print("Original list", z)
# print(x)
# print(a)
# print("Original list", z)
# ---------------------------------------------------------





# List comprehension
# [ <expression> for x in <sequence> if <condition> ]
# -----------------------------------------------------
# result = [v for v in "Hello world" if v in 'aioue']
# print(result)


# data = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

# # Ex1: List comprehension: updating the same list
# data = [number+3 for number in data]
# print("Updating the list: ", data)

# # Ex2: List comprehension: creating a different list with updated values
# new_data = [x*2 for x in data]
# print("Creating new list: ", new_data)

# # Ex3: With an if-condition: Multiples of four:
# fourx = [x for x in new_data if x % 4 == 0]
# print("Divisible by four: ", fourx)


# # Ex4: Alternatively, we can update the list with the if condition as well
# fourxsub = [el-1 for el in new_data if el % 4 == 0]
# print("Divisible by four minus one: ", fourxsub)

# # Ex5: Using range function:
# nines = [x for x in range(100) if x % 9 == 0]
# print("Nines: ", nines)
# ---------------------------------------------
# users = ['Aziz', 'Jomol','Farzod', 'Diana', 'Laziz']
#  [x…() for … in … if … ]

# z = [name.upper() for name in users if name.endswith('z')]

# # z = []
# for name in users:
#     if name.endswith('l'):
#         name = name.upper()
#         z.append(name)
# print(z)

# ---------------------------------------------

# [if … else for … in … ]
# a = [name if name.endswith('z') else 'Not ends with Z' for name in users]

# a = []
# for name in users:
#     if name.endswith('z'):
#         a.append(name)
#     else:
#         a.append('Not Z')
# print(a)

# a = []
# for name in users:
#     if name.endswith('z'):
#         a.append(name)
#     else:
#         a.append('Not endswith Z')
# print(a)
# ---------------------------------------------
# arr = range(100)
# s = [
#     f"Even {num}" if num % 2 == 0 else f"Odd {num}"
#     for num in list(arr) if num < 50
# ]
# print(s)


# s = []
# for num in list(arr):
#     if num < 50:
#         if num % 2 == 0:
#             s.append(f"Even {num}")
#         else:
#             s.append(f"Odd {num}")
# ==============================================
# for i in s:
#     print(i)
# ---------------------------------------------
# def double(*arr, **kwargs):
#     return [num*2 for num in arr]


# res = double(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, bemiyya="Kamron")
# print(res)
# ---------------------------------------------


# TUPLE
# []  =>  mutable           =>  Можно изменять
# ()  =>  immutable         =>  Нельзя изменять
# ---------------------------------------------
# Tuple comprehension
# x = ("apple", "banana", "cherry")
# x = tuple([fruit.upper() for fruit in x])
# print(x)
# for item in x:
#     print(item.upper())
# ---------------------------------------------
# ordered      =>  RU: каждый элемент имеет свой индекс, начиная с 0
#             
# unchangeable => RU: после создания кортежа мы не можем изменить его элементы ЕСТЬ ПРИМЕР выше
# Tuple Length  =>  len()

# Fibonacci
# 0, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89 ...
# RU: Мы должны добавить последние два числа, чтобы получить следующее число
# --------------------------------------------------------------------------
# Создать кортеж с одним элементом   => ('...',)
# tuple() => tuple([..., ...])
# Change Tuple Values-Изменить значения кортежа => list(("apple", "banana", "cherry"))

# Unpacing  (In JS)
# let [x,y] = [1, 2]

# (In Python)
# Using Asterisk *   ||    _ * _   ||   _ _ *
# a, *b, c = ("apple", "banana", "cherry")

# Multiply
# print(("apple", "banana", "cherry") * 2)

# - - - - - - - - - -  - - - - - - - - - - - - - - - -



# -------------------------------------------------------------------


# append()  Добавляет элемент в конец списка
# clear()   Удаляет все элементы из списка
# copy()    Возвращает копию списка
# count()   Возвращает количество элементов с указанным значением
# extend()  Добавляет элементы списка (или любого итерируемого объекта) в конец текущего списка
# index()   Возвращает индекс первого элемента с указанным значением
# insert()  Добавляет элемент в указанную позицию
# pop()     Удаляет элемент в указанной позиции
# remove()  Удаляет элемент с указанным значением
# reverse() Изменяет порядок списка на обратный
# sort()    Сортирует список (изменяет оригинал)
# sorted()  Сортирует список (не изменяет оригинал)