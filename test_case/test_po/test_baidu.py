from selenium.webdriver.common.by import By

from utils.log_util import logger


class TestBaidu:
    news = (By.CSS_SELECTOR, 'a[href="http://news.baidu.com"]')
    button = (By.ID, 'su')
    def test_baidu1(self,driver):
        #未登录测试
        driver.get("https://www.baidu.com/")
        title = driver.title
        url = driver.current_url
        text = driver.find_element(*TestBaidu.news).text
        button_text = driver.find_element(*TestBaidu.button).accessible_name
        assert title == '百度一下，你就知道'
        assert url == 'https://www.baidu.com/'
        assert text == '新闻'
        assert button_text == '百度一下'

    def test_baidu2(self,driver):
        #登录测试
        driver.get("https://www.baidu.com/")
        title = driver.title
        url = driver.current_url
        text = driver.find_element(*TestBaidu.news).text
        button_text = driver.find_element(*TestBaidu.button).accessible_name
        assert title == '百度一下，你就知道'
        assert url == 'https://www.baidu.com/'
        assert text == '新闻'
        assert button_text == '百度一下'
