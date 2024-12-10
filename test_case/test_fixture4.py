import pytest
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture(scope="session")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    print("打开浏览器")
    return driver

class Testbaidu:

    def test_baidu(self,driver):
        driver.get("https://www.baidu.com/")
        title = driver.title
        url = driver.current_url
        text = driver.find_element(By.CSS_SELECTOR, 'a[href="http://news.baidu.com"]').text
        button_text = driver.find_element(By.ID, 'su').accessible_name
        assert title == '百度一下，你就知道'
        assert url == 'https://www.baidu.com/'
        assert text == '新闻'
        assert button_text == '百度一下'


    def test_baidu1(self,driver):
        driver.get("https://www.baidu.com/")
        title = driver.title
        url = driver.current_url
        text = driver.find_element(By.CSS_SELECTOR, 'a[href="http://news.baidu.com"]').text
        button_text = driver.find_element(By.ID, 'su').accessible_name
        assert title == '百度一下，你就知道'
        assert url == 'https://www.baidu.com/'
        assert text == '新闻'
        assert button_text == '百度一下'


if __name__ == '__main__':
    pytest.main()
