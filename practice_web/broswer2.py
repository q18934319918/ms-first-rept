import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.baidu.com")
driver.find_element(By.CSS_SELECTOR,'a[href="http://news.baidu.com"]').click()
#打印当前句柄
current_handle = driver.current_window_handle
#循环切换，先切换第一个窗口，再切换第二个窗口
# for handle in driver.window_handles:
#     if handle != current_handle:
#         driver.switch_to.window(handle)
#         print(handle)
#         time.sleep(2)
# all_handles = driver.window_handles
# #根据下标去取
# driver.switch_to.window(all_handles[1])
# driver.find_element(By.CSS_SELECTOR,'a[href="//help.baidu.com"]').click()
#打开新标签
driver.switch_to.new_window('tab')
driver.get("https://www.bilibili.com")
time.sleep(3)
driver.close()
