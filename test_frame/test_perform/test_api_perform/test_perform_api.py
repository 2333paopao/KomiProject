#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====

import unittest
import time
from HTMLTestRunner_cn import HTMLTestRunner
from test_case.unittest_cases.test_api_case.test_case_api_login import TestCaseApiLogin
from test_case.unittest_cases.test_api_case.test_case_api_member import TestCaseApiMember
from test_case.unittest_cases.test_api_case.test_case_api_batch import TestCaseApiBatch

if __name__ == '__main__':
    tc01 = unittest.TestLoader().loadTestsFromTestCase(TestCaseApiLogin)
    tc02 = unittest.TestLoader().loadTestsFromTestCase(TestCaseApiMember)
    tc03 = unittest.TestLoader().loadTestsFromTestCase(TestCaseApiBatch)
    test_suite = unittest.TestSuite(tests=(tc01,tc02,tc03))
    now = time.strftime('%Y-%m-%d-%H.%M')
    filename = 'D:\\unittest_result\\api_result\\'+now+'-login-report.html'
    fp = open(filename,'wb')

# 需要取消截图功能，文件772、773行代码
    runner = HTMLTestRunner(stream=fp, verbosity=2, title='测试报告',
                            description='unittest report', tester='Komi')
    runner.run(test_suite)
    fp.close()
