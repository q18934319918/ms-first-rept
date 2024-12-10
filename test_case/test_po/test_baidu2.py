from time import sleep

import pytest

from page.page_baidu import PageBaidu
from utils.read import read_yaml


class TestBaidu:
    @pytest.mark.parametrize("key", read_yaml()['skill'])
    def test_baidu1(self,driver,key):
        page = PageBaidu(driver)
        page.search_keyword(key)
        sleep(2)

    def test_baidu2(self,driver):
        page = PageBaidu(driver)
        page.search_keyword("UI自动化")
        sleep(2)

    def test_baidu3(self,driver):
        page = PageBaidu(driver)

        driver.find_element(*page.input).send_keys("UI自动化")
        driver.find_element(*page.button).click()
        sleep(2)