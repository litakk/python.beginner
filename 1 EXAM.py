

# 6. Write a Python program to remove duplicates from the dictionary.
# First, leave at least one item from duplicates
# Second, delete all duplicates
# RU: Напишите программу Python для удаления дубликатов из словаря.
# Во-первых, оставьте хотя бы один элемент из дубликатов
# Во-вторых, удалите все дубликаты
def rem_duplicates(dict):
    pass
# ex: {'x':1, 'y':2, 'z':2, 'a':3, 'b':1, 'c':3}
# =>  {x':1, 'y':2, 'a':3}


# RU: Вот как будет выглядеть программа для удаления дубликатов из словаря:

def rem_duplicates(dict):
    # создаем пустой словарь, в который будем добавлять уникальные элементы
    unique_dict = {}

    # проходим по элементам переданного словаря
    for key, value in dict.items():
        # проверяем, есть ли уже такой элемент в unique_dict
        if value not in unique_dict.values():
            # если элемент уникален, добавляем его в unique_dict
            unique_dict[key] = value

    return unique_dict

# тест программы
dict = {'x': 1, 'y': 2, 'z': 2, 'a': 3, 'b': 1, 'c': 3}

unique_dict = rem_duplicates(dict)
print(unique_dict) # выводит: {'x': 1, 'y': 2, 'a': 3}

# ==========================================================================


# 7. Write a function that takes a dict as first argument and number as second argument.
# Return a list of all the keys that have values greater than the number passed as second argument.
# RU: Напишите функцию, которая принимает словарь в качестве первого аргумента и число в
# качестве второго аргумента. Верните список всех ключей, у которых значения больше, чем число,
# переданное в качестве второго аргумента.
# Input:   {'a': 100, 'b': 200, 'c': 300, 'd': "Hello world", 'e': True},    150
# Output:  {'b': 200, 'c': 300}
def get_keys_greater_than(dict, num):
    pass


# ==========================================================================


# 8. Write a function that takes a dictionary as an argument and returns
# a new dictionary with the keys and values reversed.
# RU: Напишите функцию, которая принимает словарь в качестве аргумента
# и возвращает новый словарь с обратными ключами и значениями.
def reverse_dict(d):
    pass


# ==========================================================================


# 9. Write a function that takes a list of dictionaries as an argument
# and returns a sum of numeric values of all dicts
# RU: Напишите функцию, которая принимает список словарей в качестве аргумента
# и возвращает сумму числовых значений всех словарей
x = {'a': 1, 'b': "2", "c": "Hello"}
z = {'d': "4", 'e': 3, "f": "World"}
a = {'g': 5, 'h': "!!!", "i": "6"}
arr = [x, z, a]
# test(arr)  #  21
def sum_numeric_values(arr_of_dicts: list[dict]) -> int:
    pass