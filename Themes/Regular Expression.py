# REGULAR EXPRESSION - РЕГУЛЯРНОЕ ВЫРАЖЕНИЕ
# РАБОТА С ТЕКСТОМ

# - - - - - - - - - - - - - - - - - - - 
import re

# re.findall(pattern, string) - НАХОДИТ ВСЕ СОВПАДАЮЩИЕСЯ ЗНАЧЕНИЯ  
text = 'The rain is Spain'
result = re.findall('i',text)
print(result)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# re.search(pattern, string) - ДАЕТ МЕСТОПОЛОЖЕНИЕ ЗНАЧЕНИЯ В ИНДЕКСАХ
text = 'The rain in Spain'
r = re.search('rain', text) 
print(r)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# УБИРАЕТ ТО ЧТО ПРИСУТСТВУЕТ В ПРАВИЛАХ
text = 'The rain in Spain'
regex = re.compile(r'@[A-Za-z0-9]')  # compile создает регулярное выражение
r = re.split(regex,text)
print(r)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
x = 'ab ab ab ab'
original_text = 'The rain in Spain'
replacement = "*"
r = re.sub(
    r'ab',                            # ЧТО МЕНЯТЬ
    replacement,                      # ОТКУДА МЕНЯТЬ
    original_text,                    # НА ЧТО МЕНЯТЬ
    count=2,                          # Сколько менять
    flags=re.IGNORECASE               #  указывает, что замена должна производиться без учёта регистра.
)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# compile - создает регулярное выражение
# re.compile(r'[a-z]*)
# - - - - - - 
# re.compile(r'[a-z])
# print(re)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# x = r"[a-z]"
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# APPENDLEFT - ДОБАВЛЯЕТ СЛЕВА
# ROTATE - МЕНЯЕТ МЕСТА С НАЧАЛА В КОНЕЦ
import collections
queue = collections.deque()
queue.append(5)
queue.append('Mine')
queue.append(True)
queue.appendleft(10)
print(queue)
queue.rotate(2) # меняет местами индексы
print(queue)