import pytest
from pythoncode.calculator import Calculator
import yaml


def get_yaml_data(file="./data.yml"):
    """获取yaml数据"""
    with open(file) as f:
        yaml_data = yaml.safe_load(f)
        add = yaml_data["add"]
        sub = yaml_data["sub"]
        div = yaml_data["div"]
        mul = yaml_data["mul"]
    return {"add": add, "sub": sub, "div": div, "mul": mul}


yd = get_yaml_data()
mf = Calculator()


class TestCalc:
    # def setup_class(self):
    #     self.calc = Calculator()
    #     print("类开始(%s)------开始计算" % "setup_class")
    #
    # def teardown_class(self):
    #     print("类结束(%s)------结束计算" % "teardown_class")
    #
    # def setup_method(self):
    #     print("方法开始(%s)------开始计算" % "setup_method")
    #
    # def teardown_method(self):
    #     print("方法结束(%s)------开始计算" % "teardown_method")

    @pytest.mark.run(order=4)
    @pytest.mark.add
    @pytest.mark.parametrize("a,b,expect", yd["add"])
    def test_add(self, a, b, expect):
        """加法测试"""
        assert expect == mf.add(a, b)

    @pytest.mark.run(order=3)
    @pytest.mark.sub
    @pytest.mark.parametrize("a,b,expect", yd["sub"])
    def test_sub(self, a, b, expect):
        """减法测试"""
        assert expect == mf.sub(a, b)

    @pytest.mark.run(order=2)
    @pytest.mark.div
    @pytest.mark.parametrize("a, b, expect", yd["div"])
    def test_div(self, a, b, expect):
        """除法测试"""
        assert expect == mf.div(a, b)

    @pytest.mark.run(order=1)
    @pytest.mark.mul
    @pytest.mark.parametrize("a", yd["mul"][0])
    @pytest.mark.parametrize("b", yd["mul"][1])
    def test_mul(self, a, b):
        """乘法测试"""
        expect = a * b
        assert expect == mf.mul(a, b)
