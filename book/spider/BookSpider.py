# -*- coding: utf-8 -*-
import random
import requests
from book import Global, Constant
from book.db.IPDao import IPDao
from book.parse.BookListParse import BookListParse
from book.ExceptionSelf import NeedNextUrl

ipValid = ''
needNextUrl = False
currPage = 0 # 一页


class BookSpider(object):
    def __init__(self):
        pass

    def start(self):
        urls = Constant.CHANNEL.split()
        for url in urls:
            while not needNextUrl:
                # 组装参数
                # TODO。。
                self.request(url)

    def request(self, url):
        user_agent = random.choice(Constant.USER_AGENTS)
        try:
            response = requests.get(url,
                                    proxies={"http": "http://%s:%s" % self.checkIP()},
                                    headers={"User-Agent": user_agent},
                                    timeout=5)
        except requests.exceptions.ConnectTimeout, e:
            print "超時"
            Global.NEED_RESET_PROXY = True
        else:
            print "请求通过"
            req_code = response.status_code
            req_msg = response.reason
            if req_code >= 400:
                print "返回状态错误"
            else:
                print "开始解析"
                # 解析文档
                try:
                    BookListParse().start(response.text)
                except NeedNextUrl, e:
                    print "next url"
                    global needNextUrl
                    needNextUrl = True

    def checkIP(self):
        global ipValid
        if Global.NEED_RESET_PROXY:
            # 从数据库取出IP
            # 先判断是否需要代理 一个字段
            Global.NEED_RESET_PROXY = False
            ipValid = IPDao().getOneIp()
        return ipValid


d = BookSpider()
print d.start()
