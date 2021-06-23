#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====

#定义去重的类
class Dedup:
    #将需要去重的列表作为对象，该处为形式参数
    def __init__(self,list0):
        self.list0 = list0

    #定义去重的方法
    def dedup(self):
        #定义一个空列表用来存放去重后的数据
        list1 = []
        #利用循环，将不存在于list1的数据放入，可以达到去重的效果z
        for i in self.list0:
            if i not in list1:
                list1.append(i)
        return list1

if __name__ == '__main__':
    print(Dedup([1,32,132,5,1,35,4,8,32]).dedup())