import os
import unittest
import xmlrunner
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import inspect

class LogOut(unittest.TestCase):

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
    test_suite = test_loader.loadTestsFromTestCase(LogOut)

    # Run tests and generate XML report
    with open(xml_report_path, 'wb') as xml_report:
        runner = xmlrunner.XMLTestRunner(output=xml_report)
        runner.run(test_suite)


    unittest.main()
