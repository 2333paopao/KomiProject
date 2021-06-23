#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====

from business.webui.wns_login import WNLogin
from business.webui.wns_sales import WNSales
from business.webui.wns_member import WNMember

class TestPerformWNLogin:
    def __init__(self):
        pass

    def test_perfrom_wns(self):
        #调用登录类中的执行方法，传入用户名、密码、验证码
        WNLogin().perform_login('admin','Milor123','0000')
        #调用销售类中的执行方法，传入商品条码、会员电话
        # WNSales().perform_sales('0','13200000000')
        #调用会员类中的执行方法，传入会员电话、姓名、性别
        # WNMember().perform_member('12345','admin','女')

if __name__ == '__main__':
    mytest = TestPerformWNLogin()
    mytest.test_perfrom_wns()
