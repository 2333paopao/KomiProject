#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====

import json
class ReadJson:
    def __init__(self,path):
        self.path = path

    def read_json(self):
        with open(self.path,'r+') as f:
            result = f.read()
            result1 = json.loads(result)
            print(result1)
            for i in result1:
                print(result1[i])

if __name__ == '__main__':
    mytest = ReadJson('D:\\test_frame\\data\\data_json')
    data = mytest.read_json()
