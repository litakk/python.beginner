# ТЕСТИРОВЩИКИ НУЖНЫ ДЛЯ ПРОВЕРКИ ВСЕГО BACK-END и FRONT-END 
# UNITTEST - ПРОВЕРЯЕТ КАЖДЫЙ ЭЛЕМЕНТ ДО КАЖДОЙ МЕЛОЧИ
# FRONT-END - E2E - ПРОВЕРЯЕТ, ОТ НАЧАЛА ДО КОНЦА - КНОПКИ, СТРАНИЦЫ, И.Т.Д
# TEST DRIVEN DEVELOPMENT - ПОЗВОЛЯЕТ ПОЛНОСТЬЮ ИМЕТЬ МАКЕТ САЙТА(ОПИСАТЬ САЙТ)
# ПОСЛЕ ПРИЗЫВА И ЗАПУСКА unittest ПОЯВЛЯЕТСЯ ПАПКА PYCACHE ИСХОДИТ ОТ С++ ДЛЯ ТОГО ЧТО БЫ ПРОЧИТАТЬ КОД БЫСТРО
# UNITTEST - КОНКРЕТНО ПОКАЗЫВАЕТ ОШИБКУ
# Для запуска определенного теста из командной строки:
# python -m unittest -v function_tests.py
#  -    -    - 
# assert 2 == 1
#  -    -    - 
# def my_f():
#     return 2 + 2

# assert my_f() == 4

#  -    -    -   -    -    -   -    -    -   -    -    -   -    -    - 

import unittest

class MyTest(unittest.TestCase):
    
    def setUP(self):
        self.var = 1

    def tearDown(self):
     self.var = None
      
    def test_1(self):
        self.assertEqual(1,1)
        
    def test_2(self):
        self.assertNotEqual(1,2)

    def test_3(self):
        self.assertTrue(True)
        
    def test_4(self):
        self.assertFalse(False)
        
    def test_5(self):
        self.assertIs(1,1)

    def test_6(self):
        self.assertIsNone(None)
        
    def test_7(self):
        self.assertIn(1,[1,2,3])
        
    def test_8(self):
        self.assertIs(1,1)