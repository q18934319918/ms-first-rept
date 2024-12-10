import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.bilibili.com/")
driver.find_element(By.TAG_NAME,"input").send_keys("学习selenium")
#不推荐
# driver.find_element(By.TAG_NAME,"input")[50].click()
time.sleep(3)
driver.quit()