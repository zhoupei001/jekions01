import allure
import pytest

class Test01():
    @allure.step('我是测试步骤001')
    def test001(self):
        print("001被执行")
       

    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    def test002(self):
        allure.attach('描述', '我是测试步骤002的描述～～～')
        print("test002被执行")
        assert 0



