import time

import select

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://iviewui.com/view-ui-plus/component/form/slider")
actions = ActionChains(driver)
# 双击
# element = driver.find_element(By.CSS_SELECTOR,"body > form > input[type=button]:nth-child(8)")
# actions.double_click(element).perform()
# 右击
# element = driver.find_element(By.XPATH,'/html/body/form/input[4]')
# actions.context_click(element).perform()
# 悬浮
# element = driver.find_element(By.CSS_SELECTOR,'#s-top-left > div > a')
# actions.move_to_element(element).perform()
# driver.find_element(By.XPATH,'//*[@id="s-top-more"]/div[3]/a/img').click()
# 拖动
# element_start = driver.find_element(By.ID, 'dragger')
# element_end = driver.find_element(By.XPATH, '/html/body/div[2]')
# actions.drag_and_drop(element_start, element_end).perform()
#根据坐标点拖动
element = driver.find_element(By.XPATH,"//div[@class='ivu-slider-button']")
actions.drag_and_drop_by_offset(element,250,0).perform()
time.sleep(3)
driver.close()


