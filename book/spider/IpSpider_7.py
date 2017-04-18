# -*- coding: utf-8 -*-
import random
import requests

from book import Constant
from book.parse.IpParse_7 import IpParse_7
from selenium import webdriver


class IpSpider_7(object):
    def __init__(self):
        pass

    def start(self, url):
        self.request(url)
        pass

    def request(self, url):
        user_agent = random.choice(Constant.USER_AGENTS)
        try:
            response = requests.get(url,
                                    headers={"User-Agent": user_agent},
                                    timeout=5)

            req_code = response.status_code
            if req_code >= 400:
                print "返回状态错误", req_code
            else:
                print "请求通过"
                print "开启IP7抓取 开始解析"
                # 解析文档
                IpParse_7().start(response.text)
        except requests.exceptions.ConnectTimeout, e:
            print "超時"
        except requests.exceptions.ProxyError, e:
            print "代理服务器有问题"