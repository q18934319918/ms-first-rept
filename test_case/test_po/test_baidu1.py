from selenium.webdriver.common.by import By

from page.page_baidu import PageBaidu
from utils.assert_util import assert_compare
from utils.log_util import logger


class TestBaidu:
    def test_baidu1(self,driver):
        page = PageBaidu(driver)
        #未登录测试
        driver.get("https://www.baidu.com/")
        title = driver.title
        url = driver.current_url
        text = driver.find_element(*page.news).text
        button_text = driver.find_element(*page.button).accessible_name
        assert title == '百度一下，你就知道'
        assert url == 'https://www.baidu.com/'
        assert text == '新闻'
        assert button_text == '百度一下'

    def test_baidu2(self,driver):
        page = PageBaidu(driver)
        #登录测试
        driver.get("https://www.baidu.com/")
        title = driver.title
        url = driver.current_url
        text = driver.find_element(*page.news).text
        button_text = driver.find_element(*page.button).accessible_name
        assert_compare(title,"==","百度一下，你就知道")
        # assert title == '百度一下，你就知道'
        assert_compare(url,"==","https://www.baidu.com/")
        # assert url == 'https://www.baidu.com/'
        assert text == '新闻'
        assert button_text == '百度一下'
