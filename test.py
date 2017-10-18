# -*- coding: utf-8 -*-
import json
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

# driver.get("http://www.xdaili.cn/freeproxy.html")

# response = requests.get("http://tech.sina.com.cn/i/2017-06-18/doc-ifyhfnqa4408196.shtml?cre=tianyi&mod=pctech&loc=1&r=25&doct=0&rfunc=13&tj=none&s=0&tr=25", timeout=5)
# # print response.text.encode('utf8')
# # print response.encoding
# print response.text.encode('ISO-8859-1')
# params = {
#     'callback': '111202363455688951963_1497843123655',
#     'cateid': '1z',
#     'cre': 'tianyi',
#     'mod': 'pctech',
#     'merge': 3,
#     'statics': 1,
#     'length': 15,
#     'up': 1,
#     'down': 0,
#     'fields': 'media, author, labels_show, commentid, comment_count, title, url, info, thumbs, thumb, ctime, reason, vid, img_count',
#     'tm': int(time.time()),
#     'action': 1,
#     'top_id': '1Tbiz, 1Te8L, 1Tdwo, 1Teft, 1TeGe, 1TYCd, 1TXKW, 1Tbpa',
#     'offset': 0,
#     'ad': json.dumps({"rotate_count": 100, "platform": "pc", "channel": "tianyi_pctech", "page_url": "http://tech.sina.com.cn/",
#            "timestamp": 1497843123730}),
#     'ctime': int(time.time()),
#     '_': 1497839000657,
# }
# response = requests.get("http://cre.mix.sina.com.cn/api/v3/get", timeout=5, params=params)
# cookies = response.cookies
# print response.text.lstrip('jQuery111206768197617928955_1497839000641(').rstrip(')').encode('utf8')

# print json.loads(response.text.lstrip('jQuery111206768197617928955_1497839000641(').rstrip(')'))

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
#
# def get():
#     a = 1
#     b = 2
#     print "ddd"
#     while a < 10:
#         yield a
#         a += 1
#         print "ccc"
#     b = 1111
#     print b
#
# for z in get():
#     print 11
#     print z
