import time

import select

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.baidu.com/")
driver.find_element(By.ID,"kw").send_keys("selenium")
actions = ActionChains(driver)
element = driver.find_element(By.ID,"su")
actions.click(element).perform()
time.sleep(3)
driver.close()

