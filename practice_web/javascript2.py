import time

import select

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://element.eleme.cn/#/zh-CN/component/form")
# driver.execute_script('window.scrollTo(0,1000)')
# time.sleep(2)
# driver.execute_script('window.scrollTo(0,0)')
# time.sleep(2)
# driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
# driver.find_element(By.ID,'change-city').click()
# time.sleep(2)
# driver.find_element(By.CSS_SELECTOR,'#city_view > div.city_list > a:nth-child(1)').click()
driver.find_element(By.XPATH,'//*[@id="app"]/div[2]/div/div[1]/div/div/div[2]/section/div[1]/div[1]/div/form/div[6]/div/div/label[1]/span[1]').click()
time.sleep(2)
driver.close()
