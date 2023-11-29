# 1. max() - Возвращает наибольший элемент в итерируемом объекте или наибольший из двух или более аргументов. 
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# max(iterable, *[, key, default]) 
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# Если предоставлено два или более позиционных аргумента, возвращается наибольший из позиционных аргументов. 
# max(arg1, arg2, *args[, key]) 
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# Есть два необязательных аргумента только ключевых слов. 
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# key- ключевая функция, в которой передаются итерируемые объекты, и сравнение выполняется на основе возвращаемого значения 
# iterable = ['geeks', 'code', 'python', 'java'] 
# max(iterable, key=len)   

# peremenaya = ['text', 'banana', 'keys']
# max(peremenaya, key=len)

# iterable = [30, 15, 20, 25, 30] 
# print(max(iterable, key=lambda x: x%15))  => 25 
# EX: 
#   iterable = [] 
#   max(iterable, default=100)  =>  100 
#   max(iterable) => ValueError: аргумент max() — пустая последовательность
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# 2. min() - Работает так же, как max(), но возвращает наименьшее значение.
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# 3. map() - Возвращает объект отображения (который является итератором) результатов после применения заданной функции к каждому элементу заданного итерируемого объекта (список, кортеж и т. д.) 
#           EX: 
#               def wordCount(n): 
#                   return len(n) 
#                 Или мы могли бы использовать:
#                 wordCount = lambda n: len(n) 
#               x = map(wordCount, ('apple', 'banana', 'cherry')) 
#               print(list(x))  => [5, 6, 6] 
# ------------------------------------------------------------------------------ 
# 4. filter() - Используйте функцию фильтра, чтобы исключить элементы в итерируемом объекте 
#              EX:  
# def myFunc(n): 
#  if n > 18: 
    #                     return True 
    #                 else: 
    #                     return False 
                    # return True if n > 18 else False 
                #   return n > 18 
# x = filter(myFunc, (5, 7, 18, 25, 32)) 
# print(list(x))  

# Функция обратного вызова должна возвращать True / False в зависимости от значения в итерируемом объекте 
# ------------------------------------------------------------------------------ 
# 5. reduce() - Используйте функцию для сокращения итерируемого объекта до одного значения 
#           EX: 
# from functools import reduce 
# numbers = [1, 2, 3, 4, 5]
# def add(x, y):
#     return x + y
# sum_numbers = reduce(add, numbers)
# print("Сумма чисел:", sum_numbers)




# =>  10 
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# x = map(lambda x: x*2, arr) 
# print(list(x)) 
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -  
# def myFunc(current, next): 
#     if current > next: 
#         print("current > next", current) 
#         return current









#          - LAMBDA -
# print((lambda a,b: a * b)(17,14))
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -  
#        - DEF FUNCTION -   
# def myFunc(a,b):
#     return a * b
# print(myFunc(17,14))
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -  


# 45 - 9 = 36
# 36  =>  Odd  || Even


# from functools import reduce

# def sum_and_compare(arr:list[int]) -> None:
#     summ = reduce(lambda x,z: x+z, arr)
#     maximum = max(arr)
#     diff = summ - maximum
#     print(f"{diff} Even" if   diff%2==0   else f"{diff} Odd")

# x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# sum_and_compare(x)

