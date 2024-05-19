#7. Demo Site

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
"""driver.find_element(By.LINK_TEXT, "My Account").click()

driver.find_element("name", "username").send_keys("dhuonggiang566@gmail.com")
driver.find_element("name", "password").send_keys("Gimas+3006")
driver.find_element("name", "rememberme").click()
driver.find_element("name", "login").click()
time.sleep(2)"""


driver.find_element(By.PARTIAL_LINK_TEXT, "Demo Site").click()

#Photo Upload Images TC_01
image_path = "E:\\IMG_0571.JPG"
file_input = driver.find_element("id","imagesrc")
file_input.send_keys(image_path)
time.sleep(5)

#Drag and Drop TC_02
interactions_section = driver.find_element(By.LINK_TEXT, "Interactions")
driver.execute_script("arguments[0].scrollIntoView();", interactions_section)
interactions_section.click()

driver.find_element( By.LINK_TEXT,"Drag and Drop").click()
driver.find_element( By.LINK_TEXT,"Static").click()


source_1 = driver.find_element ("id", "angular") #cat
source_2 = driver.find_element ("id", "mongo") #dog
source_3 = driver.find_element ("id", "node") #horse

target = driver.find_element (By.ID, "droparea")

actions = ActionChains(driver)
"""actions.drag_and_drop(source_1, target).perform()
actions.drag_and_drop(source_2, target).perform()
actions.drag_and_drop(source_3, target).perform()
actions.drag_and_drop(source_4, target).perform()"""

for source_element in [source_1, source_3, source_2]:
    actions.drag_and_drop(source_element, target).perform()

for source_element in [source_1, source_3, source_3]:
    actions.drag_and_drop(source_element, target).perform()

actions.drag_and_drop(source_2, target).perform()
time.sleep(5)

#SummerNote TC_03
section = driver.find_element(By.LINK_TEXT, "WYSIWYG")
driver.execute_script("arguments[0].scrollIntoView();", section)
section.click()

driver.find_element(By.LINK_TEXT, "SummerNote").click()

note = driver.find_element(By.XPATH, "/html/body/section/div[1]/div/div/div[2]/div[3]/div[2]")#khung văn bản
note.send_keys(Keys.ENTER)

driver.find_element(By.XPATH, "/html/body/section/div[1]/div/div/div[2]/div[2]/div[7]/button[2]").click()
image_path = "E:\\logo.PNG"
file_input = driver.find_element(By.XPATH, "/html/body/section/div[1]/div/div/div[2]/div[6]/div/div/div[2]/div[1]/input")
file_input.send_keys(image_path)

driver.find_element(By.XPATH, "/html/body/section/div[1]/div/div/div[2]/div[2]/div[7]/button[2]").click()
image_path = "E:\\IMG_0519.JPG"
file_input = driver.find_element(By.XPATH, "/html/body/section/div[1]/div/div/div[2]/div[6]/div/div/div[2]/div[1]/input")
file_input.send_keys(image_path)

note.send_keys(Keys.ENTER)
driver.find_element(By.XPATH, "/html/body/section/div[1]/div/div/div[2]/div[2]/div[2]/button[1]").send_keys(" Đinh Ngọc Hương Giang") #in đậm B

interactions_section = driver.find_element(By.XPATH, "/html/body/section/div[1]/div/div/div[2]/div[2]/div[1]/div/button")#button style
driver.execute_script("arguments[0].scrollIntoView();", interactions_section)
interactions_section.click()

style = driver.find_element(By.PARTIAL_LINK_TEXT, "pre").click()
style = driver.find_element(By.XPATH, "/html/body/section/div[1]/div/div/div[2]/div[3]/div[2]").send_keys(" CNTTK20")
note.send_keys(Keys.ENTER)
style = driver.find_element(By.XPATH, "/html/body/section/div[1]/div/div/div[2]/div[3]/div[2]").send_keys(" Trường đại học Tây Nguyên")
time.sleep(5)

#Button More with Dynamic Data TC_04
section = driver.find_element(By.LINK_TEXT, "More")
driver.execute_script("arguments[0].scrollIntoView();", section)
section.click()

driver.find_element(By.LINK_TEXT, "Dynamic Data").click()

driver.find_element("id", "save").click()
time.sleep(4)
driver.find_element("id", "save").click()
time.sleep(4)

#Button More with File Download TC_05
section = driver.find_element(By.LINK_TEXT, "More")
driver.execute_script("arguments[0].scrollIntoView();", section)
section.click()

driver.find_element(By.LINK_TEXT, "File Download").click()
time.sleep(5)

element = driver.find_element(By.XPATH, '/html/body/section/div[1]/div/div/h2')
driver.execute_script("arguments[0].scrollIntoView(true);", element)

driver.find_element ("id", "textbox").send_keys("Testing download text file: Đinh Giang")
driver.find_element("id", "createTxt").click()
driver.find_element("id", "link-to-download").click()

time.sleep(5)
#download file
#driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")# lướt xuống cuối trang

element = driver.find_element("id", "textarea_feedback")
driver.execute_script("arguments[0].scrollIntoView(true);", element)# Cuộn trang web xuống vị trí của phần tử

driver.find_element ("id", "pdfbox").send_keys("Testing download text file: Đinh Ngọc Hương Giang")
driver.find_element("id", "createPdf").click()
driver.find_element("id", "pdf-link-to-download").click()
time.sleep(5)


#Button More with File Download TC_06
section = driver.find_element(By.LINK_TEXT, "More")
driver.execute_script("arguments[0].scrollIntoView();", section)
section.click()
driver.find_element(By.LINK_TEXT, "File Upload").click()


file_input = driver.find_element("id", "input-4")
file_input.send_keys("E:\\flutter\\20103109_Đinh Ngọc Hương Giang.pdf")
time.sleep(5)

driver.quit()
