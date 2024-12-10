import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    print("打开浏览器")
    return driver

@pytest.fixture(scope="session",autouse=True)
def session():
    print("我是session级别")

@pytest.fixture(scope="module",autouse=True)
def module():
    print("我是module级别")

@pytest.fixture(scope="class",autouse=True)
def te_class():
    print("我是class级别")

@pytest.fixture(scope="function",autouse=True)
def function():
    print("我是function级别")