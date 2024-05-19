from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.maximize_window()
#TC_01 home seen
driver.get("https://practice.automationtesting.in/")
#TC_02 search
driver.find_element(By.NAME, "s").send_keys("selenium", Keys.RETURN)
time.sleep(2)
#TC_03 shop
driver.find_element(By.LINK_TEXT, "Shop").click()
time.sleep(2)
#TC_04 my accout
driver.find_element(By.LINK_TEXT, "My Account").click()
time.sleep(2)
#TC_05 test cases
driver.find_element(By.LINK_TEXT, "Test Cases").click()
time.sleep(2)
#TC_08 icon shopping
driver.find_element(By.XPATH, "//*[@id='wpmenucartli']/a").click()
time.sleep(2)
#TC_06 at site
driver.find_element(By.LINK_TEXT, "AT Site").click()
time.sleep(2)
#TC_07 demo site
driver.get("https://practice.automationtesting.in/")
driver.find_element(By.LINK_TEXT, "Demo Site").click()
time.sleep(2)

driver.quit()