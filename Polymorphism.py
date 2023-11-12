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