# import time
# from pywinauto import keyboard
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get('https://www.baidu.com/')
# driver.implicitly_wait(10)
# time.sleep(2)
# driver.find_element(By.XPATH, '//*[@id="form"]/span[1]/span[1]').click()
# time.sleep(2)
# driver.find_element(By.XPATH, '//*[@id="form"]/div[1]/div[2]/div[2]/input').click()#使用class和Xpath定位均报错，怀疑驱动问题，当前69版本浏览器，驱动为70
# time.sleep(2)
# keyboard.send_keys(r"F:\UI自动化学习\Pytest+Selenium4Web自动化\test2024.10.26\pythonProject\img\9999999999999.png")  # 输入文件绝对路径
# time.sleep(2)
# keyboard.send_keys('{ENTER}')
# time.sleep(2)

#此份代码报错，原因尚未清楚