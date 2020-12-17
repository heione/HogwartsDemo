import pytest


@pytest.fixture(autouse=True, scope="class")
def myfixture():
    print("测试开始")
    yield "success"
    print("测试结束")
