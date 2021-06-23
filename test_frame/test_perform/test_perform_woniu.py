#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
#导入测试用例
from test_case.test_case_woniu import TestCaseWoniu

class Perform:
    def __init__(self,image_path,jar_path):
        self.image_path = image_path
        self.jar_path = jar_path

    def perform(self):
        #调用测试用例
        TestCaseWoniu(self.image_path,self.jar_path).woniu()

if __name__ == '__main__':
    #将断言图片和jar包传入
    Perform('D:/sikulix/test_woniu.sikuli/1592829877581.png','D:/test_frame/library/sikulixapi.jar').perform()