# DECORATORS - БЕРЕТ ВСЕ ФУНКЦИИ В СЕБЯ  
# WRAPPER - ОБЕРТКА - 
# MEMOIZE - ДАЁТ ИЗ СВОЕЙ ПАМЯТИ 

# def fn_1():
#     print("Function first")

# def fn_2():
#     print("Function Second")

# def fn_3(fn):
#     print('-----------------------------------')
#     print("Befor calling {}".format(fn.__name__))
#     fn()
#     print("After calling {}".format(fn.__name__))

# fn_3(fn_1)
# fn_3(fn_2)

# lesson  = "RU: Декораторы и обертки. EN: Decorators & Wrappers"
# Decorators — это функции, которые принимают в качестве аргумента другую функцию, добавляют какую-то функциональность,
# и затем возвращаем другую функцию. И все это без изменения исходного кода оригинала.
# функция, которую мы передали. В Python функции являются объектами первого класса, а это значит, что мы можем
# передать их в качестве аргументов другим функциям. Мы также можем вернуть их как значения из других функций.
# Это основа декораторов.

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# Синтаксис - SYNTAX

# def decorator_function(original_function):
#     def wrapper_function(): # RU: обертка => та функция которая покрывает оригинальную функцию
#         return original_function()
#     return wrapper_function

# @decorator_function
# def display():
#     print("Display function ran")


# display() # == decorator_function(display)()

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# БАЗОВЫЙ ДЕКОРАТОР
# def decorator_function(original_function):
#     def wrapper_function(*args, **kwargs):
#         print(f"Wrapper executed this before {original_function.__name__}")
#         return original_function(*args, **kwargs)
#     return wrapper_function

# @decorator_function
# def original_function(*args):
#     print("Original function ran")

# x = [1, 2, 3, 4, 5]
# original_function(x)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# определение декоратора
# def декоротивная_функция(func):
#     def покрывала_функции():
#         print("Это до выполнения функции")
#         result = func()  # RU: вызов оригинальной функции
#         print("Это после выполнения функции")
#         return result
#     return покрывала_функции

# Создание оригинальной функции
# @декоротивная_функция
# def оригинальная_функция():
#     print("Это призвано быть оригинальной функцией")

# функция_для_использования = декоротивная_функция(оригинальная_функция)

# Призив оригинальной функции
# оригинальная_функция()

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# Практический пример 1 - узнать время выполнения функции с помощью декоратора.
# декоратор для расчета продолжительности
# принимается любой функцией.

# def calculate_time(func):
    # added arguments inside the inner1,
    # if function takes any arguments,
    # can be added like this.
    # def inner1(*args, **kwargs):
    #     # storing time before function execution
    #     begin = time.time()
    #     func(*args, **kwargs)
    #     # storing time after function execution
    #     end = time.time()
    #     print("Total time taken in : ", func.__name__, end - begin)
    # return inner1

# это можно добавить к любой существующей функции,
# в данном случае для вычисления факториала

# @calculate_time
# def factorial(num):
# спать 1 секунду, потому что это занимает гораздо меньше времени
# чтобы вы могли увидеть реальную разницу
    # time.sleep(1)
    # print(math.factorial(num))

# вызов функции.
# factorial(10)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# ВОЗВРАЩАЕМ ЗНАЧЕНИЕ


# def hello_decorator(func):
    # def inner1(*args, **kwargs):
    #     print("before Execution")
# получение возвращаемого значения
        # returned_value = func(*args, **kwargs)
        # print("after Execution")
# возвращаем значение в исходный кадр
    #     return returned_value
    # return inner1

#добавляем декоратор в функцию
# @hello_decorator
# def sum_two_numbers(a, b):
#     print("Inside the function")
#     return a + b

# a, b = 1, 2

# получение значения через возврат функции
# sum = sum_two_numbers(a, b)
# print("Sum =", sum)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# ПРОСТО ТАК

# def decorator_glavniy(argument_function):
#     def wrapper_func(*args, **kwargs):
#         print(f'Wrapper executed this before {argument_function.name}')
#         return argument_function(*args, **kwargs)
#     return wrapper_func

# @decorator_glavniy
# def argument_function(*args):
#     print('Original function ran')

# x = [1,2,3,4,5]
# argument_function(x)

#  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# import time
# import math
# def calculate_time(func):
#     def inner1(*args,**kwargs):
#         begin = time.time()
#         func(*args, **kwargs)
#         end = time.time()
#         print('Total time taken in: ', func.name, end - begin)
#     return inner1

# @calculate_time

# def factorial_time(num):
#     time.sleep(2)
#     print(math.factorial(num))
# factorial_time(10)

#  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# memory = {}

# def memoize_factorial(original_func):
#     def inner(num):
#         if num not in memory:
#             memory[num] = original_func(num)
#             print('result saved in memory')
#         else:
#             print('FROM SAVED MEMORY:', memory[num])
#         return memory[num]
#     return inner

# @memoize_factorial
# def facto(num):
#     if num == 1:
#         return 1
#     else:
#         return num * facto(num-1)

# print(facto(5))
# print(facto(5))
# print(facto(3))
# print(memory)