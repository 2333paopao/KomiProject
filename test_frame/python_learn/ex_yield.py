#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====

class ExYield:
    def __init__(self):
        pass
    @classmethod
    def ex_yield(cls):
        with open('txt1') as f:
            for line in f:
                yield line  #一行一行的返回，替换return，每次只返回一行

if __name__ == '__main__':
    mytest = ExYield.ex_yield()
    print(mytest)
    print(next(mytest))
    print(next(mytest))
    print(next(mytest))
