#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====

import requests

class ApiLogin:
    def __init__(self):
        self.base_url = 'http://172.16.8.99:8001/WoniuSales1.4'
        self.session = requests.Session()

    #登录
    def api_login(self):
        login_uri = '/user/login'
        login_data = {'username':'admin','password':'Milor123','verifycode':'0000'}
        custom_headers = {'Content-Type':'application/x-www-form-urlencoded;charset=UTF-8'}
        response = self.session.post(url=self.base_url+login_uri,data=login_data,headers=custom_headers)
        # print(response.text)
        return response

    def get_session(self):
        self.api_login()
        print(self.session.cookies)
        return self.session



if __name__ == '__main__':
    mytest = ApiLogin()
    mytest.get_session()
