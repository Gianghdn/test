import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestLogout(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def test_login_logout(self):
        # Đăng nhập
        self.driver.get("https://practice.automationtesting.in/")
        self.driver.find_element(By.LINK_TEXT, "My Account").click()

        self.driver.find_element("name", "username").send_keys("dhuonggiang566@gmail.com")
        self.driver.find_element("name", "password").send_keys("Gimas+3006")
        self.driver.find_element("name", "rememberme").click()
        self.driver.find_element("name", "login").click()
        time.sleep(2)

        self.driver.find_element(By.PARTIAL_LINK_TEXT, "Logout").click()
        time.sleep(5)


    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
