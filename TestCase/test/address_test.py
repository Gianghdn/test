import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

class TestAddress(unittest.TestCase):
    _ran_tests = False  # Biến class để theo dõi xem các test đã được thực thi hay chưa

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get("https://practice.automationtesting.in/")

    @classmethod
    def tearDownClass(self):
        self.driver.quit()
        

    def check_billing(self, billing_info):
        self.driver.get("https://practice.automationtesting.in/my-account/")
        self.driver.find_element("name", "username").send_keys("dhuonggiang566@gmail.com")
        self.driver.find_element("name", "password").send_keys("Gimas+3006")
        self.driver.find_element("name", "rememberme").click()
        self.driver.find_element("name", "login").click()
        self.driver.find_element(By.PARTIAL_LINK_TEXT, "Addresses").click()
        self.driver.find_element(By.XPATH, "//*[@id='page-36']/div/div[1]/div/div/div[1]/header/a").click()

        try:
            self.driver.find_element(By.NAME, "billing_first_name").clear()
            self.driver.find_element(By.NAME, "billing_first_name").send_keys(billing_info["first"])

            self.driver.find_element(By.NAME, "billing_last_name").clear()
            self.driver.find_element(By.NAME, "billing_last_name").send_keys(billing_info["last"])

            self.driver.find_element(By.NAME, "billing_company").clear()
            self.driver.find_element(By.NAME, "billing_company").send_keys(billing_info["company"])

            self.driver.find_element(By.NAME, "billing_email").clear()
            self.driver.find_element(By.NAME, "billing_email").send_keys(billing_info["email"])

            self.driver.find_element(By.NAME, "billing_phone").clear()
            self.driver.find_element(By.NAME, "billing_phone").send_keys(billing_info["phone"])

            country = Select(self.driver.find_element(By.ID, "billing_country"))
            country.select_by_visible_text("Vietnam")

            self.driver.find_element(By.NAME, "billing_address_1").clear()
            self.driver.find_element(By.NAME, "billing_address_1").send_keys(billing_info["address"])

            self.driver.find_element(By.NAME, "billing_postcode").clear()
            self.driver.find_element(By.NAME, "billing_postcode").send_keys(billing_info["zip"])

            self.driver.find_element(By.NAME, "billing_city").clear()
            self.driver.find_element(By.ID, "billing_city").send_keys(billing_info["city"])

            self.driver.find_element("name", "save_address").click()
            time.sleep(5)

            
            success_message = self.driver.find_elements(By.PARTIAL_LINK_TEXT, "Sign out")
            if success_message:
                print("Pass: Billing Address successful.")
            else:
                print("Fail: Billing Address failed.")
            # Thêm lệnh fail() để báo hiệu cho hàm kiểm thử rằng quá trình đăng ký thất bại
                self.fail("Billing Address failed.")
        except Exception as e:
            print("Error:", e)
            self.fail("An error occurred during Billing Address.")

    def check_shipping(self, shipping_info):
        self.driver.get("https://practice.automationtesting.in/my-account/")
        self.driver.find_element("name", "username").send_keys("dhuonggiang566@gmail.com")
        self.driver.find_element("name", "password").send_keys("Gimas+3006")
        self.driver.find_element("name", "rememberme").click()
        self.driver.find_element("name", "login").click()
        self.driver.find_element(By.PARTIAL_LINK_TEXT, "Addresses").click()
        self.driver.find_element(By.XPATH, "//*[@id='page-36']/div/div[1]/div/div/div[2]/header/a").click()

        try:
            self.driver.find_element(By.NAME, "shipping_first_name").clear()
            self.driver.find_element(By.NAME, "shipping_first_name").send_keys(shipping_info["first"])

            self.driver.find_element(By.NAME, "shipping_last_name").clear()
            self.driver.find_element(By.NAME, "shipping_last_name").send_keys(shipping_info["last"])

            self.driver.find_element(By.NAME, "shipping_company").clear()
            self.driver.find_element(By.NAME, "shipping_company").send_keys(shipping_info["company"])

            country = Select(self.driver.find_element(By.ID, "shipping_country"))
            country.select_by_visible_text("Vietnam")

            self.driver.find_element(By.NAME, "shipping_address_1").clear()
            self.driver.find_element(By.NAME, "shipping_address_1").send_keys(shipping_info["address"])

            self.driver.find_element(By.NAME, "shipping_postcode").clear()
            self.driver.find_element(By.NAME, "shipping_postcode").send_keys(shipping_info["zip"])

            self.driver.find_element(By.NAME, "shipping_city").clear()
            self.driver.find_element(By.ID, "shipping_city").send_keys(shipping_info["city"])

            self.driver.find_element("name", "save_address").click()
            time.sleep(5)

            
            success_message = self.driver.find_elements(By.PARTIAL_LINK_TEXT, "Sign out")
            if success_message:
                print("Pass: shipping Address successful.")
            else:
                print("Fail: shipping Address failed.")
            # Thêm lệnh fail() để báo hiệu cho hàm kiểm thử rằng quá trình đăng ký thất bại
                self.fail("Billing Address failed.")
        except Exception as e:
            print("Error:", e)
            self.fail("An error occurred during Billing Address.")

    def test_TC1_Successful_Billing_the_corrent(self):
        billing_info = {
            "first" : "Giang",
            "last" : "Đinh",
            "company" : "CUNGOP",
            "email" : "dhuonggiang566@gmail.com",
            "phone" : "0339264512",
            "address" : "Đắk Lắk",
            "zip" : "073006",
            "city" : "Buôn Ma Thuột",
        }
        print("TC_01 Successful Add Billing Address with the correct full enter")
        result = self.check_billing(billing_info)

    def test_TC2_Success_Billing_item_blank(self):
        self.driver.find_element(By.PARTIAL_LINK_TEXT, "Logout").click()
        billing_info = {
            "first" : "Giang",
            "last" : "Đinh",
            "company" : "",
            "email" : "dhuonggiang566@gmail.com",
            "phone" : "0339264512",
            "address" : "Đắk Lắk",
            "zip" : "",
            "city" : "Buôn Ma Thuột",
        }
        print("TC_02 Successful Add Billing Address with leave the item blank optional")
        result = self.check_billing(billing_info)

    def test_TC3_FailBilling_empty_FirstLastname(self):
        self.driver.find_element(By.PARTIAL_LINK_TEXT, "Logout").click()
        billing_info = {
            "first" : "",
            "last" : "",
            "company" : "",
            "email" : "dhuonggiang566@gmail.com",
            "phone" : "0339264512",
            "address" : "Đắk Lắk",
            "zip" : "",
            "city" : "Buôn Ma Thuột",
        }
        print("TC_03 Add Billing Address failed with empty First name, empty Last name")
        result = self.check_billing(billing_info)

    def test_TC4_FailBilling_empty_PhoneCity(self):
        self.driver.find_element(By.PARTIAL_LINK_TEXT, "Logout").click()
        billing_info = {
            "first" : "Giang",
            "last" : "Đinh",
            "company" : "",
            "email" : "dhuonggiang566@gmail.com",
            "phone" : "",
            "address" : "",
            "zip" : "",
            "city" : "",
        }
        print("TC_04 Add Billing Address failed with empty Town/City, empty Phone")
        result = self.check_billing(billing_info)

    def test_TC5_Successful_Shipping_the_correct(self):
        self.driver.find_element(By.PARTIAL_LINK_TEXT, "Logout").click()
        shipping_info = {
            "first" : "Giang",
            "last" : "Đinh",
            "company" : "CUNGOP",
            "address" : "Đắk Lắk",
            "zip" : "073006",
            "city" : "Buôn Ma Thuột",
        }
        print("TC_05 Successful Add Shipping Address with the correct full enter")
        result = self.check_shipping(shipping_info)

    def test_TC6_FailShipping_empty_FirstLastname(self):
        self.driver.find_element(By.PARTIAL_LINK_TEXT, "Logout").click()
        shipping_info = {
            "first" : "",
            "last" : "",
            "company" : "CUNGOP",
            "address" : "Đắk Lắk",
            "zip" : "073006",
            "city" : "Buôn Ma Thuột",
        }
        print("TC_06 Add Shipping Address failed with empty First name, empty Last name")
        result = self.check_shipping(shipping_info)

    def test_TC7_FailShipping_empty_AddressCity(self):
        self.driver.find_element(By.PARTIAL_LINK_TEXT, "Logout").click()
        shipping_info = {
            "first" : "Giang",
            "last" : "Đinh",
            "company" : "CUNGOP",
            "address" : "",
            "zip" : "073006",
            "city" : "",
        }
        print("TC_07 Add Shipping Address failed with empty Address, empty Town/City")
        result = self.check_shipping(shipping_info)

    def test_TC8_FailShipping_invalidZIP(self):
        self.driver.find_element(By.PARTIAL_LINK_TEXT, "Logout").click()
        shipping_info = {
            "first" : "Giang",
            "last" : "Đinh",
            "company" : "CUNGOP",
            "address" : "Đắk Lắk",
            "zip" : "đinh ngọc",
            "city" : "Buôn Ma Thuột",
        }
        print("TC_08 Add Shipping Address failed with invalid Postcode/ZIP")
        result = self.check_shipping(shipping_info)

    def setUp(self):
        self.driver.get("https://practice.automationtesting.in/my-account/")
        


    @classmethod
    def tearDownClass(cls):
        TestAddress._ran_tests = True  # Đánh dấu rằng các test đã được thực thi

if __name__ == '__main__':
    unittest.main()