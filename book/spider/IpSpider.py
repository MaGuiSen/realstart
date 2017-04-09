# -*- coding: utf-8 -*-
import random
import requests

from book import Constant
from book.parse.IpParse import IpParse


class IpSpider(object):
    def __init__(self):
        pass

    def start(self):
        self.request("http://www.xicidaili.com/")
        pass

    def request(self, url):
        user_agent = random.choice(Constant.USER_AGENTS)
        try:
            response = requests.get(url,
                                    headers={"User-Agent": user_agent},
                                    timeout=5)
        except requests.exceptions.ConnectTimeout, e:
            print "超時"
        except requests.exceptions.ProxyError, e:
            print "代理服务器有问题"
        else:
            print "请求通过"
            if response:
                req_code = response.status_code
                if req_code >= 400:
                    print "返回状态错误"
                else:
                    print "开始解析"
                    # 解析文档
                    IpParse().start(response.text)