import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://sahitest.com/demo/selectTest.htm")
time.sleep(1)
select = Select(driver.find_element(By.ID,'s1'))
#根据index下标获取，从0开始
# select.select_by_index(1)
# select.select_by_value("51")
select.select_by_visible_text("Cell Phone")

time.sleep(1)
driver.close()
