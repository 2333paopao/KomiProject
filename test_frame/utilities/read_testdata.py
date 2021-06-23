#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====

import xlrd

class Utility:

    def get_excel(self):
        book = xlrd.open_workbook('../data/testdata.xlsx')
        sheet = book.sheet_by_name('customer')


        # 使用json格式来存储测试信息
        test_info = []

        for i in range(1,4):
            url = sheet.cell(i,2).value
            data = sheet.cell(i,4).value
            temp = str(data).split('\n')

            d = {}
            for t in temp:
                s = t.split('=')
                d[s[0]] = s[1]

            expect = sheet.cell(i,6).value
            di = {'url':url,'data':d,'expect':expect}
            test_info.append(di)

        print(test_info)
        return test_info


if __name__ == '__main__':
    Utility().get_excel()
