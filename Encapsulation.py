# Инкапсуляция
# используется для ограничения доступа к методам и переменным.
# Это предотвращает прямую модификацию данных, которая называется инкапсуляцией.
class Alpha:
    def __init__(self):
        self.test = "This is test"
        self._a = 2. # Защищенный член ‘a’ (для нас)
        self.__b = 2.  # Частный член  ‘b’

    def do_smth(self):
        return self.__b * 2
    
    @property
    def get_b(self):
        return self.__b

a = Alpha()
print(a.test)
print(a.get_b)
print(a.do_smth())