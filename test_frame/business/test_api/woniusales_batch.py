#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====

from business.test_api.woniusales_login import ApiLogin

class ApiBatch:
    def __init__(self):
        self.base_url = 'http://172.16.8.99:8001/WoniuSales1.4'
        self.session = ApiLogin().get_session()

    def batch_upload(self):
        upload_url = '/goods/upload'
        #首先清楚，requests的数据格式什么，或者什么类型的数据
        files = {
            "batchname":(None,"woniu_test"),
            #filename可以是任意的
            #打开一个文件才是文件对象fileobj
            "batchfile":("anyname",open('C:\\Users\\Komi\\Desktop\\testdata_upload.xls','rb'),
                         "application/vnd.ms-excel")
        }
        res = self.session.post(url=self.base_url+upload_url,files=files)
        # print(res)
        print(res.text)
        return res

if __name__ == '__main__':
    mytest = ApiBatch()
    mytest.batch_upload()