#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====

import time
from drivers.wbeuidriver.web_driver import WebDriver

class WNBatch:
    def __init__(self):
        #获取driver
        self.driver = WebDriver.get_driver()

    def batch_page(self):
        self.driver.find_element_by_link_text('批次管理').click()
        time.sleep(2)


