import pytest


@pytest.mark.run(order=2)
class TestUser:

    def test_login(self):
        print("我现在登录。。。")
        assert 1 == 1

