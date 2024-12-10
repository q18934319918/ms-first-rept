import pytest
from selenium import webdriver

@pytest.fixture(scope="session")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    print("打开浏览器")
    yield driver
    print("关闭浏览器")
    driver.close()
    driver.quit()

