import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.baidu.com")
driver.find_element(By.CSS_SELECTOR,'a[href="http://news.baidu.com"]').click()
driver.find_element(By.CSS_SELECTOR,'a[href="http://news.baidu.com"]').click()
time.sleep(3)
driver.refresh()
time.sleep(3)
driver.close()
