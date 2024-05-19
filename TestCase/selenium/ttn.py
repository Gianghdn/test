
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.ttn.edu.vn/index.php/ttnnth")
driver.find_element(By.PARTIAL_LINK_TEXT, "22-23/6/2024").click()

driver.find_element(By.XPATH, '//*[@id="attachmentsList_com_content_article_5519"]/table/tbody/tr/td[1]/a[2]').click()
time.sleep(2)
driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)
time.sleep(2)