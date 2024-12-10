import pytest


@pytest.mark.parametrize("data",[{"name":"安琪拉","word":"火焰是我最喜欢的玩具"}])
def test_parametrize03(data):
    print(data["name"])
    print(data["word"])
