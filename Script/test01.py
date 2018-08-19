# 页面测试脚本
import os,sys
sys.path.append(os.getcwd())
from time import sleep
from Base.get_driver import get_driver
from Page.page_setting import PageSetting

class TestSetting():
    def setup(self):
        self.driver=get_driver()
        self.setting=PageSetting(self.driver)

    def teardown(self):
        sleep(3)
        self.driver.quit()

    def test_setting(self):
        self.setting.page_click_search_btn()
        self.setting.page_input_text("wlan")
        self.setting.page_click_back_btn()

