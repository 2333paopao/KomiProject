#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====

#类反射
class TestClassReflection:
    def attr_a(self):
        print('A属性')

    @classmethod
    def attr_b(cls):
        print('B属性')

if __name__ == '__main__':
    # obj = TestClassReflection()
    if hasattr(TestClassReflection,'attr_a'):    #如果TestClassReflection类中有attr_a
        print('You are already had attr_a, please use it.')
        getattr(TestClassReflection(),'attr_a')()    #？？？

    if hasattr(TestClassReflection,'attr_b'):
        print('You are already had attr_b, please use it.')
        getattr(TestClassReflection,'attr_b')()
