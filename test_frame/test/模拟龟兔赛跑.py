#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====

import threading
import time

def rabit():
    while 1:
        time.sleep(0.5)
        print('兔子领先')

def turtle():
    while 1:
        time.sleep(0.5)
        print('乌龟领先')

if __name__ == '__main__':
    t1=threading.Thread(target=rabit)
    t2=threading.Thread(target=turtle)
    t1.start()
    t2.start()

