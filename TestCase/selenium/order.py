#đặt hàng

#8. Shopping

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")

driver.find_element(By.LINK_TEXT, "My Account").click()
driver.find_element("name", "username").send_keys("dhuonggiang566@gmail.com")
driver.find_element("name", "password").send_keys("Gimas+3006")
driver.find_element("name", "rememberme").click()
driver.find_element("name", "login").click()


driver.find_element("id", "wpmenucartli").click()#icon shopping

"""element = driver.find_element(By.XPATH, '//*[@id="woocommerce_price_filter-2"]/form/div/div[2]/button')
driver.execute_script("arguments[0].scrollIntoView(true);", element)# Cuộn trang web xuống vị trí của phần tử
driver.find_element(By.XPATH, '//*[@id="content"]/ul/li[1]/a[1]').click()#ấn vào sách
driver.find_element(By.XPATH, '//*[@id="product-169"]/div[2]/form/button').click()#nút add to basket
time.sleep(2)
driver.find_element(By.PARTIAL_LINK_TEXT, "VIEW BASKET").click()"""
time.sleep(3)




element = driver.find_element("name", "update_cart")
driver.execute_script("arguments[0].scrollIntoView(true);", element)# Cuộn trang web xuống vị trí của phần tử
time.sleep(5)
driver.find_element(By.PARTIAL_LINK_TEXT, "PROCEED TO CHECKOUT").click()


element = driver.find_element(By.XPATH, '//*[@id="order_review"]/table/tfoot/tr[1]')
driver.execute_script("arguments[0].scrollIntoView(true);", element)# Cuộn trang web xuống vị trí của phần tử
driver.find_element("name", "payment_method").click() #PayPal  Direct Bank Transfer 1


"""driver.find_element("name", "payment_method_ppec_paypal").click() #PayPal 4
time.sleep(3)
"""

driver.find_element("id", "place_order").click()
time.sleep(5)

driver.quit()