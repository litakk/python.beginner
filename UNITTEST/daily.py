def test_wikipedia(self):
        self.driver.get("https://www.wikipedia.org/")
        print("Getting url...")
        slogan = self.driver.find_element(By.CLASS_NAME, "localized-slogan")
        print(slogan)
        print("ID: -> ", slogan.get_property("id"))
        print("link.text: -> ", slogan.text)

        text_to_write = "FullStack programming"
        search_input = self.driver.find_element(By.ID, "searchInput")
        search_input.send_keys(text_to_write)
        time.sleep(HALF_SECOND)
        btn = self.driver.find_element(By.CLASS_NAME, "svg-search-icon")
        btn.click()
        time.sleep(HALF_SECOND*2)
        expected_heading = self.driver.find_element(By.ID, "firstHeading")
        assert expected_heading.text == "Search results"
        assert "Search results" in self.driver.page_source
import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


# https://chromedriver.chromium.org/downloads
PATH = "C:\\Users\\Admin\\Desktop\\python beginner\\UNITTEST\\chromedriver.exe"

HALF_SECOND = 0.5

class Fullstack(unittest.TestCase):

    def setUp(self):
        options = Options()
        # options.add_argument('--headless') # delete this if you want to see the browser
        self.driver = webdriver.Chrome(service=Service(PATH), 
                                        options=options)
        self.driver.minimize_window()
        # self.current_test = self.id().split(".")[-1]

    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        print(f"Ending test for {self.driver}")

    def test_login_to_facebook(self):
        pass

    def test_wikipedia(self):
        self.driver.get("https://www.wikipedia.org/")
        print("Getting url...")
        slogan = self.driver.find_element(By.CLASS_NAME, "localized-slogan")
        print(slogan)
        print("ID: -> ", slogan.get_property("id"))
        print("link.text: -> ", slogan.text)

        text_to_write = "FullStack programming"
        search_input = self.driver.find_element(By.ID, "searchInput")
        search_input.send_keys(text_to_write)
        time.sleep(HALF_SECOND)
        btn = self.driver.find_element(By.CLASS_NAME, "svg-search-icon")
        btn.click()
        time.sleep(HALF_SECOND*2)
        expected_heading = self.driver.find_element(By.ID, "firstHeading")
        assert expected_heading.text == "Search results"
        assert "Search results" in self.driver.page_source


# запустить этот тест из командной строки:
# python -m unittest -v functional_tests.py
# -v  =>  подробный режим (означает, что мы увидим все результаты теста)
# -m  =>  модуль (означает, что мы будем запускать тест из модуля)
