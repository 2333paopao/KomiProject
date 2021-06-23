#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====

#定义一个解析数据的类
class Read_Dedup:
    #将要解析的文件路径作为对象
    def __init__(self,path):
        self.path = path

    #定义解析的方法
    def read_dedup(self):
        #打开文件路径
        with open(self.path,'r') as f:
            #进行解析
            for line in f:
                line = line.replace('\n','')
                line1 = line.split(' ')
                #以空格切割后的数据为两个字符串'[]','[]'，下面对字符串进行转换处理
                list_data = []
                for i in line1:
                    #使用eval方法可以去掉引号，将字符串转换为引号中原本的格式
                    #转换后的数据添加到空列表中，形成一个二维列表
                    list_data.append(eval(i))
                #使用yield可以一行一行的返回数据，方便后期测试用例一条一条的测试，需要通过循环读取所有返回数据
                yield list_data

if __name__ == '__main__':
    test_data = Read_Dedup('../data/data_dedup').read_dedup()
    print(next(test_data))
    # for i in test_data:
    #     print(i)