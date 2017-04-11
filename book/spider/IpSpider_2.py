# -*- coding: utf-8 -*-
import random
import requests

from book import Constant
from book.parse.IpParse_2 import IpParse_2
from selenium import webdriver


class IpSpider_2(object):
    def __init__(self):
        pass

    def start(self):
        self.request("http://www.xdaili.cn/freeproxy.html")
        pass

    def request(self, url):
        try:
            driver = webdriver.PhantomJS()
            driver.get(url)
            page = driver.page_source
            if page:
                print "请求通过"
                print "IpSpider_2开始解析"
                # 解析文档
                IpParse_2().start(page)
            else:
                print "没有数据"
        except requests.exceptions.ConnectTimeout, e:
            print "超時"
        except requests.exceptions.ProxyError, e:
            print "代理服务器有问题"