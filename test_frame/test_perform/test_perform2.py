#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====

#思路
#找到用例
#将用例添加到管理执行的办法
#需要一个runner TextTestRunner
#报告 - 写在文件，解析再生成报告，边执行边写报告，最后汇总

import unittest
import time
from HTMLTestRunner_cn import HTMLTestRunner
from test_case.unittest_cases.test_case_login import TestCaseLogin
from test_case.unittest_cases.test_case_sales import TestCaseSales

if __name__ == '__main__':

    #1、装载测试用例
    tc01 = unittest.TestLoader().loadTestsFromTestCase(TestCaseLogin)
    tc02 = unittest.TestLoader().loadTestsFromTestCase(TestCaseSales)
    #2、测试套件suite
    test_suite = unittest.TestSuite(tests=(tc01,tc02))
    #3、进行执行，将测试套件和runner（执行者）关联起来
    #  生成runner（生成一个执行器）
    #  利用时间生成动态的文件名字
    now = time.strftime('%Y-%m-%d-%H.%M')
    filename = 'D:\\unittest_result\\'+now+'-report.html'
    fp = open(filename,'wb')
    #生成runner - HTMLTestRunner
    #stream -> file，verbosity 详细程度
    runner = HTMLTestRunner(stream=fp, verbosity=2)
    #关联和执行
    runner.run(test_suite)
    fp.close()