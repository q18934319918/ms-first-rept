import pytest


@pytest.mark.run(order=1)
class TestRegister:
    def test_register(self):
        print("我现在注册。。。")
        assert 2 == 2