#8. Shopping

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")

driver.find_element(By.LINK_TEXT, "My Account").click()
"""driver.find_element("name", "username").send_keys("dhuonggiang566@gmail.com")
driver.find_element("name", "password").send_keys("Gimas+3006")
driver.find_element("name", "rememberme").click()
driver.find_element("name", "login").click()"""



#thêm giỏ hàng
driver.find_element("id", "wpmenucartli").click()#icon shopping
element = driver.find_element(By.XPATH, '//*[@id="woocommerce_price_filter-2"]/form/div/div[2]/button')
driver.execute_script("arguments[0].scrollIntoView(true);", element)# Cuộn trang web xuống vị trí của phần tử
driver.find_element(By.XPATH, '//*[@id="content"]/ul/li[1]/a[1]').click()#ấn vào sách
driver.find_element(By.XPATH, '//*[@id="product-169"]/div[2]/form/button').click()#nút add to basket
time.sleep(2)
driver.find_element(By.PARTIAL_LINK_TEXT, "VIEW BASKET").click()


driver.find_element(By.LINK_TEXT, "Shop").click()#icon shop
element = driver.find_element(By.XPATH, '//*[@id="content"]/ul/li[3]/a[1]/h3')
driver.execute_script("arguments[0].scrollIntoView(true);", element)# Cuộn trang web xuống vị trí của phần tử
driver.find_element(By.XPATH, '//*[@id="content"]/ul/li[5]').click()#sách JS Data
driver.find_element(By.XPATH, '//*[@id="product-180"]/div[2]/form/button').click()#add to basket
driver.find_element(By.PARTIAL_LINK_TEXT, "VIEW BASKET").click()
time.sleep(2)
#cập nhật giỏ hàng

quantity_input = driver.find_element(By.XPATH, '//*[@id="page-34"]/div/div[1]/form/table/tbody/tr[1]/td[5]/div/input')
quantity_input.clear()#xóa giá trị trong ô
new_quantity = "4"  # Số lượng mới bạn muốn nhập
quantity_input.send_keys(new_quantity)
quantity_input.send_keys(Keys.ENTER)

time.sleep(2)
element = driver.find_element("name", "update_cart")
driver.execute_script("arguments[0].scrollIntoView(true);", element)# Cuộn trang web xuống vị trí của phần tử
time.sleep(5)

#xóa giỏ hàng
element = driver.find_element(By.TAG_NAME, "body").send_keys(Keys.PAGE_UP)#di chuyển lên đầu trang
driver.find_element(By.XPATH, '//*[@id="page-34"]/div/div[1]/form/table/tbody/tr[1]/td[1]/a').click()
time.sleep(5)

driver.quit()