############### Polymorphism - Полиморфизм позволяет определить один интерфейс и иметь несколько реализаций.
# Полиморфизм означает «множество форм», и он возникает, когда у нас есть много классов, связанных друг с другом наследованием.
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Dog(Animal):
    def speak(self):
        return self.name+' says Woof!'

class Cat(Animal):
    def speak(self):
        return self.name+' says Meow!'

dog = Dog("Max")
print(dog.speak())
cat = Cat("Alice")
print(cat.speak())

############################################################################################
############### Encapsulation
# is used to restrict access to methods and variables.
# This prevents data from direct modification which is called encapsulation.

class Alpha:
    def __init__(self):
        self.test = "This is test"
        self._a = 2.  # Protected member ‘a’ (for us)
        self.__b = 2.  # Private member ‘b’

    def do_smth(self):
        return self.__b * 2
    
    @property
    def get_b(self):
        return self.__b

a = Alpha()
print(a.test)
print(a.get_b)
print(a.do_smth())

############################################################################################
################### DECORATORS

# @property   — это встроенный декоратор в Python, который используется для определения свойств
# № объекта. Декоратор @property упрощает работу,
# автоматически вызываем метод получения при доступе к значению атрибута.

# @classmethod — это встроенный декоратор в Python, который используется для создания методов класса.
# Метод класса может быть вызван как классом, так и объектом.
# Этот метод принимает класс в качестве первого аргумента, который передается автоматически
# при вызове метода.

# @staticmethod — встроенный декоратор Python, определяющий статический метод.
# Статический метод не получает никаких ссылочных аргументов, независимо от того, вызывается ли он
# экземпляр класса или сам класс. Это означает, что статический метод не может ни
# изменить состояние объекта или состояние класса. Статические методы ограничены в том, какие данные они могут использовать.
# доступ - и это в первую очередь способ размещения имен ваших методов.

# -- Static -- Статический метод ничего не знает о классе и занимается только параметрами.
# --  Class -- метод класса работает с классом, поскольку его параметром всегда является сам класс.
# Ссылка о разнице двух декораторов:
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




####################################################################################
####################################################################################
_3 = 'Dunder methods'

from abc import ABC, abstractmethod
# __...__


class AbstractUserClass(ABC):
    name: str
    surname: str
    age: int
    email: str

    @abstractmethod
    def get_info(self):
        raise NotImplementedError(
            "This is an abstract method and needs to be implemented in the child class.")


class User(AbstractUserClass):
    def __init__(self, name: str, surname: str, age: int = 0, email: str = '') -> None:
        self.name = name
        self.surname = surname
        self.age = age
        self.email = email

    def __str__(self) -> str:
        return f'{self.name} {self.surname} is {self.age} years old.\nEmail: {self.email}'
    

    def __repr__(self) -> str:
        return f'{self.name} {self.surname} is {self.age} years old.\nEmail: {self.email}'

    def __call__(self, *args, **kwargs):
        print(f"Это вызов из __call__")
        for i in args:
            print(i)
        return ''
        # ex:
        # user1("test1", "test2", "test3")  => This is call fn from __call__

    def __add__(self, other):
        return "This user has $" + str(other.budget)

    def get_info(self):
        print(f'{self.name} {self.surname}')
        return ''

    @classmethod
    def from_string(cls, string):
        if not string.count(',') == 3:
            raise Exception("String must have 4 values separated by comma.")

        # string  =>  "John, Doe, 25, test@gmail.com"
        splitted_str = string.split(",")
        name, surname, age, email = splitted_str
        # name = splitted_str[0]
        # surname = splitted_str[1]
        # age = splitted_str[2]
        # email = splitted_str[3]
        return cls(name, surname, int(age), email)

    @staticmethod
    def is_adult(age):
        return age > 18


class Client(User):
    def __init__(self, name: str, surname: str, budget: float) -> None:
        super().__init__(name, surname)
        self.budget = budget

    def __str__(self) -> str:
        return f'{self.name} {self.surname} has ${self.budget} budget.'

    def __repr__(self) -> str:
        return f'{self.name} {self.surname} has ${self.budget} budget.'

    def get_info(self):
        print(f'{self.name} {self.surname} has ${self.budget} budget.')
        return ''


# =================================================
user1 = User('John', 'Doe', 25, 'test@gmail.com')
print(user1.get_info())
# =================================================
client1 = Client("Cathrine", "Mackwold", 10000)
print(client1.get_info())
# =================================================
result = user1 + client1
print(result)
# =================================================
user1 = User.from_string("John, Doe, 25, test@gmail.com")  # classmethod
print(user1)
print(User.is_adult(user1.age))  # staticmethod