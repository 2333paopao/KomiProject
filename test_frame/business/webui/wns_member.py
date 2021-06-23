#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
import time
from drivers.wbeuidriver.web_driver import WebDriver
from selenium.webdriver.support.select import Select

class WNMember:
    def __init__(self):
        #获取driver
        self.driver = WebDriver.get_driver()

    def member_page(self):
        self.driver.find_element_by_link_text('会员管理').click()
        time.sleep(2)

    def member_phone(self,phone):
        self.driver.find_element_by_id('customerphone').click()
        self.driver.find_element_by_id('customerphone').send_keys(phone)
        time.sleep(2)

    def member_name(self,name):
        self.driver.find_element_by_id('customername').click()
        self.driver.find_element_by_id('customername').clear()
        self.driver.find_element_by_id('customername').send_keys(name)
        time.sleep(2)

    def member_sex(self,sex):
        #定位到下拉选择框
        sex_choose = self.driver.find_element_by_id('childsex')
        #通过选项的value值选择对应选项，此处还可以用text(文本)、index(序号)
        Select(sex_choose).select_by_value(sex)
        time.sleep(2)

    def member_add(self):
        self.driver.find_element_by_xpath('//button[contains(text(),"新增")]').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('//button[contains(text(),"OK")]').click()
        time.sleep(2)

    def member_query(self):
        self.member_page()
        self.driver.find_element_by_xpath('//button[contains(text(),"查询")]').click()

    def perform_member(self,phone,name,sex):
        self.member_page()
        self.member_phone(phone)
        self.member_name(name)
        self.member_sex(sex)
        self.member_add()
        self.member_query()

if __name__ == '__main__':
    pass