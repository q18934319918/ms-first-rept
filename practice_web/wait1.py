import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
# driver.set_page_load_timeout(3)
driver.implicitly_wait(0.01)
driver.get("https://www.baidu.com")
driver.find_element(By.ID,"kw").send_keys("selenium")
time.sleep(3)
driver.close()