#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====

import os
import re

class GetAppDevice:

    def get_device(self):
        command1 = 'adb devices -l >> D:/Android/temp.txt'
        os.popen(command1)

    def analysis_result(self):
        with open('D:/Android/temp.txt','r+') as f:
            result = f.read()
            print(result)
            list_device = re.findall('(?<=\n).*?(?=\s\s)',result)
            print(list_device)
            return list_device

if __name__ == '__main__':
    mytest = GetAppDevice()
    # mytest.get_device()
    mytest.analysis_result()



