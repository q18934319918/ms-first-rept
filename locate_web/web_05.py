import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.baidu.com/")
# driver.find_element(By.NAME,"wd").send_keys("根据name属性定位")
driver.find_elements(By.NAME,"wd")[0].send_keys("根据name属性定位")
time.sleep(3)
driver.close()