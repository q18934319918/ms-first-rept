import time

import pytest
from selenium.webdriver.common.by import By

from utils.read import read_yaml


# 单参数，单次循环
# @pytest.mark.parametrize("key",["value"])
# def test_parametrize(key):
#     print(key)
#     assert 1 == 1

# 单参数，多次循环。数组里面有几组数据，循环几次
# @pytest.mark.parametrize("test", ['接口自动化', 'UI自动化', '性能测试'])
# def test_parametrize02(test):
#     assert test == "接口自动化"


@pytest.mark.parametrize("key", read_yaml()['skill'])
def test_baidu(driver,key):
    driver.get("https://www.baidu.com")
    driver.find_element(By.ID,"kw").send_keys(key)
    driver.find_element(By.ID, "su").click()
    time.sleep(1)
