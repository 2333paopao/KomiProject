#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====

import time
import uiautomation
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains

class SeleniumMethod:
    def __init__(self):
        self.driver = webdriver.Chrome()
        #最大化窗口
        self.driver.maximize_window()
        #隐式等待
        self.driver.implicitly_wait(30)

    def basic_method(self):
        self.driver.get('https://www.12306.cn/')
        # driver.refresh()
        # driver.back()
        # driver.forward()
        # driver.close()
        # driver.find_element_by_id('').click()
        # driver.find_element_by_id('').clear()
        # driver.find_element_by_id('').send_keys('西安北')
        #关闭所有窗口
        # driver.quit()

    #切换窗口
    def switch_window(self):
        self.driver.get('')


    def switch_iframe(self):
        #进入网站
        self.driver.get('https://user.qzone.qq.com/1141520403/infocenter')
        time.sleep(5)
        #切换到登陆头像所在的iframe
        iframe1 = self.driver.find_element_by_id('login_frame')
        self.driver.switch_to.frame(iframe1)
        #点击头像登录
        self.driver.find_element_by_id('img_out_1141520403').click()
        time.sleep(10)
        #点击日志进入
        self.driver.find_element_by_link_text('日志').click()
        #切换到日志所在的iframe
        # iframe2 = self.driver.find_element_by_id('tblog')
        # self.driver.switch_to.frame(iframe2)
        self.driver.switch_to.frame('tblog')
        time.sleep(10)
        #点击进入写日志界面
        self.driver.find_element_by_link_text('写日志').click()
        time.sleep(5)
        #通过xpath找到标题输入框，输入内容
        self.driver.find_element_by_xpath('//div/input[@id="blog-title-input"]').send_keys('This is testing')
        #切换到内容区所在的iframe
        iframe3 = self.driver.find_element_by_id('blogContent_Iframe')
        self.driver.switch_to.frame(iframe3)
        #通过xpath找到内容输入框，并输入内容
        text = self.driver.find_element_by_xpath('/html/body[@class="blog_details_20120222"]')
        text.send_keys('门前大桥下，游过一群鸭')
        # 发表按钮位于内容输入框的上一层iframe，需要返回上一层iframe
        self.driver.switch_to.parent_frame()
        # 通过xpath找到发表按钮，点击
        self.driver.find_element_by_xpath('//span[@id="blogContent_submit"]').click()

        #定位到发表按钮位置后，将滚动条拉到按钮所在位置，再点击
        targetElem = self.driver.find_element_by_xpath('//button[@id="saveBlogButton"]')
        self.driver.execute_script('arguments[0].scrollIntoView();',targetElem)
        targetElem.click()

    #控制滚动条
    def do_scroll(self):
        self.driver.get('http://www.woniuxy.com/train/teacher.html')
        #首先定位元素，定位到元素后，使用js code将滚动条拉到目标元素所在的位置
        targetElem = self.driver.find_element_by_xpath("//div[contains(text(),'联系我们')]")
        self.driver.execute_script('arguments[0].scrollIntoView();',targetElem)

    #select
    def select_method(self):
        self.driver.get('http://www.woniuxy.com/live')
        time.sleep(3)
        targetElem = self.driver.find_element_by_id('searchlivebymajor')
        Select(targetElem).select_by_visible_text('Web前端开发')

    def ActionChains(self):
        self.driver.get('https://www.bejson.com/')
        time.sleep(3)
        #实例化一个actions使用当前的driver
        actions = ActionChains(self.driver)
        #定位前端下拉框的位置
        qianduan = self.driver.find_element_by_xpath('//li[@id="dropdown4"]')
        #定位图片压缩工具的位置
        yasuo = self.driver.find_element_by_xpath\
            ('//a[(contains(@class,"text-nav-info-import") and contains(text(),"图片压缩"))]')
        #将鼠标移动到【前端】并点击
        actions.move_to_element(qianduan).click()
        #将鼠标移动到【图片压缩工具】并点击
        actions.move_to_element(yasuo).click()
        #执行actions操作
        actions.perform()
        time.sleep(3)
        actions = ActionChains(self.driver)
        xuanze = self.driver.find_element_by_xpath('//button[@id="compressBtn"]')
        actions.move_to_element(xuanze).click()
        actions.perform()

        #使用uiautomation上传图片
        time.sleep(3)
        pop = uiautomation.WindowControl(searchDepth=2, Name='打开')
        pop.SetFocus()
        pop.SetTopmost(isTopmost=True)
        fileName = pop.ComboBoxControl(AutomationId='1148')
        fileName.Click()
        uiautomation.SendKeys('D:\\test_frame\\images\\1111.png')
        # pop.ButtonControl(AutomationName='打开(O)').Click()
        uiautomation.SendKeys('{Enter}')
        download = self.driver.find_element_by_xpath('//a[contains(text(),"下载压缩图片")]')
        # download.click()


    def webdriver_wait(self):
        self.driver.get('http://www.woniuxy.com/train/teacher.html')


if __name__ == '__main__':
    mytest = SeleniumMethod()
    mytest.do_scroll()