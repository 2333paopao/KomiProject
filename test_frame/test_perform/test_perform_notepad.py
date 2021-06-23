#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
#导入测试用例
from test_case.test_case_notepad import TestCaseNotepad

class TestPerformNotepad:
    #参数为输入文本和文件保存路径
    def __init__(self,text,save_path):
        self.text = text
        self.save_path = save_path

    def test_perform_notepad(self):
        #调用测试用例
        TestCaseNotepad(self.text,self.save_path).test_case_notepad()

if __name__ == '__main__':
    #将输入文本和保存路径传入
    TestPerformNotepad('一二三四五\n上山打老虎\n','C:\\Users\\Komi\\Desktop\\file01.txt').test_perform_notepad()
