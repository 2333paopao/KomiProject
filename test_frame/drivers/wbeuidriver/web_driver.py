#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
import time
from selenium import webdriver

#定义返回单例模式中driver的类
class WebDriver:
    #定义类的属性，它停留在内存中保持地址的唯一性，默认值为None，目的是为了判断里面是否有driver
    driver = None
    #临时将浏览器类型和url放在这里，可以不放在这里
    browser = 'Firefox'
    url = 'http://172.16.8.49:8080/WoniuSales1.4/'

    def __init__(self):
        pass

    #类方法，将普通的方法（对象方法）转变为类方法，直接调用，无需实例
    @classmethod
    #定义一个类方法，接受来自配置文件的参数，完整相关webdriver初始功能
    def get_driver(cls):
        #判断是否已经有webdriver存在，如果不存在则执行下面的实例化driver的操作，如果存在，直接返回已经存在的driver
        if cls.driver is None:
            #判断浏览器类型，告诉webdriver该用哪个类型的浏览器，用哪个原生API
            if cls.browser == 'Firefox':
                #实例化webdriver，使用Firefox
                cls.driver = webdriver.Firefox()
            else:
                #实例化webdriver，使用Chrome
                cls.driver = webdriver.Chrome()

            #浏览器最大化，隐式等待，打开url
            cls.driver.maximize_window()
            cls.driver.implicitly_wait(10)
            cls.driver.get(cls.url)
        #返回实例化后的webdriver，如果存在直接返回
        return cls.driver

    @classmethod
    def wait_element_present(cls,how,what,timeout=30):  #how=id/xpath/classname   what='//div[@id="xx"]'
        for t in range(timeout):
            try:
                element = cls.driver.find_element(how,what)  #查找元素的方法
                return element  #找到后返回
            except Exception as ex:  #没有找到时打印异常信息
                print(ex)  #打印，等后期学了日志后可放进日志
            finally:
                time.sleep(1)  #设置强制等待时间
        return None  #如果没有找到，返回一个None，为了方便判断是否找到element


    @classmethod
    def is_element_present(cls,how,what,timeout=1):
        element = cls.wait_element_present(how,what,timeout)
        if element is None:
            return False
        return True

if __name__ == '__main__':
    mytest = WebDriver()
    mytest.get_driver()