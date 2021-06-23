#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====

#定义一个父类
class Father(object):
    #定义父类的方法
    def action(self):
        print('抽卡抽卡')

#定义一个子类
#将父类作为参数传入子类，子类可以继承父类
class Hero(Father):
    #定义类的属性
    test_var = '欧气爆棚~~'
    #定义对象的初始化属性
    def __init__(self,name,level):
        #self是对象(类的实例化后的实体)本身
        #name和level是实例化要传入的参数，在这里是形参
        self.n = name
        self.l = level

    #定义对象（实例）方法
    #实例方法只能被对象调用
    def method1(self):
        # 如何在实例方法中调用类的属性
        print(Hero.test_var+'获得式神%s'%self.n)

    #定义对象（实例）方法
    def method2(self):
        print('式神等级%s'%self.l)
        self.class_method()
        #对象方法可以调用类方法，不能调用静态方法

    #装饰器本质上是一个Python函数或类，它可以让其他函数或类在不需要做任何代码修改的前提下增加额外功能，
    #装饰器的返回值也是一个函数/类对象
    #装饰器的作用是将对象方法转换成类的方法，类可以直接调用类方法，不需要实例。
    #类方法由@classmethod装饰
    #类方法，第一个参数必须要默认传类，一般习惯用cls
    @classmethod
    def class_method(cls):
        # cls是类本身
        print('类方法')

    #静态方法由@staticmethod装饰
    #静态方法相当于普通方法，不需要传入实例参数
    #把对象方法转换为静态方法
    @staticmethod
    def static_method():
        print('静态方法')

if __name__ == '__main__':
    # if __name__ == '__main__'当别的模块调用本模块的方法时，不执行本行代码以下的部分

    #实例化一个对象
    h1 = Hero('云外镜','SSR')
    #子类可以调用继承的父类的方法
    h1.action()
    #子类对象调用自身的方法
    h1.method1()
    h1.method2()

    #类可以直接调用类方法
    Hero.class_method()
    #对象也可以调用类方法，不过需要传入对象
    h1.class_method()

    #类调用静态方法
    Hero.static_method()
    #对象调用静态方法
    h1.static_method()