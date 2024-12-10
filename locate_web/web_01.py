import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# 定义一个driver的变量，用来接收实例化后的浏览器
driver = webdriver.Chrome()
# 使用get方法，访问网址
driver.get('https://www.bilibili.com/')
driver.find_element(By.CLASS_NAME, 'nav-search-input').send_keys("软件测试老白")
time.sleep(3)
driver.find_element(By.CLASS_NAME, 'nav-search-btn').click()
time.sleep(3)
driver.close()
