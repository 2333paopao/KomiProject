#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====

#调取数据解析
from utilities.read_dedup import Read_Dedup
#调取测试用例
from test_case.test_case_dedup import TestCaseDedup
#定义执行测试用例的类
class Test_Perform_Dedup:
    def __init__(self):
        pass

    #没有实例对象，所以将对象方法转为类方法，类可以直接调用
    @classmethod
    def test_perform_dedup(cls):
        #将要解析的路径传入解析类中进行解析
        #再将解析出来的原始数据传入测试用例中进行断言
       TestCaseDedup(Read_Dedup('../data/data_dedup').read_dedup()).test_case_dedup()
       TestCaseDedup(Read_Dedup('../data/data_dedup2').read_dedup()).test_case2()

if __name__ == '__main__':
    #执行测试用例
    Test_Perform_Dedup.test_perform_dedup()