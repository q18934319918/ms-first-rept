import pytest


def test_three():
    assert 1 == 1
    assert 1 != 2
    assert 3 > 1
    assert 1 < 3
    assert 3 >= 3
    assert 3 <= 3
    pytest.assume("e" in "abc")
    pytest.assume("a" not in "abc")
    assert True is True
    assert False is not True
