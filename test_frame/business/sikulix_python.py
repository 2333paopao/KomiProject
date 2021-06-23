#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====

import jpype
#把每一个具体的方法或要做的事情放到一起（内聚），把和sikulix相关的操作和启动jvm的内容，
#全部放到sikulix_python模块，也就是SikulixPython类中

class SikulixPython:
    def __init__(self,jar_path):
        #找jvm的环境变量，JAVA_HOME,%JAVA_HOME%,PATH绝对路径
        self.jvm_path = jpype.getDefaultJVMPath()
        self.jar_path = jar_path

    def start_jvm(self):
        #使用sikulix jar包启动jvm
        if not jpype.isJVMStarted():   #判断jvm是否启动
            jpype.startJVM(self.jvm_path,'-Djava.class.path=%s' % (self.jar_path))
            print('starting......')

    #导入模块的封装，最后返回的实例化的对象
    def sikulix_screen(self):
        #导入包 class_screen ---> 'org.sikuli.script.Screen'
        sikulix_screen = jpype.JClass('org.sikuli.script.Screen')
        screen = sikulix_screen() #进行实例化
        return screen

    #导入模块的封装，最后返回的实例化的对象
    def key(self):
        #导入class_key ---> 'org.sikuli.script.Key'
        key = jpype.JClass('org.sikuli.script.Key')
        return key

    #封装的是sikulix的doubleClick()
    def doubleClick(self,png_path):
        #调用实例化的screen，执行click操作
        dbClick = self.sikulix_screen().doubleClick(png_path)
        return dbClick

    def click(self,png_path):
        click = self.sikulix_screen().click(png_path)
        return click

    def type(self,png_path):
        type = self.sikulix_screen().type(png_path)
        return type

if __name__ == '__main__':
    pass