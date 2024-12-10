from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.bilibili.com/")
# driver.find_element(By.CLASS_NAME,'nav-search-input').send_keys("2024新年快乐")
# driver.find_element(By.CLASS_NAME,'channel-link').click()
# driver.find_elements(By.CLASS_NAME,'channel-link')[4].click()
# for ele in driver.find_elements(By.CLASS_NAME,'channel-link'):
#     print(ele.text)
#错误用法
driver.find_element(By.CLASS_NAME,'icon-bg icon-bg__dynamic').click()


sleep(3)


