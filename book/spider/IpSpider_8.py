# -*- coding: utf-8 -*-
import random
import requests

from book import Constant
from book.parse.IpParse_8 import IpParse_8
from selenium import webdriver


class IpSpider_8(object):
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
                print "开启IP8抓取 开始解析"
                # 解析文档
                IpParse_8().start(response.text)
        except requests.exceptions.ConnectTimeout, e:
            print "超時"
        except requests.exceptions.ProxyError, e:
            print "代理服务器有问题"