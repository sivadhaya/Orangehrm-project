from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
driver.implicitly_wait(10)
#Login functionality
driver.find_element(By.NAME, "username").send_keys("Admin")
driver.find_element(By.NAME, "password").send_keys("admin123")
driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(5)
print("sucessfully login")
# #Switching from dashboard to PIM module
driver.switch_to.parent_frame()
# #PIM module details
driver.find_element(By.XPATH, "//span[normalize-space()='PIM']").click()
driver.find_element(By.XPATH, "//a[normalize-space()='Add Employee']").click()
driver.find_element(By.XPATH, "//input[@placeholder='First Name']").send_keys("Dhayalan")
driver.find_element(By.XPATH, "//input[@placeholder='Middle Name']").send_keys(".")
driver.find_element(By.XPATH, "//input[@placeholder='Last Name']").send_keys("S")
# driver.find_element(By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[2]").clear()
time.sleep(3)
driver.find_element(By.XPATH, "//div[@class='oxd-input-group oxd-input-field-bottom-space']//div//input[@class='oxd-input oxd-input--active']").send_keys("0311")
time.sleep(3)
driver.find_element(By.XPATH, "//button[@type='submit']").click()
print("sucessfully added")
time.sleep(5)
# #After adding employee filling the personal details
driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div[2]/div/div/div[2]/input").send_keys("ArnMar")
driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[2]/div/div[2]/div/div/input").send_keys("2036-05-15")
driver.find_element(By.XPATH, "(//i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow'])[1]").click()
# Html = driver.page_source
# print(Html)
driver.find_element(By.XPATH, "//div[@role='option']/span[text()='Indian']").click()
driver.find_element(By.XPATH, "(//i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow'])[2]").click()
# Html = driver.page_source
# print(Html)
driver.find_element(By.XPATH, "//span[normalize-space()='Single']").click()
time.sleep(5)
driver.find_element(By.XPATH, "//label[normalize-space()='Male']").click()
driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[1]/div/div[2]/div/div/input").send_keys("1997-07-14")
driver.find_element(By.XPATH, "//label[normalize-space()='Male']//span[@class='oxd-radio-input oxd-radio-input--active --label-right oxd-radio-input']").click()
driver.find_element(By.XPATH, "//div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']//button[@type='submit'][normalize-space()='Save']").click()
time.sleep(10)
print("Add employee sucessfully")
#Custom fields
driver.find_element(By.XPATH, "(//i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow'])[3]").click()
driver.find_element(By.XPATH, "//span[normalize-space()='B+']").click()
driver.find_element(By.XPATH, "//div[@class='orangehrm-custom-fields']//button[@type='submit'][normalize-space()='Save']").click()
time.sleep(10)
print("Saved sucessfully")


