#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====

import uiautomation
from pywinauto.application import Application
import os
import subprocess

class PyUiAuto:
    def __init__(self):
        self.app_path = 'C:/Windows/System32/notepad.exe'
        result1 = subprocess.Popen(self.app_path)
        print(result1)

    def test_notepad(self):
        notepadApp = uiautomation.WindowControl(searchDepth=1, Name='无标题 - 记事本')
        notepadApp.SetFocus()
        notepadApp.SetTopmost(isTopmost=True)

        # textEditor = notepadApp.EditControl(AutomationId='15')
        # textEditor.Click()
        # textEditor.SendKeys('hello world')
        # menu = notepadApp.MenuItemControl(Name='文件(F)')
        # menu.Click()
        # uiautomation.SendKeys('{Down 4}')
        # uiautomation.SendKeys('ENTER')
        # select = notepadApp.ButtonControl(AutomationName='保存(S)')
        # select.Click()

        app_name = '无标题 - 记事本'
        #将pywinwuto的app连接到已打开的notepad
        app = Application().connect(title_re=app_name, class_name='Notepad')
        #app指定名字，选择控件，输入内容
        app[app_name].Edit.type_keys('hello world!\n',with_spaces=True,with_newlines=True)
        #菜单的选择是'文件(F)->保存(O)' or '文件->保存'
        app[app_name].menu_select('文件->保存')

        fileName = notepadApp.ComboBoxControl(AutomationId='FileNameControlHost')
        fileName.DoubleClick()
        uiautomation.SendKeys('C:\\Users\\Komi\\Desktop\\file01.txt')
        # uiautomation.SendKeys('file01.txt')
        # path = notepadApp.ProgressBarControl(AutomationType='进度栏')
        # path.Click()
        # uiautomation.SendKeys('C:/Users/Komi/Desktop')
        # uiautomation.SendKeys('{Enter}')
        save_button= notepadApp.ButtonControl(AutomationName='1')
        save_button.Click()

if __name__ == '__main__':
    mytest = PyUiAuto()
    mytest.test_notepad()