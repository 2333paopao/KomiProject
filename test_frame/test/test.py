#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====

from utilities.read_testdata import Utility
from parameterized import parameterized
import requests
import unittest

class TestQuery(unittest.TestCase):
    read = Utility().get_excel()

    def setUp(self):
        self.session = requests.Session()
        login_url = 'http://172.16.8.50:8001/WoniuSales1.4/user/login'
        login_data = {'username':'admin','password':'Milor123','verifycode':'0000'}
        self.session.post(url=login_url,data=login_data)

    @parameterized.expand([
                            (read[0]['url'],read[0]['data'],read[0]['expect']),
                            (read[1]['url'],read[1]['data'],read[1]['expect']),
                            (read[2]['url'],read[2]['data'],read[2]['expect'])
                            ])
    def test_query(self,query_url,query_data,expect):
        response = self.session.post(url=query_url,data=query_data)
        actural = response.text
        self.assertEqual(actural,expect)

if __name__ == '__main__':
    unittest.main()

