#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====

#平均响应时间 = 用户的总响应时间/线程数
#吞吐量：在以上时间内的打开页面响应后html的字节数
#吞吐率 = 吞吐量/10个线程运行的总时间

import threading,requests,time,random

tp = 0
class Test:
    def __init__(self):
        self.baseurl = 'http://172.16.8.50:8001/WoniuSales1.4/'
        self.session = requests.session()

    def openpage(self):
        openpage_response = self.session.get(self.baseurl)
        openpage_tp = len(openpage_response.text.encode())
        global tp
        tp += openpage_tp

    def login(self):
        login_url = self.baseurl + 'user/login'
        login_data = {'username':'admin','password':'Milor123','verifycode':'0000'}
        response = self.session.post(url=login_url,data=login_data)

    def start(self):
        start_time = time.time()
        self.openpage()
        time.sleep(random.randint(1,3))
        self.login()
        end_time = time.time()
        cost_time = end_time - start_time
        print(f'线程{threading.current_thread().getName()}所花费的时间为{cost_time}秒')
        print(f'线程{threading.current_thread().getName()}的吞吐量为{tp}字节')


if __name__ == '__main__':
    start_time = time.time()
    for i in range(10):
        ws = Test()
        th = threading.Thread(target=ws.start)
        th.setDaemon(True)  #守护线程，保证让10个线程先执行完
        th.start()
    th.join()
    end_time = time.time()
    count_time = end_time - start_time
    print(f'线程的总时间为：{str(count_time)}')
    print(f'平均响应时间为：{str(count_time/10)}')
    print(f'吞吐率为：{str(tp/count_time)}')
