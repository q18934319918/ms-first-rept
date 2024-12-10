import time

import select

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://news.baidu.com/")
driver.find_element(By.ID,'change-city').click()
time.sleep(2)
element = driver.find_element(By.CSS_SELECTOR,'#city_view > div.city_list > a:nth-child(1)')
time.sleep(3)
# driver.execute_script("arguments[0].scrollIntoView();",element)
# driver.execute_script("arguments[0].scrollIntoView(false);",element)
# driver.execute_script("arguments[0].scrollIntoViewIfNeeded(false);",element)
time.sleep(3)
driver.close()
