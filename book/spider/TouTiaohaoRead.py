# -*- coding: utf-8 -*-
import random
import threading
import time

import requests

from book import Constant
from book import Global
from book.db.BookCatchRecordDao import BookCatchRecordDao
from book.db.IPDao import IPDao
from book.log.Log import Log


class TouTiaohaoRead(threading.Thread):
    def __init__(self, connector):
        threading.Thread.__init__(self)
        self.needNextUrl = False
        self.ipValid = None
        self.currPage = 0
        self.ipDao = IPDao(connector)
        self.log = Log()
        self.canOverCatch = True  # 是否需要更换参数，在服务器异常的时候不需要更换，保持原有参数
        self.bookCatchRecordDao = BookCatchRecordDao(connector)
        self.connector = connector
        self.isException = False
        pass

    def run(self):
        urls = [
            'http://www.toutiao.com/i6477734526264017422/',
            'http://www.toutiao.com/i6476422082686091790/',
            'http://www.toutiao.com/i6476420572015231501/',
            'http://www.toutiao.com/i6476294333824762382/',
            'http://www.toutiao.com/i6475868700351136270/',
            'http://www.toutiao.com/i6477135834528088589/'
        ]
        while not Global.consoleToStopCatch:
            for url in urls:
                self.request(url)
                time.sleep(int(format(random.randint(5, 10))))

    def request(self, url):
        user_agent = random.choice(Constant.USER_AGENTS)
        try:
            self.checkIP()
            if self.ipValid and len(self.ipValid) >= 2:
                proxies = {"http": "http://%s:%s" % self.ipValid, "https": "http://%s:%s" % self.ipValid}
                print u">代理" + str(proxies)
                response = requests.get(url, proxies=proxies,
                                        headers={"User-Agent": user_agent},
                                        timeout=10)
                req_code = response.status_code
                req_msg = response.reason
                print u">状态:%s，消息:%s" % (str(req_code), req_msg)
                print u"> %s" % (url, )
                if req_code >= 400:
                    self.exceptionOperate_1()
                else:
                    print u">成功"
            else:
                self.ipValid = None
                raise requests.exceptions.ProxyError(u"没有IP")
        except Exception as e:
            print u">出错%s" % (str(e),)
            print url
            self.exceptionOperate_1()

    def exceptionOperate_1(self):
        """
        处理异常情况1
        :return:
        """
        if self.ipValid:
            ip, port = self.ipValid
            self.ipDao.deleteIpUnUseful(ip, port)
            self.ipValid = None

    def checkIP(self):
        self.ipValid = IPDao(self.connector).getOneIp()
        if self.ipValid and len(self.ipValid) >= 2:
            print u">新的ip:", self.ipValid
        else:
            self.ipValid = None
            print u">没有新的IP"
