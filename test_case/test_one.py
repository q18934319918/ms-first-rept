import pytest


@pytest.mark.run(order=3)
@pytest.mark.pro
def test_1():
    name = "老白"
    assert name == "老白"


@pytest.mark.run(order=5)
@pytest.mark.test
def test_3():
    num = 10
    assert num == 10


@pytest.mark.run(order=4)
@pytest.mark.test
def test_2():
    num = 10
    assert num == 10
