import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
#打开本地的HTML文件，前面要加file://
driver.get("file://F:/UI自动化学习/Pytest+Selenium4Web自动化/test2024.10.26/pythonProject/HTML/iframe_test.html")
driver.find_element(By.ID,"checkRecord").clear()
driver.find_element(By.ID,"checkRecord").send_keys("666")
time.sleep(3)
#用下标
# driver.switch_to.frame("iframe_id")
#用name
driver.switch_to.frame("iframe_name")
driver.find_element(By.XPATH,'//span[text()="番剧"]').click()
time.sleep(3)
driver.close()
