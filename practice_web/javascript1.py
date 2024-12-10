import time

import select

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.baidu.com/")
driver.execute_script('document.getElementById("kw").value="selenium"')
driver.execute_script('document.getElementById("su").click()')
time.sleep(3)
driver.close()
