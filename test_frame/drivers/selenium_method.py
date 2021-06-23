#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====

import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class SeleniumMethod:
    def __init__(self):
        #
        self.driver = webdriver.Chrome()
        #最大化窗口
        self.driver.maximize_window()
        #隐式等待
        self.driver.implicitly_wait(30)

    #控制滚动条
    #将目标位置的xpath传入
    def do_scroll(self,element_xpath):
        #首先定位元素
        targetElem = self.driver.find_element_by_xpath(element_xpath)
        #定位到元素后，使用js code将滚动条拉到目标元素所在的位置
        self.driver.execute_script('arguments[0].scrollIntoView();',targetElem)

    #下拉选择框
    #将下拉框的id和要选的选项传入
    def select_method(self,select_id,option):
        #通过id定位到下拉选择框
        targetElem = self.driver.find_element_by_id(select_id)
        #选择选项
        Select(targetElem).select_by_visible_text(option)

    #拖拽
    #将来源位置和目标位置传入
    def drag_drop(self,source_css,target_css):
        #使用css语法定位到来源位置和目标位置
        sourceElem = self.driver.find_element_by_css_selector(source_css)
        targetElem = self.driver.find_element_by_css_selector(target_css)
        #实例化一个actions使用当前的driver
        actions = ActionChains(self.driver)
        #第一种写法
        #定义动作链，添加源位置和目标位置
        actions.drag_and_drop(sourceElem,targetElem)
        #执行actions
        actions.perform()
        #第二种写法
        # ActionChains(self.driver).drag_and_drop(sourceElem,targetElem).perform()
        #第二种写法能够避免每执行一次就要实例化一次

    #截图
    #将截图的保存路径传入
    def screenshot(self,save_path):
        self.driver.get_screenshot_as_file(save_path)
        #路径需要完整路径，如 D:\images\xxx.png

    #动作链
    #将目标位置的xpath传入
    def action_chains(self,goal_xpath):
        #实例化一个actions使用当前的driver
        actions = ActionChains(self.driver)
        #通过xpath定位到目标位置
        goalElem = self.driver.find_element_by_xpath(goal_xpath)
        #鼠标移动到目标位置并点击
        actions.move_to_element(goalElem).click()
        #执行actions
        actions.perform()

    #等待
    def webdriver_wait(self,*locator,timeout=30,FREQ=0.5):
        #WebDriverWait参数说明（driver；超时时间；查找频率）
        wait = WebDriverWait(self.driver,timeout,FREQ)
        #返回找到的元素 *locator是自动解压开传入的元组参数，如（By.ID,"ID"）
        element = wait.until(EC.presence_of_element_located(*locator))
        return element


if __name__ == '__main__':
    mytest = SeleniumMethod()