from selenium import webdriver
from selenium.webdriver import Keys
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
#Switching from dashboard to PIM module
driver.switch_to.parent_frame()
# #PIM module details
driver.find_element(By.XPATH, "//span[normalize-space()='PIM']").click()
driver.find_element(By.XPATH, "//a[normalize-space()='Employee List']").click()
time.sleep(5)
driver.find_element(By.XPATH, "//i[@class='oxd-icon bi-trash']").click()
driver.find_element(By.XPATH, "//button[normalize-space()='Yes, Delete']").click()
time.sleep(10)
print("Employee details: Sucessfully deleted")