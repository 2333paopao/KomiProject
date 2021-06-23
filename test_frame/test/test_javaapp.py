#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====

#导入
import jpype   #sikulix是基于jpython的，所以需要jpype
import os

#流水线的代码给了执行的顺序，但是缺少归类，需要调用的时候得重复写

#1、找jvm的环境变量，JAVA_HOME,JAVA_HOME%,PATH绝对路径
jvm_path = jpype.getDefaultJVMPath()
print(jvm_path)

jar_path = os.path.join(os.path.abspath('.'),r'D:/test_frame/library/')

#启动jvm指定jar包，运行jar
if not jpype.isJVMStarted():     #判断jvm是否启动
    jpype.startJVM(jvm_path,'-Djava.class.path=%s' % (jar_path + 'sikulixapi.jar'))
    print('starting......')

#测试环境ok，执行一段java的打印代码
jpype.java.lang.System.out.println('hello world')
#进入java运行环境
#import Java包
sikulix_screen = jpype.JClass('org.sikuli.script.Screen') #类，和屏幕相关，截图，相当于import功能，导入模块
sikulix_key = jpype.JClass('org.sikuli.script.Key') #键盘相关操作
screen = sikulix_screen() #类实例化
Key = sikulix_key()

#导入组合键的类
# sikulix_keymodifier = jpype.JClass('org.sikuli.script.KeyModifier')
# #进行实例化
# Keys = sikulix_keymodifier()
# screen('a',Keys.CTRL)  #ctrl+A

#调用对象方法
screen.doubleClick(r'D:\sikulix\test_woniu.sikuli\1592810356332.png')
screen.click(r'D:\sikulix\test_woniu.sikuli\1592802616682.png')
screen.type('http://172.16.8.65:8080/WoniuSales1.4/')
screen.type(Key.ENTER)
screen.type(Key.ENTER)
screen.type(r'D:\sikulix\test_woniu.sikuli\1592802655670.png','admin')
screen.type(Key.ENTER)
screen.type(Key.TAB)
screen.type('Milor123')
screen.type(Key.TAB)
screen.type('0000')
screen.type(Key.ENTER)