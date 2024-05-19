import os
import unittest
import xmlrunner
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import inspect

class HomePage(unittest.TestCase):

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
    
    def test_TC_06_AT_Site(self):
        self.driver.find_element(By.LINK_TEXT, "AT Site").click()
        time.sleep(2)
        print("TC_06 Button AT Site")

    def test_TC_07_Demo_Site(self):
        self.driver.find_element(By.LINK_TEXT, "Demo Site").click()
        time.sleep(2)
        print("TC_07 Button Demo Site")

    def test_TC_08_icon_shopping(self):
        self.driver.find_element(By.XPATH, "//*[@id='wpmenucartli']/a").click()
        time.sleep(2)
        print("TC_08 Button icon Shopping")

    def setUp(self):
        self.driver.get("https://practice.automationtesting.in/")

    @classmethod
    def tearDownClass(cls):
        HomePage._ran_tests = True
    pass


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
    test_suite = test_loader.loadTestsFromTestCase(HomePage)

    # Run tests and generate XML report
    with open(xml_report_path, 'wb') as xml_report:
        runner = xmlrunner.XMLTestRunner(output=xml_report)
        runner.run(test_suite)


    unittest.main()
