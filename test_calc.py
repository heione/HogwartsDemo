import pytest
from pythoncode.calculator import Calculator


class TestCalc:
    def setup_class(self):
        self.calc = Calculator()
        print("类开始(%s)------开始计算" % "setup_class")

    def teardown_class(self):
        print("类结束(%s)------结束计算" % "teardown_class")

    def setup_method(self):
        print("方法开始(%s)------开始计算" % "setup_method")

    def teardown_method(self):
        print("方法结束(%s)------开始计算" % "teardown_method")

    @pytest.mark.parametrize("a,b,expect", [
        (3, 5, 8), (-1, -2, -3), (100, 300, 400)
    ], ids=["int", "minus", "bigint"])
    def test_add(self, a, b, expect):
        """加法测试"""
        assert expect == self.calc.add(a, b)

    @pytest.mark.parametrize("a,b,expect", [
        (1, 1, 0), (-1, -1, 0), (2.5, 0.5, 2)
    ], ids=["int", "minus", "decimal"])
    def test_sub(self, a, b, expect):
        """减法测试"""
        assert expect == self.calc.sub(a, b)

    @pytest.mark.parametrize("a, b, expect", [
        (1, 0, False), (1, 1, 2)
    ], ids=("False Test", "int"))
    def test_div(self, a, b, expect):
        """除法测试"""
        assert expect == self.calc.div(a, b)

    @pytest.mark.parametrize("a", [1, 2, 3])
    @pytest.mark.parametrize("b", [1, 7, 8])
    def test_mul(self, a, b):
        """乘法测试"""
        print(self.calc.mul(a, b))
