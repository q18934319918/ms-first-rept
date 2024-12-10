import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://sahitest.com/demo/clicks.htm")
element1 = driver.find_element(By.XPATH,'/html/body/form/input[5]')
element2 = driver.find_element(By.XPATH,'/html/body/form/input[6]')
# print(element1.is_enabled())
# print(element2.is_enabled())
print(element2.is_selected())
element2.click()
print(element2.is_selected())   


time.sleep(3)
