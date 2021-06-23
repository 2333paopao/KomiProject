#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====

import requests

class ApiLib:
    def __init__(self):
        self.base_url = 'http://172.16.8.49:8080/WoniuSales1.4'
        self.session = requests.Session()

    def api_login(self):
        api_uri = '/user/login'

        # 1、用的字典格式的数据进行post
        login_data = {'username':'admin','password':'Milor123','verifycode':'0000'}
        # response = requests.request(method='POST',url=self.base_url+api_uri,data=login_data)

        # 2、用的字符串格式的数据进行post
        # login_data = 'username=admin&password=Milor123&verifycode=0000'
        # 定制的request headers，如果需要，按照标准头的内容，设计成字典格式，将需要的头内容按key，value形式存在字典里
        custom_headers = {'Content-Type':'application/x-www-form-urlencoded;charset=UTF-8'}
        response = self.session.post(url=self.base_url+api_uri,data=login_data,headers=custom_headers)

        # text返回的是正常的返回值
        print(response.text)
        # content返回的类型是字节，通过字节长度--len()可以判断返回内容的大小
        # print(response.content)
        # print(response.headers)
        print(response.cookies)
        return response

    def get_cookie(self):
        res = self.api_login()
        print(res.cookies)
        return res.cookies

    def add_member(self):
        add_member_uri = '/customer/add'
        add_member_params = {'customername':'', 'customerphone':112233445566, 'childsex':'女', 'childdate':'2020-02-05',
                             'creditkids':0, 'creditcloth':0}
        res = self.session.post(url=self.base_url+add_member_uri,data=add_member_params)
        print(res.text)

    def requests_upload(self):
        upload_url = '/goods/upload'
        #首先清楚，requests的数据格式什么，或者什么类型的数据
        files = {
            "batchname":(None,"WNS20200708"),
            #filename可以是任意的
            #打开一个文件才是文件对象fileobj
            "batchfile":("anyname",open('C:\\Users\\Komi\\Desktop\\testdata_upload.xls','rb'),
                         "application/vnd.ms-excel")
        }
        res = requests.request(method='POST',url=self.base_url+upload_url,files=files,cookies=self.get_cookie())
        print(res.text)



if __name__ == '__main__':
    mytest = ApiLib()
    mytest.requests_upload()