import time
from pywinauto import keyboard
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from utils.get_filepath import get_logo_path


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://iviewui.com/view-ui-plus/component/form/upload")
driver.implicitly_wait(10)
driver.find_element(By.XPATH,'//button[@class="ivu-btn ivu-btn-default"]').click()
time.sleep(2)
keyboard.send_keys(r"F:\24萤火虫\IMG_2123")
time.sleep(2)
keyboard.send_keys('{ENTER}')
time.sleep(6)