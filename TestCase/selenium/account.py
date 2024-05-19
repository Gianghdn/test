#5.Account Details

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")

driver.find_element(By.LINK_TEXT, "My Account").click()

driver.find_element("name", "username").send_keys("dhuonggiang566@gmail.com")
driver.find_element("name", "password").send_keys("Dinh+3006giang")
driver.find_element("name", "rememberme").click()
driver.find_element("name", "login").click()
time.sleep(2)

driver.find_element(By.PARTIAL_LINK_TEXT, "Account Details").click()

driver.find_element("name", "account_first_name").send_keys("d")
driver.find_element("name", "account_last_name").send_keys("ngoc")
driver.find_element("name", "account_email").send_keys("dhuonggiang566@gmail.com")

driver.find_element("name", "password_current").send_keys("Dinh+3006giang")
driver.find_element("name", "password_1").send_keys("fsddsd") #New Password
driver.find_element("name", "password_2").send_keys("adadada") #Confirm New Password
time.sleep(5)

driver.find_element("name", "save_account_details").click()

driver.quit()