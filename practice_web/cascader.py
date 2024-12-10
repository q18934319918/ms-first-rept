import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://iviewui.com/view-ui-plus/component/form/cascader")
driver.find_element(By.XPATH,'//input[@class="ivu-input ivu-input-default"]').click()
driver.find_element(By.XPATH,'//li[contains(text(),"北京")]').click()
driver.find_element(By.XPATH,'//li[contains(text(),"王府井")]').click()
time.sleep(1)
driver.close()
