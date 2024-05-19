#Dinh+3006giang

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TestLogin(unittest.TestCase):
    _ran_tests = False  # Biến class để theo dõi xem các test đã được thực thi hay chưa

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get("https://practice.automationtesting.in/")

    

    def check_registration(self, user, password):
        
        self.driver.find_element(By.LINK_TEXT, "My Account").click()
        try:
            userid = self.driver.find_element(By.NAME, "username")
            userid.clear()
            userid.send_keys(user)
            
            passw = self.driver.find_element(By.NAME, "password")
            passw.clear()
            passw.send_keys(password)
            
            self.driver.find_element("name", "rememberme").click()
            time.sleep(1)
            self.driver.find_element(By.NAME, "login").click()
            time.sleep(1)
        # Kiểm tra xem phần tử có tồn tại không dựa trên XPath
            if self.driver.find_elements(By.PARTIAL_LINK_TEXT, "Dashboard"):
                print(f"Test is passed for login: {user, password}")
            else:
                print(f"Test is failed for login: {user, password}")
                self.fail("Login failed.")

        except Exception as e:
        # In ra lỗi nếu có
            print(f"Error: {e}")
            self.fail("An error occurred during Login.")

        

    def test_Successful_Login_with_correct(self):
        user = "dhuonggiang566@gmail.com"
        password = "Gimas+3006"
        print("TC_01 Successful Login With the correct email address and password")
        result = self.check_registration(user, password)

        self.driver.find_element(By.PARTIAL_LINK_TEXT, "Logout").click()

        
    
    def test_Failed_empty_email_password(self):
        user = ""
        password = ""
        print("TC_02 Login failed With  empty email address and empty password")
        result = self.check_registration(user, password)
        

    def test_Failed_empty_email(self):
        user = ""
        password = "Giangdinh%456hg"
        print("TC_03 Login failed With  empty email address and correct password")
        result = self.check_registration(user, password)
        

    def test_Failed_empty_password(self):
        user = "dhuonggiang566@gmail.com"
        password = ""
        print("TC_04 Login failed With correct email address and empty password")
        result = self.check_registration(user, password)
    
    def test_incorrect_email_password(self):
        user = "sfsfsf"
        password = "Evy0"
        print("TC_05 Login failed With incorrect email address and incorrect password")
        result = self.check_registration(user, password)
        
    def test_invalid_email_password(self):
        user = "sfsfsf"
        password = "Gimas+3006"
        print("TC_06 Login failed With incorrect email address and correct password")
        result = self.check_registration(user, password)

    def test_invalid_email_password(self):
        user = "dhuonggiang566@gmail.com"
        password = "Evy0"
        print("TC_07 Login failed With correct email address and incorrect password")
        result = self.check_registration(user, password)

    def setUp(self):
        self.driver.get("https://practice.automationtesting.in/")

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

    @classmethod
    def tearDownClass(cls):
        TestLogin._ran_tests = True
    pass 

if __name__ == '__main__':
    unittest.main()
