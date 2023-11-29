import random
import math
import time
# ВЫДАЕТ ТОЛЬКО 1 РАНДОМНЫЙ

names = [
    'a', 'b','c','d','e',
    'f','g','h','i','j',
]
r = random.choice(names)
print(r)

# - - - - - - - - - - - - - - - - - - - - - 

# ПЕРЕМЕШИВАЕТ ЛИСТ В РАНДОМНОМ ПОРЯДКЕ

names = [
    'a', 'b','c','d','e',
    'f','g','h','i','j',
]
random.shuffle(names)
print(names)

# - - - - - - - - - - - - - - - - - - - - - 

# УДАЛЯЕТ ВСЁ ПОСЛЕ ЗАПЯТОЙ 
x = math.trunc(1.2144)
print(x)

# - - - - - - - - - - - - - - - - - - - - - 

# ДАЁТ ЧТО БЛИЖЕ  
x = round(5.5)
print(x)
 # 6
x = round(5.4)
print(x)
 # 5

# - - - - - - - - - - - - - - - - - - - - - 

# УМНОЖАЕТ ВСЁ ДРУГ НА ДРУГА 
# EXAMPLE: 5 * 4 * 3 * 2 * 1
x = math.factorial(5)
print(x)
# 120
# - - - - - - - - - - - - - - - - - - - - - 

# Функция `math.gcd()` наибольший общий делитель чисел 105, 45 и 30 равен 15.

x = math.gcd(105, 45, 30)
print(x)

# - - - - - - - - - - - - - - - - - - - - - 

# Код вычисляет квадратный корень числа 64
x = math.sqrt(64)
print(x)

# - - - - - - - - - - - - - - - - - - - - - 

# считает время в милисекундах с 1970 
r = time.time()
print(r)
#  result => 1700576051.7460122

# - - - - - - - - - - - - - - - - - - - - - 

# Даёт информацию о дате часах и годах с нашего ПК
r = time.localtime()
print(r)

# - - - - - - - - - - - - - - - - - - - - - 

# Даёт время на данный момент / даёт информацию с нашего ПК
import datetime
r = datetime.datetime.now()
print(r)

# - - - - - - - - - - - - - - - - - - - - -