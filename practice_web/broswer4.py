import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.baidu.com")
size = driver.get_window_size()
print(size)
driver.set_window_size(width=500, height=500)
time.sleep(3)
driver.close()
 