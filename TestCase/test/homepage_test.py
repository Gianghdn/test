import os
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import inspect

class TestHomePage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get("https://practice.automationtesting.in/")

    def test_TC_01_home_screen(self):
        print("TC_01 Home Page")
        print("\nClassname : " + self.__class__.__name__)
        print("Running Test Method : " + inspect.stack()[0][3])

    def test_TC_02_search(self):
        self.driver.find_element(By.NAME, "s").send_keys("selenium", Keys.RETURN)
        time.sleep(2)
        print("TC_02 Button Search")
        print("\nClassname : " + self.__class__.__name__)
        print("Running Test Method : " + inspect.stack()[0][3])

    def test_TC_03_shop(self):
        self.driver.find_element(By.LINK_TEXT, "Shop").click()
        time.sleep(2)
        print("TC_03 Button Shop")
        print("\nClassname : " + self.__class__.__name__)
        print("Running Test Method : " + inspect.stack()[0][3])

    def test_TC_04_my_account(self):
        self.driver.find_element(By.LINK_TEXT, "My Account").click()
        time.sleep(2)
        print("TC_04 Button My Account")
        print("\nClassname : " + self.__class__.__name__)
        print("Running Test Method : " + inspect.stack()[0][3])

    def test_TC_05_testcases(self):
        self.driver.find_element(By.LINK_TEXT, "Test Cases").click()
        time.sleep(2)
        print("TC_05 Button Test Cases")
        print("\nClassname : " + self.__class__.__name__)
        print("Running Test Method : " + inspect.stack()[0][3])
    
    def test_TC_06_AT_Site(self):
        self.driver.find_element(By.LINK_TEXT, "AT Site").click()
        time.sleep(2)
        print("TC_06 Button AT Site")
        print("\nClassname : " + self.__class__.__name__)
        print("Running Test Method : " + inspect.stack()[0][3])

    def test_TC_07_Demo_Site(self):
        self.driver.find_element(By.LINK_TEXT, "Demo Site").click()
        time.sleep(2)
        print("TC_07 Button Demo Site")
        print("\nClassname : " + self.__class__.__name__)
        print("Running Test Method : " + inspect.stack()[0][3])

    def test_TC_08_icon_shopping(self):
        self.driver.find_element(By.XPATH, "//*[@id='wpmenucartli']/a").click()
        time.sleep(2)
        print("TC_08 Button icon Shopping")
        print("\nClassname : " + self.__class__.__name__)
        print("Running Test Method : " + inspect.stack()[0][3])

    def setUp(self):
        self.driver.get("https://practice.automationtesting.in/")

    @classmethod
    def tearDownClass(cls):
        TestHomePage._ran_tests = True
    pass

if __name__ == '__main__':
    unittest.main()
