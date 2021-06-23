#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
#导入功能函数
from business.notepad import PyUiAuto

class TestCaseNotepad:
    #将输入的文本内容和文件保存路径作为参数传入
    def __init__(self,text,save_path):
        self.text = text
        self.save_path = save_path

    def test_case_notepad(self):
        #调用功能函数
        PyUiAuto().test_notepad(self.text,self.save_path)
        #进行断言
        with open('../result/result_notepad','a+') as r:
            with open(self.save_path,'r',encoding='utf-8') as f:
                read = f.read()
                print(read)
            if read == self.text:
                r.write('%s写入成功\n'%self.save_path)
                print('测试通过')
            else:
                r.write('%s没有找到或写入失败\n'%self.save_path)
                print('测试失败')
if __name__ == '__main__':
    TestCaseNotepad('一二三四五\n上山打老虎\n','C:\\Users\\Komi\\Desktop\\file01.txt').test_case_notepad()
