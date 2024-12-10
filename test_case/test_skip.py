import pytest

a = 1

@pytest.mark.skip(reason="我不想执行")
def test_skip1():
    assert 1 == 1


@pytest.mark.skipif(a == 2,reason="判断1等于1")
def test_skip2():
    assert 1 == 1

def test_skip3():
    if a > 1:
        pytest.skip("测试用例中跳过")
    assert 1 == 1

if __name__ == '__main__':
    pytest.main()
