#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====

from business.test_api.woniusales_login import ApiLogin

class ApiMember:
    def __init__(self):
        self.base_url = 'http://172.16.8.99:8001/WoniuSales1.4'
        self.session = ApiLogin().get_session()

    def add_member(self):
        add_member_uri = '/customer/add'
        add_member_params = {'customername':'', 'customerphone':233333445566, 'childsex':'女',
                             'childdate':'2020-02-05','creditkids':0, 'creditcloth':0}
        res = self.session.post(url=self.base_url+add_member_uri,data=add_member_params)
        print(res.text)
        return res

    def search_member(self):
        search_member_uri = '/customer/search'
        search_member_params = 'customerphone=123&page=1'
        headers = {"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8"}
        res = self.session.post(url=self.base_url+search_member_uri,data=search_member_params,headers=headers)
        print(res.text)
        return res

if __name__ == '__main__':
    mytest = ApiMember()
    mytest.search_member()