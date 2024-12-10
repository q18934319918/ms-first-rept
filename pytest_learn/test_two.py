import pytest


class TestCase:
    def test_two(self):
        assert 1 == 1

    def test_three(self):
        assert 1 == 2

if __name__ == '__main__':
    pytest.main()