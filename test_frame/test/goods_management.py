#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
import pymysql
class GoodsMangement(object):
    #建立数据库连接，开启游标
    conn = pymysql.connect("localhost","root","","good_manage")
    cur = conn.cursor()

    #定义十个属性
    def __init__(self):
        self._goodsid = None
        self._batchname = None
        self._goodsname = None
        self._goodscolor = None
        self._goodstype = None
        self._quantity = None
        self._sell_price = None
        self._purchase_price = None
        self._total_price = None
        self._create_time = None


    #定义get和set方法
    @property
    def goodsid(self):
        return self._goodsid

    @goodsid.setter
    def goodsid(self,value):
        if isinstance(value,int):
            self._goodsid = value
        else:
            self._goodsid = int(value)


    @property
    def batchname(self):
        return self._batchname

    @batchname.setter
    def batchname(self,value):
        if isinstance(value,str):
            self._batchname = value
        else:
            self._batchname = str(value)


    @property
    def goodsname(self):
        return self._goodsname

    @goodsname.setter
    def goodsname(self,value):
        if isinstance(value,str):
            self._goodsname = value
        else:
            self._goodsname = str(value)


    @property
    def goodscolor(self):
        return self._goodscolor

    @goodscolor.setter
    def goodscolor(self,value):
        if isinstance(value,str):
            self._goodscolor = value
        else:
            self._goodscolor = str(value)


    @property
    def goodstype(self):
        return self._goodstype

    @goodstype.setter
    def goodstype(self,value):
        if isinstance(value,str):
            self._goodstype = value
        else:
            self._goodstype = str(value)


    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self,value):
        if isinstance(value,int):
            self._quantity = value
        else:
            while True:
                if value.isdigit():
                    self._quantity = int(value)
                    break


    @property
    def sell_price(self):
        return self._sell_price

    @sell_price.setter
    def sell_price(self,value):
        if isinstance(value,float):
            self._sell_price = value
        else:
            self._sell_price = float(value)


    @property
    def purchase_price(self):
        return self._purchase_price

    @purchase_price.setter
    def purchase_price(self,value):
        if isinstance(value,float):
            self._purchase_price = value
        else:
            self._purchase_price = float(value)


    @property
    def total_price(self):
        return self._total_price

    @total_price.setter
    def total_price(self,value):
        if isinstance(value,float):
            self._total_price = value
        else:
            self._total_price = float(value)


    @property
    def create_time(self):
        return self._create_time

    @create_time.setter
    def create_time(self,value):
        if isinstance(value,str):
            self._create_time = value
        else:
            self._create_time = str(value)


    #增加数据
    def add_data(self,table_name,*args):
        #判断传入的参数是否符合要求
        self.goodsid = args[0]
        self.batchname = args[1]
        self.goodsname = args[2]
        self.goodscolor = args[3]
        self.goodstype = args[4]
        self.quantity = args[5]
        self.sell_price = args[6]
        self.purchase_price = args[7]
        self.total_price = args[8]
        self.create_time = args[9]

        sql = "insert into %s (goodsid,batchname,goodsname,goodscolor,goodstype,quantity,sell_price,purchase_price,total_price,create_time) values %s"%(table_name,args)
        #执行
        self.cur.execute(sql)
        self.conn.commit()

    #查找
    #传入表名和要读取的属性名
    def select_data(self,data,table_name):
        sql = "select %s from %s"%(data,table_name)
        self.cur.execute(sql)
        result = self.cur.fetchall()
        print(result)
        return result

    #定义删除函数，传入表名和要删除的条件为参数
    def  delete_data(self,table_name,condition):
        sql = "delete from %s where %s"%(table_name,condition)
        self.cur.execute(sql)
        self.conn.commit()

    #定义更新函数，传入表名，要更新的值，更新的条件为参数
    def update_data(self,table_name,update,condation):
        sql = "update %s set %s where %s"%(table_name,update,condation)
        self.cur.execute(sql)
        self.conn.commit()

    #关闭游标和连接
    def close(self):
        self.conn.close()
        self.cur.close()

if __name__ == '__main__':
    g = GoodsMangement()
    g.add_data("goods",0,"GB72341659","苹果","红色","水果",8,12,9,72,"2020-7-17")
    g.select_data("goodsname","goods")
    g.close()

