#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====

#对象与业务分离
from drivers.wbeuidriver.web_driver import WebDriver

class WNLogin:
    def __init__(self):
        #获取driver
        self.driver = WebDriver.get_driver()

    #输入用户名
    def input_username(self,username):
        self.driver.find_element_by_id('username').click()
        self.driver.find_element_by_id('username').clear()
        self.driver.find_element_by_id('username').send_keys(username)

    #输入密码
    def input_password(self,password):
        self.driver.find_element_by_id('password').click()
        self.driver.find_element_by_id('password').clear()
        self.driver.find_element_by_id('password').send_keys(password)

    #输入验证码
    def input_verifycode(self):
        self.driver.find_element_by_id('verifycode').click()
        self.driver.find_element_by_id('verifycode').clear()
        self.driver.find_element_by_id('verifycode').send_keys('0000')

    #点击登录按钮
    def button_login(self):
        self.driver.find_element_by_xpath('//button[@class="form-control btn-primary"]').click()

    #定义一个执行方法，执行上面的所有操作
    def perform_login(self,username,password):
        self.input_username(username)
        self.input_password(password)
        self.input_verifycode()
        self.button_login()

    #定义一个注销操作
    def quit(self):
        self.driver.find_element_by_link_text('注销').click()

if __name__ == '__main__':
    mytest = WNLogin()
    mytest.perform_login('admin','Milor123')
    mytest.quit()



