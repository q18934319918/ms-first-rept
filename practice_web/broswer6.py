import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://news.baidu.com/")
driver.find_element(By.CSS_SELECTOR,'a[href="//help.baidu.com"]').click()
time.sleep(1)
driver.back()
time.sleep(1)
driver.forward()
time.sleep(3)
driver.close()

   