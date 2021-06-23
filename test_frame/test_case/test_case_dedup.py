#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====

#调取要测的去重功能函数
from business.dedup import Dedup

#定义测试用例的类
class TestCaseDedup:
    #将需要测试的数据作为对象（data），该处为形式参数
    def __init__(self,data):
        self.data = data

    #定义断言方法
    def test_case_dedup(self):
        #self.data的实际参数是通过yield返回的测试数据，所以要通过循环一条一条的读取
        for i in self.data:
            #数据的第二位是期望结果
            exptected_result = i[1]
            #调取去重函数，将测试数据的第一位作为实际参数传入去重函数中，得到去重函数运行的实际结果
            actual_result = Dedup(i[0]).dedup()
            #打开存放测试结果的文档
            with open('../result/result_dedup','a+') as  f:
                #进行断言操作
                if actual_result == exptected_result:
                    print('测试通过')
                    f.write('%s测试通过\n'%i[0])
                else:
                    print('测试失败')
                    f.write('%s测试失败\n'%i[0])
                #注意这里循环中不能使用return返回结果
                #一旦return就会导致yield循环就中断，等于执行了一次

    def test_case2(self):
        for i in self.data:
            exptected_result = i[1]
            actual_result = Dedup(i[0]).dedup()
            with open('../result/result_dedup','a+') as  f:
                if actual_result == exptected_result:
                    print('测试通过')
                    f.write('%s测试通过\n'%i[0])
                else:
                    print('测试失败')
                    f.write('%s测试失败\n'%i[0])

if __name__ == '__main__':
    pass