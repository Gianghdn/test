import os
import unittest
import xmlrunner
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import inspect

class Register(unittest.TestCase):
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

    def check_registration(self, email, password):
        try:
            emailid = self.driver.find_element(By.NAME, "email")
            emailid.clear()
            emailid.send_keys(email)
            passw = self.driver.find_element(By.ID, "reg_password")
            passw.clear()
            passw.send_keys(password)
            time.sleep(1)
            self.driver.find_element(By.NAME, "register").click()
            time.sleep(3)
        # Kiểm tra xem phần tử có tồn tại không dựa trên XPath
            if self.driver.find_elements(By.PARTIAL_LINK_TEXT, "Dashboard"):
                print(f"Test is passed for login: {email, password}")
            else:
                print(f"Test is failed for login: {email, password}")
                self.fail("Registration failed.")

        except Exception as e:
        # In ra lỗi nếu có
            print(f"Error: {e}")
            self.fail("An error occurred during Registration.")

        

    def test_Successful_registration_correct(self):
        email = "Minh2013@gmail.com"
        password = "Giangdinh%456hg"
        print("TC_01 Successful registration With the correct email address and password")
        result = self.check_registration(email, password)
        
    
    def test_Failed_empty(self):
        email = ""
        password = ""
        print("TC_02 Registration failed With  empty email address and empty password")
        result = self.check_registration(email, password)
        

    def test_Failed_invalid_email(self):
        email = "mngr550"
        password = "Giangdinh%456hg"
        print("TC_03 Registration failed With an improperly formatted Email address (invalid Email)")
        result = self.check_registration(email, password)
        

    def test_Failed_weak_password(self):
        email = "Cung082021@gmail.com"
        password = "Evyy"
        print("TC_04 Registration failed With a weak password")
        result = self.check_registration(email, password)
    
    def test_invalid_email_password(self):
        email = "sfsfsf"
        password = "Evy0"
        print("TC_05 Registration failed With invalid email and weak password")
        result = self.check_registration(email, password)
        

    def setUp(self):
        self.driver.get("https://practice.automationtesting.in/")
        self.driver.find_element(By.LINK_TEXT, "My Account").click()

    @classmethod
    def tearDownClass(cls):
        Register._ran_tests = True 

if __name__ == '__main__':
    # đường dẫn để lưu thư mục
    report_dir = r'C:\Chuyende\report'
    if not os.path.exists(report_dir):
        os.makedirs(report_dir)
    
    # sau khi chạy xong sẽ được lưu vô
    xml_report_path = os.path.join(report_dir, 'test_results.xml')
    unittest.main(
        testRunner=xmlrunner.XMLTestRunner(output=xml_report_path),
        
    )
    # Create a test suite
    test_loader = unittest.TestLoader()
    test_suite = test_loader.loadTestsFromTestCase(Register)

    # Run tests and generate XML report
    with open(xml_report_path, 'wb') as xml_report:
        runner = xmlrunner.XMLTestRunner(output=xml_report)
        runner.run(test_suite)


    unittest.main()
