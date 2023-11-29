# def piramida():
#     for q in range(8):
#         print( " " * (8 - 1 - q) + '*' * ( 1 + q * 2) )
# piramida()

#        *
#       ***
#      *****
#     *******
#    *********
#   ***********
#  *************
# ***************



# 1. Create a tuple with numbers and print one last item.
# ANSWER: 
# numbers = (1, 2, 3, 4, 5) 
# print(numbers[-1])

#  - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# 2. Create a tuple with numbers and check if a given element exists in the tuple.
# ANSWER: 
# numbers = (1, 2, 3, 4, 5)
# index = numbers.index(3)
# print(index)

#  - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# Create a tuple with numbers and find the number of occurrences
# of a given element in the tuple.
# ANSWER: 
# numbers = (1, 2, 3, 1, 1, 1)
# element = 1
# count = numbers.count(element)
# print(f"{element} раз встречался элемент: 1 в кортеже: {count}")

#  - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# Напишите функцию Python, которая принимает в качестве входных данных
# кортеж целых чисел и возвращает новый кортеж с теми же целыми числами,
# отсортированными в порядке убывания, но с четными числами перед нечетными.
# ANSWER: 
# def sort_tuple(numbers):
#     even = [x for x in numbers if x % 2 == 0]
#     odd = [x for x in numbers if x % 2 != 0]
#     even.sort(reverse=True)
#     odd.sort(reverse=True)
#     return tuple(even + odd)
# numbers = [5,4,7,2,6,9,8,3,1,0,10]
# result = sort_tuple(numbers)
# print(result)
#  - - - - - - - - - - - - - - - - - - - - - - - - - - - -