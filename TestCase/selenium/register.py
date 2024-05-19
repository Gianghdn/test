from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")

driver.find_element(By.LINK_TEXT, "My Account").click()

driver.find_element("name", "email").send_keys("Didshg900@gmail.com")
driver.find_element("id", "reg_password").send_keys("Giangdinh%456hg")
driver.find_element("name", "register").click()
time.sleep(5)



driver.quit()