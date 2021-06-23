#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====

from business.test_api.woniusales_batch import ApiBatch
import unittest

class TestCaseApiBatch(unittest.TestCase):

    def test_case_api_batch(self):
        reponse = ApiBatch().batch_upload()
        actural_result = reponse.text
        expected_result = '背带裤套装'
        self.assertIn(expected_result,actural_result)

if __name__ == '__main__':
    unittest.main()
