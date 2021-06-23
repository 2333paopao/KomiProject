#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====

from business.test_api.woniusales_member import ApiMember
import unittest

class TestCaseApiMember(unittest.TestCase):

    def test_case_api_add(self):
        reponse = ApiMember().add_member()
        actural_result = reponse.text
        expected_result = 'add-successful'
        self.assertEqual(actural_result,expected_result)

    def test_case_api_search(self):
        response = ApiMember().search_member()
        actual_result = response.text
        expected_result = 'childsex'
        self.assertIn(expected_result,actual_result)

if __name__ == '__main__':
    unittest.main()
