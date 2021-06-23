#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====

import uiautomation
from pywinauto.application import Application
import subprocess

class PyUiAuto:
    def __init__(self):
        self.app_path = 'C:/Windows/System32/notepad.exe'
        path = subprocess.Popen(self.app_path)
        print(path)

    #封装？
    def test_notepad(self,text,save_path):
        notepadApp = uiautomation.WindowControl(searchDepth=1, Name='无标题 - 记事本')
        notepadApp.SetFocus()  #聚焦
        notepadApp.SetTopmost(isTopmost=True)  #置顶

        app_name = '无标题 - 记事本'
        #将pywinwuto的app连接到已打开的notepad
        app = Application().connect(title_re=app_name, class_name='Notepad')
        #app指定名字，选择控件，输入文本
        app[app_name].Edit.type_keys(text,with_spaces=True,with_newlines=True)
        #菜单的选择是'文件(F)->保存(O)' or '文件->保存'
        app[app_name].menu_select('文件->保存')

        fileName = notepadApp.ComboBoxControl(AutomationId='FileNameControlHost')
        fileName.DoubleClick()
        uiautomation.SendKeys(save_path)
        save_button= notepadApp.ButtonControl(AutomationId='1')
        save_button.Click()

if __name__ == '__main__':
    mytest = PyUiAuto()
    mytest.test_notepad('hello,i am here\n','C:\\Users\\Komi\\Desktop\\file01.txt')
