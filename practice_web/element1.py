import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.baidu.com")
element1 = driver.find_element(By.CSS_SELECTOR,'a[href="http://news.baidu.com"]')
element2 = driver.find_element(By.XPATH,'//span[@class="title-content-title"]')
element3 = driver.find_element(By.ID,'su')
time.sleep(3)
print(element1.text)
print(element2.text)
print(element3.accessible_name)