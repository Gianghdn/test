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
        self.driver.get("https://www.ttn.edu.vn/")

    def test_TC1_Thoi_Khoa_Bieu(self):
        self.driver.get("https://www.ttn.edu.vn/?option=com_tnu&view=sinhvien")
        self.driver.find_element( By.ID, "fmsv").send_keys("20103109")
        self.driver.find_element( By.XPATH, '//*[@id="tdiv"]/input[2]').click()


        time.sleep(2)
        print("TC_01 Thời khóa biểu sinh viên")

    def test_TC2_KQHT(self):
        self.driver.get("https://www.ttn.edu.vn/?option=com_tnu&view=kqchinhquy")
        self.driver.find_element( By.ID, "fmsv").send_keys("20103109")
        self.driver.find_element( By.XPATH, '//*[@id="tdiv"]/form/input[2]').click()
        self.driver.execute_script("window.scrollBy(200,600);")

        time.sleep(5)
        print("TC_02 Kết quả học tập sinh viên")

    def test_TC3_Ngoại_ngữ_Tin_học(self):
        self.driver.get("https://www.ttn.edu.vn/index.php/ttnnth")
        self.driver.find_element(By.PARTIAL_LINK_TEXT, "22-23/6/2024").click()

        self.driver.find_element(By.XPATH, '//*[@id="attachmentsList_com_content_article_5519"]/table/tbody/tr/td[1]/a[2]').click()
        time.sleep(5)
        print("TC_03 Trung tâm Ngoại ngữ Tin học")


    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
