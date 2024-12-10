import time

import select

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://element.eleme.cn/#/zh-CN/component/form")
element = driver.find_element(By.XPATH,'//*[@id="app"]/div[2]/div/div[1]/div/div/div[2]/section/div[1]/div[1]/div/form/div[6]/div/div/label[1]/span[1]')
driver.execute_script("arguments[0].click();",element)
time.sleep(10)
driver.close()
