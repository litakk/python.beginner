# -- Статический метод ничего не знает о классе и занимается только параметрами.
# -- Метод класса работает с классом, поскольку его параметром всегда является сам класс.

# Ссылка о разнице 
# https://sparkbyexamples.com/python/python-difference-between-staticmethod-and-classmethod/#h-1-what-is-staticmethod

from datetime import date
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def fromBirthYear(cls, name, year):
        return cls(name, date.today().year - year)

    @staticmethod
    def isAdult(age):
        return age > 18

student1 = Student('Rolf', 19)
print(student1.isAdult(22))
print(student1.age)

student2 = Student.fromBirthYear('Anna', 1990)
print(student2.age)