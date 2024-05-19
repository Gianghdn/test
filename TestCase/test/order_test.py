#9. Order
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time

class TestShoppingOrder(unittest.TestCase):
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

    def  check_add (self):
        self.driver.get("https://practice.automationtesting.in/my-account/")
        self.driver.find_element("name", "username").send_keys("dhuonggiang566@gmail.com")
        self.driver.find_element("name", "password").send_keys("Gimas+3006")
        self.driver.find_element("name", "rememberme").click()
        self.driver.find_element("name", "login").click()

        self.driver.find_element(By.LINK_TEXT, "Shop").click()#icon shop

        element = self.driver.find_element(By.XPATH, '//*[@id="woocommerce_price_filter-2"]/form/div/div[2]/button')
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)# Cuộn trang web xuống vị trí của phần tử
        self.driver.find_element(By.XPATH, '//*[@id="content"]/ul/li[1]/a[1]').click()#ấn vào sách
        self.driver.find_element(By.XPATH, '//*[@id="product-169"]/div[2]/form/button').click()#nút add to basket
        time.sleep(2)
        self.driver.find_element(By.PARTIAL_LINK_TEXT, "VIEW BASKET").click()

    def check_free(self):
        self.driver.get("https://practice.automationtesting.in/my-account/")
        self.driver.find_element("name", "username").send_keys("dhuonggiang566@gmail.com")
        self.driver.find_element("name", "password").send_keys("Gimas+3006")
        self.driver.find_element("name", "rememberme").click()
        self.driver.find_element("name", "login").click()

        self.driver.find_element("id", "wpmenucartli").click()#icon shopping
        

    def check_billing(self, billing_info):
       
        self.driver.find_element(By.PARTIAL_LINK_TEXT, "PROCEED TO CHECKOUT").click()
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

            element = self.driver.find_element(By.XPATH, '//*[@id="order_review"]/table/tfoot/tr[1]')
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)# Cuộn trang web xuống vị trí của phần tử
            

            self.driver.find_element("id", "place_order").click() 
            element = self.driver.find_element(By.TAG_NAME, "body").send_keys(Keys.PAGE_UP)#di chuyển lên đầu trang           
            time.sleep(3)

            
            success_message = self.driver.find_elements(By.XPATH, '//*[@id="page-35"]/div/div[1]/p[1]')
            if success_message:
                print("Pass: Shopping Order successful.")
            else:
                print("Fail: Shopping Order failed.")
            # Thêm lệnh fail() để báo hiệu cho hàm kiểm thử rằng quá trình đăng ký thất bại
                self.fail("Shopping Order failed.")
        except Exception as e:
            print("Error:", e)
            self.fail("An error occurred during Shopping Order.")

    def check_payment(self):
        element = self.driver.find_element("name", "update_cart")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)# Cuộn trang web xuống
        self.driver.find_element(By.PARTIAL_LINK_TEXT, "PROCEED TO CHECKOUT").click()
        try:
            element = self.driver.find_element(By.XPATH, '//*[@id="order_review"]/table/tfoot/tr[1]')
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)# Cuộn trang web xuống vị trí của phần tử
            self.driver.find_element(By.XPATH, '//*[@id="payment_method_ppec_paypal"]').click() #PayPal 4
            time.sleep(3)
            self.driver.find_element("id", "place_order").click() 
            element = self.driver.find_element(By.TAG_NAME, "body").send_keys(Keys.PAGE_UP)#di chuyển lên đầu trang           
            time.sleep(3)

            success_message = self.driver.find_elements(By.XPATH, '//*[@id="page-35"]/div/div[1]/p[1]')
            if success_message:
                print("Pass: Shopping Order successful.")
            else:
                print("Fail: Shopping Order failed.")
            # Thêm lệnh fail() để báo hiệu cho hàm kiểm thử rằng quá trình đăng ký thất bại
                self.fail("Shopping Order failed.")
        except Exception as e:
            print("Error:", e)
            self.fail("An error occurred during Shopping Order.")

    
    def test_TC1_Successful_Order_the_correct(self):
        result = self.check_free()
        billing_info = {
            "first" : "Giang",
            "last" : "Đinh",
            "company" : "CUNGOP",
            "email" : "dhuonggiang566@gmail.com",
            "phone" : "0339264512",
            "address" : "Đắk Lắk",
            "zip" : "073006",
            "city" : "BMT",
        }
        result = self.check_billing(billing_info)
        print("TC_01 Successful Shopping Order with the correct full enter")
    
    def test_TC2_Successful_Order_item_blank(self):
        self.driver.find_element(By.PARTIAL_LINK_TEXT, "Logout").click()
        result = self.check_add()
        billing_info = {
            "first" : "Giang",
            "last" : "Đinh",
            "company" : "",
            "email" : "dhuonggiang566@gmail.com",
            "phone" : "0339264512",
            "address" : "Đắk Lắk",
            "zip" : "",
            "city" : "BMT",
        }
        print("TC_02 Successful Shopping Order with leave the item blank optional")
        result = self.check_billing(billing_info)   


    def test_TC3_Failed_Order_invalid_ZIP(self):
        self.driver.find_element(By.PARTIAL_LINK_TEXT, "Logout").click()
        result = self.check_add()
        print("TC_03 Shopping Order failed with invalid Postcode/ZIP")
        result = self.check_payment()

    def test_TC4_Failed_empty_Fristname_Lastname(self):
        self.driver.find_element(By.PARTIAL_LINK_TEXT, "Logout").click()
        result = self.check_free()
        billing_info = {
            "first" : "",
            "last" : "",
            "company" : "",
            "email" : "dhuonggiang566@gmail.com",
            "phone" : "0339264512",
            "address" : "Đắk Lắk",
            "zip" : "",
            "city" : "BMT",
        }
        print("TC_04 Shopping Order failed with Empty First Name, Last Name")
        result = self.check_billing(billing_info)

    def test_TC5_Failed_Order_invalid_email(self):
        self.driver.find_element(By.PARTIAL_LINK_TEXT, "Logout").click()
        result = self.check_free()
        billing_info = {
            "first" : "Giang",
            "last" : "Đinh",
            "company" : "",
            "email" : "giang@gmail",
            "phone" : "0339264512",
            "address" : "Đắk Lắk",
            "zip" : "",
            "city" : "BMT",
        }
        print("TC_05 Shopping Order failed with invalid email")
        result = self.check_billing(billing_info)

    def test_TC6_Failed_Order_invalid_Phone(self):
        self.driver.find_element(By.PARTIAL_LINK_TEXT, "Logout").click()
        result = self.check_free()
        billing_info = {
            "first" : "Giang",
            "last" : "Đinh",
            "company" : "",
            "email" : "dhuonggiang566@gmail.com",
            "phone" : "sdfksfjk",
            "address" : "Đắk Lắk",
            "zip" : "",
            "city" : "BMT",
        }
        print("TC_06 Shopping Order failed with invalid Phone")
        result = self.check_billing(billing_info)

    def test_TC7_Failed_empty_Address_City(self):
        self.driver.find_element(By.PARTIAL_LINK_TEXT, "Logout").click()
        result = self.check_free()
        billing_info = {
            "first" : "Giang",
            "last" : "Đinh",
            "company" : "",
            "email" : "dhuonggiang566@gmail.com",
            "phone" : "0339264512",
            "address" : "",
            "zip" : "",
            "city" : "",
        }
        print("TC_07 Add Shipping Address failed with empty Address, empty Town/City")
        result = self.check_billing(billing_info)

    


    def setUp(self):
        self.driver.get("https://practice.automationtesting.in/my-account/")
        


    @classmethod
    def tearDownClass(cls):
        TestShoppingOrder._ran_tests = True  # Đánh dấu rằng các test đã được thực thi

if __name__ == '__main__':
    unittest.main()

"""driver.maximize_window()
driver.get("https://practice.automationtesting.in/")

driver.find_element(By.LINK_TEXT, "My Account").click()
driver.find_element("name", "username").send_keys("dhuonggiang566@gmail.com")
driver.find_element("name", "password").send_keys("Gimas+3006")
driver.find_element("name", "rememberme").click()
driver.find_element("name", "login").click()


driver.find_element("id", "wpmenucartli").click()#icon shopping

time.sleep(3)




element = driver.find_element("name", "update_cart")
driver.execute_script("arguments[0].scrollIntoView(true);", element)# Cuộn trang web xuống vị trí của phần tử
time.sleep(5)
driver.find_element(By.PARTIAL_LINK_TEXT, "PROCEED TO CHECKOUT").click()


element = driver.find_element(By.XPATH, '//*[@id="order_review"]/table/tfoot/tr[1]')
driver.execute_script("arguments[0].scrollIntoView(true);", element)# Cuộn trang web xuống vị trí của phần tử
driver.find_element("name", "payment_method").click() #PayPal  Direct Bank Transfer 1


driver.find_element("name", "payment_method_ppec_paypal").click() #PayPal 4
time.sleep(3)


driver.find_element("id", "place_order").click()
time.sleep(5)"""