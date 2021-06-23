#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====

import requests

class Api:
    def __init__(self):
        self.base_url = 'http://ws.webxml.com.cn/WebServices/MobileCodeWS.asmx/getMobileCodeInfo'
        self.session = requests.Session()

    def get(self):
        # data = 'mobileCode=13288888888&userID='
        data = {'mobileCode':'13288888888','userID':''}
        # header = {'Content-Type':'application/x-www-form-urlencoded'}
        response = self.session.post(url=self.base_url,data=data)
        print(response.text)

if __name__ == '__main__':
    mytest = Api()
    mytest.get()

