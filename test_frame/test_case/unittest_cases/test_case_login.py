#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====

import unittest
from business.webui.wns_login import WNLogin
from drivers.wbeuidriver.web_driver import WebDriver
from parameterized.parameterized import parameterized
from selenium.webdriver.common.by import By

class TestCaseLogin(unittest.TestCase):
    #手工测试用例也有的
    #前置条件 - setUp准备
    #后置条件 - tearDown清除
    # def __init__(self):
    #     self.driver = WebDriver.get_driver()
    #前置条件，执行每一个测试用例前，都先执行登录操作
    @classmethod
    def setUpClass(cls):
        cls.driver = WebDriver.get_driver()

    @parameterized.expand([('admin','Milor123',True),('Lin','12345',False)])
    def test_case_login1(self,username,password,expect_result):
        WNLogin().perform_login(username,password)
        actural_result = WebDriver.is_element_present(By.LINK_TEXT,'注销')
        #断言实际结果和期望结果是否相等
        self.assertEqual(actural_result,expect_result)
        if actural_result == False:
            self.driver.find_element_by_xpath('//button[contains(text(),"OK")]').click()
        else:
            self.driver.find_element_by_link_text('注销').click()



if __name__ == '__main__':
    # TestCaseLogin.test_case_login1()
    unittest.main()
