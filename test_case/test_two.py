import pytest

@pytest.mark.pro
class TestK:
    def test_two(self):
        print("我是test_two")
        assert 1 == 1

    def test_three(self):
        print("我是test_three")
        assert 1 == 1

if __name__ == '__main__':
    pytest.main()