# DECORATORS - БЕРЕТ ВСЕ ФУНКЦИИ В СЕБЯ  
# WRAPPER - ОБЕРТКА - 
# MEMOIZE - ДАЁТ ИЗ СВОЕЙ ПАМЯТИ 

#  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

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
import time
import math
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