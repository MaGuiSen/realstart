# -*- coding: utf-8 -*-
import os
import random
import threading
import uuid

import requests
import time
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from book import Constant

#
# dcap = dict(DesiredCapabilities.PHANTOMJS)
#
# dcap["phantomjs.page.settings.userAgent"] = (
#
#     "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0"
#
# )
# driver = webdriver.PhantomJS(desired_capabilities=dcap)
# # browser = webdriver.Firefox()
# # browser.get("http://www.xdaili.cn/freeproxy.html")
# # html_source = browser.page_source
# # print html_source
# #
# driver.get("http://www.xdaili.cn/freeproxy.html")
# data = driver.page_source
# print data

# response = requests.get("http://www.66ip.cn/3.html",timeout=5)
# print response.text

# print str(random.randint(1, 6)) + str(time.time()).replace('.','')+str(random.randint(1, 6))


# class FileDownLoadThread(threading.thread):
#     def __init__(self, book_id, path_fileName, loadUrl):
#         self.book_id = book_id
#         self.path_fileName = path_fileName
#         self.loadUrl = loadUrl
#
#     def run(self):
#         try:
#             fileResponse = requests.get(self.loadUrl)
#             if fileResponse.status_code == 200:
#                 print self.book_id, "图片下载成功", self.loadUrl
#                 open(os.path.join(os.path.dirname(__file__), self.path_fileName), 'wb').write(fileResponse.content)
#             else:
#                 print self.book_id, "图片下载出错", self.loadUrl
#         except Exception,e:
#             print self.book_id, "图片下载出错", self.loadUrl

# print len(u"""
#
#  　　""")
#
# dds = [u"目录"]
# total = 0
# for dd in dds:
#     total+=len(dd)
# print total

# fileResponse = requests.get("http://www.swei360.com/")
# print fileResponse.content

def get():
    a = 1
    b = 2
    print "ddd"
    while a < 10:
        yield a
        a += 1
        print "ccc"
    b = 1111
    print b

for z in get():
    print 11
    print z

    