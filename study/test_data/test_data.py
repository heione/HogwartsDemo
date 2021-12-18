import allure
import yaml

import pytest


@allure.feature('测试模块')
class TestData:

    @allure.story('加法测试')
    @pytest.mark.parametrize('a, b, c', yaml.safe_load(open('./data.yml')))
    def test_add(self, a, b, c):
        assert c == a + b

    @allure.story('减法测试')
    @pytest.mark.parametrize('a, b, c', [(3, 2, 1)])
    def test_sub(self, a, b, c):
        assert c == a - b

    @allure.story('测试地址')
    @pytest.mark.parametrize('env', yaml.safe_load(open('./env.yml')))
    def test_data1(self, env):
        if 'test' in env:
            print('这是测试环境')
            print(f'IP地址：{env["test"]}')
        elif 'dev' in env:
            print('这是开发环境')
            print(f'IP地址：{env["dev"]}')


@allure.feature('登录模块')
class TestLogin:
    @allure.story('登录成功')
    def test_login_success(self):
        with allure.step('步骤1：打开应用'):
            allure.attach('这是一个文本', attachment_type=allure.attachment_type.TEXT)
            print('打开应用')
        with allure.step('步骤2：进入登录页面'):
            print('登录页面')
        with allure.step('步骤3：输入用户名和密码'):
            print('输入用户名密码')
        print('这是登录：测试用例，登录成功')

    test_case_link = 'https://www.baidu.com'

    @allure.testcase(test_case_link, '测试链接')
    @allure.story('文本测试')
    def test_attach(self):
        with allure.step('步骤1：显示文本'):
            allure.attach('显示文本', name='文本', attachment_type=allure.attachment_type.TEXT)

        with allure.step('步骤2：显示图片'):
            allure.attach.file('E:/work/HogwartsDemo/study/test_data/file/dnf.png', name='DNF装备', attachment_type=allure.attachment_type.PNG)

        with allure.step('步骤3：麻将视频'):
            allure.attach.file('E:/work/HogwartsDemo/study/test_data/file/mahjong.mp4', name='麻将视频', attachment_type=allure.attachment_type.MP4)
