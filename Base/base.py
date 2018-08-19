# 封装所有公用的方法
from selenium.webdriver.support.wait import WebDriverWait

class Base():
    # def find_element(self,type,value):
    #     el=None
    #     if type=="xpath":
    #         return self.driver.find_element_by_xpath(value)
    #     elif type=="id":
    #         return self.driver.find_element_by_id(value)
    #     elif type=="class":
    #         return self.driver.find_element_by_class_name(value)
    #     if el is not None:
    #         return el

    def __init__(self,driver):
        self.driver=driver

    def base_find_element(self,loc,timeout=5,poll=0.5):
        return WebDriverWait(self.driver,timeout,poll).until(lambda x:x.find_element(*loc))
    def base_find_elements(self,loc,timeout=5,poll=0.5):
        return WebDriverWait(self.driver,timeout,poll).until(lambda x:x.find_elements(*loc))

    def base_click_btn(self,loc):
        self.base_find_element(loc).click()

    def base_input_text(self,loc,value):
        self.base_find_element(loc).send_keys(value)

    def base_get_text(self,loc):
        return self.base_find_element(loc).text

