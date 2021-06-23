#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====

import unittest
from business.webui.wns_sales import WNSales
from business.webui.wns_login import WNLogin
from drivers.wbeuidriver.web_driver import WebDriver

class TestCaseSales(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = WebDriver.get_driver()
        login_status = WebDriver.is_element_present('link text','注销')
        if login_status:
            pass
        else:
            WNLogin().perform_login('admin','Milor123')

    def test_case_sales1(self):
        WNSales().input_barcode('0')
        actural_result = WebDriver.is_element_present('link text','移除')
        expect_result = True
        #断言实际结果和期望结果是否相等
        self.assertEqual(actural_result,expect_result)

    def test_case_sales2(self):
        WNSales().input_phone('13200000000')
        actural_result = self.driver.find_element_by_id('oldcredit').get_attribute('value')
        print(actural_result)
        self.assertNotEqual(actural_result,'0')

if __name__ == '__main__':
    unittest.main()