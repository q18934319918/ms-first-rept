import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def driver1():
    driver = webdriver.Chrome()
    driver.maximize_window()
    print("打开浏览器")
    yield driver
    print("关闭浏览器")
    driver.close()
    driver.quit()

@pytest.fixture()
def fixture():
    print("我是前置步骤")
    yield "老白"
    print("我是后置步骤")
