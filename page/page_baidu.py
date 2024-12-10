from selenium import webdriver
from selenium.webdriver.common.by import By

from base.base_page import BasePage
from utils.log_util import logger


class PageBaidu(BasePage):
    #新闻
    news = (By.CSS_SELECTOR, 'a[href="http://news.baidu.com"]')
    #百度一下按钮
    button = (By.ID, 'su')
    #百度输入框
    input = (By.ID,'kw')
    #帮助
    help = (By.CSS_SELECTOR,'a[href="//help.baidu.com"]')
    #更多
    more = (By.XPATH, '//*[@id="s-top-left"]/div/a')

    def search_keyword(self,keyword):
        logger.info("查找元素并输入内容")
        self.driver.find_element(*self.input).send_keys(keyword)
        logger.info("点击按钮")
        self.driver.find_element(*self.button).click()