#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
import time
#导入功能函数
from business.sikulix_python import SikulixPython

class TestCaseWoniu:
    #将jar包和用来断言的图片作为参数传入
    def __init__(self,image_path,jar_path):
        self.image_path = image_path
        self.jar_path = jar_path

    def woniu(self):
        #实例化功能函数
        s = SikulixPython(self.jar_path)
        #启动java环境
        s.start_jvm()
        #调用键盘操作函数
        key = s.key()
        #进行登录操作
        #组合键?
        s.doubleClick(r'D:\sikulix\test_woniu.sikuli\1592810356332.png')
        time.sleep(3)
        s.click(r'D:\sikulix\test_woniu.sikuli\1592802616682.png')
        s.type('http://172.16.8.65:8080/WoniuSales1.4/')
        s.type(key.ENTER)
        s.type(key.ENTER)
        s.click(r'D:\sikulix\test_woniu.sikuli\1592802655670.png')
        s.type('admin')
        s.type(key.ENTER)
        s.type(key.TAB)
        s.type('Milor123')
        s.type(key.TAB)
        s.type('0000')
        s.type(key.ENTER)
        #判断图片是否存在
        image = SikulixPython.sikulix_screen(self.jar_path).exists(self.image_path)
        with open('../result/result_sikulix','a+') as f:
            if image:
                print('登陆成功')
                f.write('http://172.16.8.65:8080/WoniuSales1.4/登陆成功')
            else:
                print('很抱歉，没有找到')
                f.write('很抱歉，没有找到http://172.16.8.65:8080/WoniuSales1.4/')

if __name__ == '__main__':
    TestCaseWoniu('D:/sikulix/test_woniu.sikuli/1592829877581.png','D:/test_frame/library/sikulixapi.jar')