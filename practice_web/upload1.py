import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from utils.get_filepath import get_logo_path

path = get_logo_path()
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://sahitest.com/demo/php/fileUpload.htm")
#获取input文件上传元素
upload = driver.find_element(By.ID,'file')
upload.send_keys(r"{}".format(path))
driver.find_element(By.NAME,'submit').click()
time.sleep(1)
driver.close()