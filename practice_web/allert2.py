import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://sahitest.com/demo/confirmTest.htm")
driver.find_element(By.NAME,'b1').click()
print(driver.switch_to.alert.text)
time.sleep(1)
#点击同意
# driver.switch_to.alert.accept()
#点击取消
driver.switch_to.alert.dismiss()
time.sleep(1)
driver.close()