#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====

import uiautomation
import os
import re
import subprocess

class PyUiAuto:
    def __init__(self):
        self.app_path = 'C:/Windows/System32/calc.exe'
        # os.system(self.app_path)
        # result = os.popen(self.app_path)
        result1 = subprocess.Popen(self.app_path)
        print(result1)

    def test_calc(self):
        #找到目标app，进行置顶
        calcapp = uiautomation.WindowControl(searchDepth=1, Name='计算器')
        calcapp.SetFocus()  #聚焦
        calcapp.SetTopmost(isTopmost=True)
        #找元素（控件，对象）
        #找的动作，按照automationid查找目标元素，控件
        button3 = calcapp.ButtonControl(AutomationId='num3Button')
        #找到控件后，就需要进行点击
        button3.Click()
        button_plus = calcapp.ButtonControl(AutomationId='plusButton')
        button_plus.Click()
        button5 = calcapp.ButtonControl(AutomationId='num5Button')
        button5.Click()
        button_equal = calcapp.ButtonControl(AutomationId='equalButton')
        button_equal.Click()
        result = calcapp.TextControl(AutomationId='CalculatorResults').Name
        print(result)

if __name__ == '__main__':
    mytest = PyUiAuto()
    mytest.test_calc()
