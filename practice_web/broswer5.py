import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.baidu.com")
title = driver.title
url = driver.current_url
page_source = driver.page_source
print(title)
print(url)
print(page_source)
time.sleep(3)
driver.close()
 