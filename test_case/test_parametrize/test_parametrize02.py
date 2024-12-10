from time import sleep

import pytest
from selenium.webdriver.common.by import By

from utils.read import read_yaml

heros = [("安琪拉", "我的小熊去哪里"),("后裔","周日被我射熄火了")]

#多参数多次循环
@pytest.mark.parametrize("hero,word", heros)
def test_parametrize02(hero, word):
    print("{}的台词是{}".format(hero,word))

@pytest.mark.parametrize("key,value",[["安琪拉","拉"],["后裔","后"]])
def test_parametrize(key,value):
    assert value in key

# @pytest.mark.parametrize("data",read_yaml()['userinfos'])
# def test_login(driver,data):
#     driver.get("http://sellshop.5istudy.online/sell/user/login_page")
#     driver.find_element(By.ID,'username').send_keys(data['username'])
#     driver.find_element(By.ID,'password').send_keys(data['password'])
#     driver.find_element(By.CSS_SELECTOR,'#login > form > p.login.button > input[type=submit]').click()
#     sleep(10)

@pytest.mark.parametrize("username,password",read_yaml()['userinfos_list'])
def test_login(driver,username,password):
    driver.get("http://sellshop.5istudy.online/sell/user/login_page")
    driver.find_element(By.ID,'username').send_keys(username)
    driver.find_element(By.ID,'password').send_keys(password)
    driver.find_element(By.CSS_SELECTOR,'#login > form > p.login.button > input[type=submit]').click()
    if username == 'admin':
        text = driver.find_element(By.CSS_SELECTOR,"body > div > div > div > div > strong").text
        assert text == "用户不存在"
    sleep(10)
