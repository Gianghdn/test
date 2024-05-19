import unittest
import time
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestLogout(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        
        # Cấu hình logging
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        self.logger = logging.getLogger(__name__)
        
        # Tạo handler cho việc ghi log vào file
        file_handler = logging.FileHandler('test.log')
        file_handler.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

    def test_login_logout(self):
        # Đăng nhập
        self.logger.info("Starting login test...")
        self.driver.get("https://practice.automationtesting.in/")
        self.driver.find_element(By.LINK_TEXT, "My Account").click()

        self.driver.find_element("name", "username").send_keys("dhuonggiang566@gmail.com")
        self.driver.find_element("name", "password").send_keys("Gimas+3006")
        self.driver.find_element("name", "rememberme").click()
        self.driver.find_element("name", "login").click()
        self.logger.info("Logged in successfully.")
        time.sleep(2)

        # Đăng xuất
        self.logger.info("Starting logout test...")
        self.driver.find_element(By.PARTIAL_LINK_TEXT, "Logout").click()
        self.logger.info("Logged out successfully.")
        time.sleep(5)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
