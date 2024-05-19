import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TestAccountDetails(unittest.TestCase):
    _ran_tests = False  # Biến class để theo dõi xem các test đã được thực thi hay chưa

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get("https://practice.automationtesting.in/")
        self.driver.find_element(By.LINK_TEXT, "My Account").click()

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

    def check_registration(self, firstn, lastn, emailn, passwn, pass1n, pass2n):
        try:
            first = self.driver.find_element(By.NAME, "account_first_name")
            first.clear()
            first.send_keys(firstn)
            last = self.driver.find_element(By.NAME, "account_last_name")
            last.clear()
            last.send_keys(lastn)
            email = self.driver.find_element(By.NAME, "account_email")
            email.clear()
            email.send_keys(emailn)
            
            passw = self.driver.find_element(By.NAME, "password_current")
            passw.clear()
            passw.send_keys(passwn)
            pass1 = self.driver.find_element(By.NAME, "password_1")
            pass1.clear()
            pass1.send_keys(pass1n)
            pass2 = self.driver.find_element(By.NAME, "password_2")
            pass2.clear()
            pass2.send_keys(pass2n)
            self.driver.find_element(By.NAME, "save_account_details").click()
            time.sleep(5)
        # Kiểm tra xem phần tử có tồn tại không dựa trên XPath
            if self.driver.find_elements(By.XPATH, "//*[@id='page-36']/div/div[1]/div[2]/p[1]"):
                print(f"Pass: Account Details successful. {firstn, lastn, emailn, passwn, pass1n, pass2n}")
            else:
                print(f"Fail: Account Details failed. {firstn, lastn, emailn, passwn, pass1n, pass2n}")
                self.fail("Account Details failed.")

        except Exception as e:
            print(f"Error: {e}")
            self.fail("An error occurred during Account Details.")

    
    def test_Successful_changename_changepassword(self):
        firstn = "Giang",
        lastn = "Đinh",
        emailn = "dhuonggiang566@gmail.com",
        passwn = "Gimas+3006",
        pass1n =  "Dinh+3006giang",
        pass2n = "Dinh+3006giang",
        print("TC_01 Successful Change With name change and password change")
        result = self.check_registration(firstn, lastn, emailn, passwn, pass1n, pass2n)
    
        
    
    def test_Successful_change_name(self):
        firstn = "Giang",
        lastn = "Đinh",
        emailn = "dhuonggiang566@gmail.com",
        passwn = "",
        pass1n =  "",
        pass2n = "",
        print("TC_02 Successful Change With name change")
        result = self.check_registration(firstn, lastn, emailn, passwn, pass1n, pass2n)
        

    
    def test_Change_failed_with_empty(self):
        firstn = "",
        lastn = "ffdsfsfsfsf",
        emailn = "",
        passwn = "",
        pass1n =  "",
        pass2n = "",
        print("TC_03 Change failed with empty First name, empty Last name")
        result = self.check_registration(firstn, lastn, emailn, passwn, pass1n, pass2n)
        
    
    def test_Change_failed_wrong_password_current(self):
        firstn = "Giang",
        lastn = "Đinh",
        emailn = "dhuonggiang566@gmail.com",
        passwn = "3006giang",
        pass1n =  "Gimas3006",
        pass2n = "Gimas3006",
        print("TC_04 Change failed with entering the wrong current password")
        result = self.check_registration(firstn, lastn, emailn, passwn, pass1n, pass2n)
    
    
    def test_Change_failed_weak_NewPassword(self):
        firstn = "Giang",
        lastn = "Đinh",
        emailn = "dhuonggiang566@gmail.com",
        passwn = "Dinh+3006giang",
        pass1n =  "Gimas",
        pass2n = "Gimas",
        print("TC_05 Change failed with a weak New Password")
        result = self.check_registration(firstn, lastn, emailn, passwn, pass1n, pass2n)

     
    def test_Change_failed_ConfirmNewPassword_not_NewPassword(self):
        firstn = "Giang",
        lastn = "Đinh",
        emailn = "dhuonggiang566@gmail.com",
        passwn = "Dinh+3006giang",
        pass1n =  "Dinh+ngoc90",
        pass2n = "Giang566",
        print("TC_06 Change failed with Confirm New Password does not match New Password")
        result = self.check_registration(firstn, lastn, emailn, passwn, pass1n, pass2n)

    def test_test_Change_failed_with_no_change(self):
        firstn = "",
        lastn = "",
        emailn = "",
        passwn = "",
        pass1n =  "",
        pass2n = "",
        print("TC_07 Change failed with no change")
        result = self.check_registration(firstn, lastn, emailn, passwn, pass1n, pass2n)
    

    def setUp(self):
        self.driver.get("https://practice.automationtesting.in/")
        self.driver.find_element(By.LINK_TEXT, "My Account").click()
        
        self.driver.find_element(By.NAME, "username").send_keys("dhuonggiang566@gmail.com")
        self.driver.find_element(By.NAME, "password").send_keys("Gimas+3006")
        self.driver.find_element(By.NAME, "rememberme").click()
        self.driver.find_element(By.NAME, "login").click()
        self.driver.find_element(By.LINK_TEXT, "Account Details").click()

    @classmethod
    def tearDownClass(cls):
        TestAccountDetails._ran_tests = True 

if __name__ == '__main__':
    unittest.main()


        
