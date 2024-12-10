import pytest


@pytest.fixture(scope="function",autouse=True)
def fixture1():
    print("我是前置步骤1。。。")
    return 1


@pytest.fixture(scope="function")
def fixture2():
    print("我是前置步骤2。。。")
    return 1


def test_fixture1():
    assert 1 == 1

def test_fixture2():
    assert 1 == 1


if __name__ == '__main__':
    pytest.main()
