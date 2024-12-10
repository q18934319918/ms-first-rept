import pytest

@pytest.mark.p1
def test_three():
    assert 1 == 1
    assert 1 != 2
    assert 3 > 1
    assert 1 < 3
    assert 3 >= 3
    assert 3 <= 3
    pytest.assume("a" in "abc")
    pytest.assume("e" not in "abc")
    assert True is True
    assert False is not True
