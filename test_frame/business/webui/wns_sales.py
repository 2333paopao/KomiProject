#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
import time
from drivers.wbeuidriver.web_driver import WebDriver

class WNSales:
    def __init__(self):
        #获取driver
        self.driver = WebDriver.get_driver()

    #定位条码输入框，输入条码,点击确认
    def input_barcode(self,barcode):
        self.driver.find_element_by_xpath('//input[@id="barcode"]').click()
        self.driver.find_element_by_xpath('//input[@id="barcode"]').send_keys(barcode)
        self.driver.find_element_by_xpath('//button[contains(text(),"确认")]').click()
        # time.sleep(2)

    #定位到电话输入框，输入电话，点击查询
    def input_phone(self,phone):
        self.driver.find_element_by_id('customerphone').click()
        self.driver.find_element_by_id('customerphone').send_keys(phone)
        self.driver.find_element_by_xpath('//button[contains(text(),"查询会员信息")]').click()
        # time.sleep(2)

    #定位到确认收款按钮，点击确认收款
    def get_money(self):
        self.driver.find_element_by_id('submit').click()
        #点击确认收款后，跳出的alert弹框，接受
        self.driver.switch_to.alert.accept()

    #定义一个执行方法，执行上面的所有操作
    def perform_sales(self,barcode,phone):
        self.input_barcode(barcode)
        self.input_phone(phone)
        self.get_money()

if __name__ == '__main__':
    pass