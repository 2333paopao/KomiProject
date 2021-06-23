#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====

from business.test_api.woniusales_login import ApiLogin
import unittest

class TestCaseApiLogin(unittest.TestCase):

    def test_case_api_login(self):
        reponse = ApiLogin().api_login()
        actural_result = reponse.text
        expected_result = 'login-pass'
        self.assertEqual(actural_result,expected_result)

if __name__ == '__main__':
    unittest.main()
