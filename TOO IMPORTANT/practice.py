# x = [1, 2, 3]
# a = x[0]
# b = x[1]
# c = x[2]
# a, b, c = x
# print(a, b, c, sep="-")
# --- --- --- --- --- --- --- --- --- --- --- ---
# import random
# main = random.randrange(1, 13)  # 0, 2, 4, 6, 8
# print(main)
# --- --- --- --- --- --- --- --- --- --- --- ---
# random.random()    # gives random float number between 0 and 1
# --- --- --- --- --- --- --- --- --- --- --- ---
# x = 'lorem loremlorem loremloremloremlorem  loremlorem'.swapcase()     # Swaps cases, lower case 
# print(x)
# # --- --- --- --- --- --- --- --- --- --- --- ---
# x = "Updated"
# p = 'hello'
# z1 = "Test text for {var} checking .format()".format(var=x)
# z2 = f"Test text for {p} checking .format()".format(var=p)
# print(z1)
# print(z2)
# --- --- --- --- --- --- --- --- --- --- --- ---
# x = ["Text 1", "Text 2", "Text 3"]
# print("|".join(x))  # Text 1|Text 2|Text 3
# print("".join(x))   # Text 1Text 2Text 3
# print(" ".join(x))   # Text 1 Text 2 Text 3
# --- --- --- --- --- --- --- --- --- --- --- ---
# z = ['Hello', 'World', 'Again']
# print(" - ".join(z))
# --- --- --- --- --- --- --- --- --- --- --- ---
# test_txt = "Hello"
# print(test_txt.ljust(20, "*"))
# print(test_txt.rjust(20, "*"))
# --- --- --- --- --- --- --- --- --- --- --- ---
# x = "   Hello world   "
# print(x.strip())  # "Hello world" => УБИРАЕТ ПРОБЕЛЫ В НАЧАЛЕ И В КОНЦЕ
# --- --- --- --- --- --- --- --- --- --- --- ---
# x = "Text 1, Text 2, Text 3"
# print(list(x)) привет

# - - -  - - - - - - - - - - - -

# First = int(input("Введите 1 значение: "))
# Second = int(input("Введите 2 значение: "))
# Third = input("Введите оператор: ")

# result = 0
# if Third == "+":
#     result = First + Second
# elif Third == "-":
#     result = First - Second
# print(result)


# arr = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
# for idx, item in enumerate(arr):
#     print(idx, item)
    
    
    
    
# a = [a for a in range(1,11)]
# b = [i**2 for i in range(1,11)]
# print(a)


# Генераторы словарей Python | Dictionary comprehension python
#  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# key:value
# b = {i:i**2 for i in range(1,11)}
# print(b)
#  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# ЦИКЛ - FOR
# a = {}
# for i in range(1,11):
#     a[i] = i**2
# print(a)
#  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# a = {word:len(word) for word in ["hello", "hi", "www"]}
# print(a[])
#  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# ЦИКЛ - FOR
# my_dict = {"apple": 5, "banana": 3, "orange": 10}
# for key, value in my_dict.items():    
#     print(key, value)
#  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# my_dict = {"apple": 5, "banana": 3, "orange": 10} 
# {key:value for key, value in my_dict.items()}
# print(my_dict)
#  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# dic = {i:len(i) for i in ["orange", "apple"]}
# print(dic)
#  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


# 5 ЗАДАНИЕ Напишите скрипт Python для печати словаря, где ключи - числа
# b = {i:i*2 for i in range(1,16)}
# print(b)

#  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# 7 ЗАДАНИЕ Напишите программу Python для умножения всех элементов в словаре. 
# my_dict = {"key1": "10", "key2": 'qwe', "key3": 5}
# product = 1
# for value in my_dict.values():
#     if isinstance(value, (int, float)):
#         product += value
# print(product)

#  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# 8  Напишите программу Python для удаления ключа из словаря.
# def remove_key(dictionary, key):
#     if key in dictionary:
#         del dictionary[key]
#         print(f"Ключ '{key}' успешно удален из словаря.")
#     else:
#       print(f"Ключ '{key}' не найден в словаре.")  
# my_dict = {"name": "John", "age": 30, "city": "New York"}
# print("Исходный словарь:")
# print(my_dict)
# remove_key(my_dict, "age")
# print("Обновленный словарь:")
# print(my_dict)

#  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# 9 Напишите программу Python для сортировки заданного словаря по ключу.
# diction = {4: 'd', 2: 'b', 1: 'a', 3: 'c'}
# print('Before sorted', diction)
# sorted = dict(sorted(diction.items()))
# print('After sorted', sorted)

#  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# 10 Напишите программу Python, чтобы получить максимальное и минимальное значение в словаре.
# dictionary = {"a": 2, "b": 5, "c": 1, "d": 10, "e": 7}
# def get_min_max(dictionary):
#     if len(dictionary) > 0:
#         min_value = min(dictionary.values())
#         max_value = max(dictionary.values())
#         return min_value, max_value
#     else:
#         return None
# print(get_min_max(dictionary))

#  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
