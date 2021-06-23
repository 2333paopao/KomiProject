#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====

class ExEval:
    def __init__(self):
        pass
    @classmethod
    def ex_eval(cls):
        str = '10*10+50'
        return str

result = ExEval.ex_eval()
print(result)
print(eval(result))