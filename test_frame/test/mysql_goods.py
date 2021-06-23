#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====

import pymysql

class Goods:
    def __init__(self):
        #与数据库建立连接
        self.conn = pymysql.connect('localhost','Komi','325320422','woniu')
        #建立游标
        self.curson = self.conn.cursor()

    #游标和数据库连接使用后需要关闭
    def close(self):
        self.curson.close()
        self.conn.close()

    #查询数据
    def select_data(self):
        #执行sql语句
        self.curson.execute('select goodsname from goods')
        #将游标中的记录拿出来
        result = self.curson.fetchall()
        print(result)
        self.close()

    #插入数据
    def insert_data(self):
        self.curson.execute('insert into goods (batch,barcode,goodsname,type,color,size,quantity,price,totalprice) '
                            'values ("GB20170923","2648374857","泡泡袖衬衣","衣服","白色","90-100","4","86","344")')
        #执行操作语言后需要向数据库提交
        self.conn.commit()
        self.close()

    #更新数据
    def update_data(self):
        self.curson.execute('update goods set color="紫色" where goodsname="泡泡袖衬衣"')
        self.conn.commit()
        self.close()

    #删除数据
    def delete_data(self):
        self.curson.execute('delete from goods where goodsname="泡泡袖衬衣"')
        self.conn.commit()
        self.close()


if __name__ == '__main__':
    mytest = Goods()
    mytest.select_data()
