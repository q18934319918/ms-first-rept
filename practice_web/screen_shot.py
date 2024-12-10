import time

import select

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from utils.get_filepath import get_screen_shot_path

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://news.baidu.com/")
driver.find_element(By.ID,'change-city').click()
time.sleep(2)
element = driver.find_element(By.CSS_SELECTOR,'#city_view > div.city_list > a:nth-child(1)')
time.sleep(2)
# driver.execute_script("arguments[0].scrollIntoView();",element)
# driver.execute_script("arguments[0].scrollIntoView(false);",element)
driver.execute_script("arguments[0].scrollIntoViewIfNeeded(false);",element)
driver.save_screenshot(get_screen_shot_path())
time.sleep(2)
driver.close()

