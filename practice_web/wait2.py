# import os
# import time
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# from utils.get_filepath import download_file_path
#
# path = download_file_path() + "/LATEST_RELEASE"
# if os.path.exists(path):
#     print("文件存在")
#     os.remove(path)
#     print("文件已删除")
# chromeOptions = webdriver.ChromeOptions()
# prefs = {"download.default_directory":"{}".format(download_file_path())}
# chromeOptions.add_experimental_option("prefs",prefs)
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://registry.npmmirror.com/binary.html?path=chromedriver")
# time.sleep(3)
# driver.find_element(By.XPATH, '/html/body/table/tbody/tr[156]/td[2]/a').click()
#
# time.sleep(5)
# driver.close()

#指定下载路径之后就会下载不了，问题尚未清楚


import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from utils.get_filepath import download_file_path

path = download_file_path() + "/LATEST_RELEASE"
if os.path.exists(path):
    print("文件存在")
    os.remove(path)
    print("文件已删除")

chromeOptions = webdriver.ChromeOptions()
prefs = {"download.default_directory": "{}".format(download_file_path())}
chromeOptions.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(chromeOptions)
driver.implicitly_wait(1)
driver.maximize_window()
driver.get("https://registry.npmmirror.com/binary.html?path=chromedriver/")
driver.find_element(By.XPATH, '/html/body/table/tbody/tr[156]/td[2]/a').click()
time.sleep(3)
driver.close()
