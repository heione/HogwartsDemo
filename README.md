# 项目说明

# 霍格沃滋测试开发学习

###一、pytest实战作业

####作业1：

1、补全计算器（加减乘除）的测试用例

2、使用参数完成测试用例的自动生成

3、在调用测试方法之前打印【开始计算】，在调用测试方法之后打印【计算结束】

答：

-->pythoncode/calculator.py  计算器程序

-->test_calc.py  对计算器进行测试

####作业2：

练习1

使用【测试数据的数据驱动】的方法完成加减乘除测试

使用fixture替换setup和teardown

将fixture方法放在conftest.py里面，设置scope=module

修改运行规则，pytest.ini文件

练习2(选做)

控制用例的执行顺序，如：加减乘除

结合allure生成测试结果报告（未完成）

答：

-->pythoncode/calculator.py  计算器程序

-->test_calc.py  对计算器进行测试

-->data.yml  数据文件

-->conftest.py  fixture文件

-->pytest.ini  pytest配置文件