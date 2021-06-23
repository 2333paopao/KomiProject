#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====

import time
import hashlib
import requests

class ApiSignature:
    def __init__(self):
        self.time_stamp = str(int(time.time()))

    def signature_create(self):
        #生成签名的字符串
        print('时间戳',self.time_stamp)
        #特定字符串+时间戳
        md5_str = '0|0|v2/Passport/login||%s'%self.time_stamp
        print('md5字符串',md5_str)
        #生成Signature
        signature = hashlib.md5(md5_str.encode('utf-8')).hexdigest()
        print(signature)
        return signature

    def signature_login(self):
        signature = self.signature_create()
        #自定义头（content-type，Signature，request-time，Client-version）
        headers = {'Content-Type':'application/json','Client-Version':'Windows',
                   'Signature':signature,'Request-Time':self.time_stamp}
        params = {
            'phone':'18049586659',
            'password':'wn@123',
            'shop_id':'null'
        }
        #json_str = json.dumps(params)
        #data，如果数据是json就用data
        #如果数据是字典就直接用json
        res = requests.request(method='POST',url='https://snailpet.com/v2/Passport/login',
                               json=params,headers=headers)
        print(res.text)

if __name__ == '__main__':
    mytest = ApiSignature()
    mytest.signature_login()