import time
from time import sleep

import pytest

from page.page_baidu import PageBaidu
from utils.read import read_yaml


class TestBaidu:

    def test_baidu3(self, driver1):
        page = PageBaidu(driver1)
        # page.find_element(page.input).send_keys("UI自动化")
        # # driver.find_element(*page.input).send_keys("UI自动化")
        # page.find_element(page.button).click()
        # # driver.find_element(*page.button).click()
        # page.find_element(page.input,retry=2).send_keys("UI自动化")
        page.send_keys(page.input, "UI自动化")
        # page.find_element(page.button).click()
        page.click_button(page.button)
        sleep(2)

    def test_baidu4(self, driver1):
        page = PageBaidu(driver1)
        page.get_url("http://www.bilibili.com")
        page.refresh()

    def test_baidu5(self, driver1):
        page = PageBaidu(driver1)
        page.click(page.news)
        page.switch_to_window()
        page.click(page.help)
        page.switch_to_window(to_parent_window=True)
        page.send_keys(page.input, "UI自动化")
        time.sleep(3)

    def test_baidu6(self,driver1):
        page = PageBaidu(driver1)
        print(page.get_title())
        print(page.get_page_source())
        print(page.get_current_url())

    def test_baidu7(self,driver1):
        page = PageBaidu(driver1)
        print(page.get_text(page.news))
        print(page.get_text(page.button))

    def test_baidu8(self,driver1):
        page = PageBaidu(driver1)
        page.move_to_element(page.more)
        sleep(3)


