#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import time
import sys
import os

class TestNews:
    def __init__(self):
        self.desired_capabilities = {
                                        "platformName": "Android",
                                        "platformVersion": "6.0.1",
                                        "deviceName": "DemoDevice",
                                        "appPackage": "com.netease.newsreader.activity",
                                        "appActivity": "com.netease.nr.biz.ad.AdActivity",
                                        "uuid": "127.0.0.1:7555"
                                    }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub',self.desired_capabilities)

    def test_shouye(self):
        time.sleep(10)
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("我")').click()




if __name__ == '__main__':
    mytest = TestNews()
    mytest.test_shouye()