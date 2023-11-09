# from abc import ABC, abstractmethod

# class Animals(ABC):
#     def __init__(self, name, *args, **kwargs): # АРГУМЕНТ - self ЭТО ИМЯ ЖИВОТНОГО 
#         self.name = name 

#     def __str__(self): # ПРЕЗЕНТАЦИЯ РЕЗУЛЬТАТА
#         return f"Class {self.name}"

#     @abstractmethod
#     def get_info(self): # Это определение метода get_info, Метод возвращает информацию о животном.
#         raise NotImplementedError # Нереализованная ошибка



# # super().__init__(name)`: Эта строка вызывает конструктор 
# # родительского класса Animals и передает #  аргумент name.
# class Tiger(Animals):
#     def __init__(self, name:str, age:int, speed:int) -> None:
#         super().__init__(name) # вызывает конструктор класса Animals и передает аргумент name.
#         self.age = age
#         self.speed = speed

#     def get_info(self):
#         return f"{self.name} ему {self.age} лет, и он может бегать {self.speed} км/ч"

# tiger1 = Tiger("White tiger", 10, 25)
# print(tiger1)
# print(tiger1.get_info())

# from abc import ABC, abstractmethod

# class Books(ABC):
#     def __init__(self, name, pages:int, price:int):
#         self.name = name
#         self.pages = pages
#         self.price = price

#     def __str__(self):
#         return f"Book {self.name}"

#     @abstractmethod
#     def get_info(self):
#         raise NotImplementedError

# class EBooks(Books):
#     def __init__(self, name:str, pages:int, price:int, link:str):
#         super().__init__(name, pages, price)
#         self.link = link

#     def get_info(self):
#         return f'{self.name} can be found on the link: {self.link}'

#     def unique_fn(self):
#         return f'{self.name} is an ebook'

# class PBooks(Books):
#     def __init__(self, name: str, pages: int, price: int, weight: str):
#         super().__init__(name, pages, price)
#         self.weight = weight

#     def get_info(self):
#         return f'{self.name} weights: {self.weight}'

#     def unique_fn(self):
#         return f'{self.name} is a paper-book'


# ebook = EBooks("Harry Potter", 500, 100, "https://www.google.com")
# pbook = PBooks("Harry Potter 2", 500, 200, "500g")

# print(ebook)
# print(pbook)
# print(ebook.get_info())
# print(pbook.get_info())





# "abc" здесь означает абстрактный базовый класс. Сначала он импортируется, а затем используется как
# родительский класс для некоторого класса, который становится абстрактным классом. Его простейшая реализация
# можно сделать, как показано ниже.
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# RU: абстрактный класс - это класс, который не предназначен для создания экземпляров,
# а предназначен для использования в качестве родительского класса для других классов
# абстрактный метод - это метод, который объявлен, но не реализован в базовом классе.
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#  INHERITANCE - Наследование позволяет нам определить класс, который наследует все методы
# и свойства из другого класса.
# Parent class - Родительский класс — это класс, от которого наследуется, также называемый базовым классом.
# Child class - Дочерний класс — это класс, который наследуется от другого класса, также называемого производным классом.
# это способ создания нового класса для использования деталей существующего класса без его изменения.
# Вновь созданный класс является производным классом (или дочерним классом).
# Аналогично, существующий класс является базовым (или родительским классом).