#5.Account Details

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")

driver.find_element(By.LINK_TEXT, "My Account").click()

driver.find_element("name", "username").send_keys("dhuonggiang566@gmail.com")
driver.find_element("name", "password").send_keys("Gimas+3006")
driver.find_element("name", "rememberme").click()
driver.find_element("name", "login").click()
time.sleep(2)


#Billing Address
driver.find_element(By.PARTIAL_LINK_TEXT, "Addresses").click()

driver.find_element(By.XPATH, "//*[@id='page-36']/div/div[1]/div/div/div[1]/header/a").click()
#//*[@id="page-36"]/div/div[1]/div/div/div[2]/header/a
driver.find_element("name", "billing_first_name").send_keys("dinh")
driver.find_element("name", "billing_last_name").send_keys("ngoc")
driver.find_element("name", "billing_company").send_keys("CUNGOP")#
driver.find_element("name", "billing_email").send_keys("dhuonggiang566@gmail.com")

driver.find_element("name", "billing_phone").send_keys("0339264512")
"""driver.implicitly_wait(10)
country = driver.find_element(By.XPATH, "//*[@id='s2id_billing_country']")
country.click()
country.send_keys("Vietnam")"""
country = Select(driver.find_element("id", "billing_country"))
country.select_by_visible_text("Vietnam")

driver.find_element("name", "billing_address_1").send_keys("Dak Lak")
driver.find_element("name", "billing_postcode").send_keys("214664") #
driver.find_element("name", "billing_city").send_keys("Buon Ma Thuot")
time.sleep(5)
driver.find_element("name", "save_address").click()
time.sleep(2)

#Shipping Address
driver.find_element(By.PARTIAL_LINK_TEXT, "Addresses").click()

driver.find_element(By.XPATH, "//*[@id='page-36']/div/div[1]/div/div/div[2]/header/a").click()
driver.find_element("name", "shipping_first_name").send_keys("dinh")
driver.find_element("name", "shipping_last_name").send_keys("ngoc")
driver.find_element("name", "shipping_company").send_keys("CUNGOP")#
"""driver.implicitly_wait(10)
country = driver.find_element(By.XPATH, "//*[@id='select2-chosen-1']")
country.click()
country.send_keys("Vietnam") """
country = Select(driver.find_element(By.ID, "shipping_country"))
country.select_by_visible_text("Vietnam")

driver.find_element("name", "shipping_address_1").send_keys("Dak Lak")
driver.find_element("name", "shipping_postcode").send_keys("214664")#
driver.find_element("name", "shipping_city").send_keys("Buon Ma Thuot")
time.sleep(5)
driver.find_element("name", "save_address").click()
time.sleep(2)


driver.quit()