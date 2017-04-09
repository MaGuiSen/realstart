# -*- coding: utf-8 -*-
from threading import Timer

from book.db.IPDao import IPDao
from book.spider.IpSpider import IpSpider


class IpLaunch(object):
    """
    """
    def start(self):
        pass
        # 没 10s 抓取一次ip
        Timer(1, self.validateIp).start()
        Timer(1, self.spiderIp).start()

    def validateIp(self):
        print "开启IP抓取"
        IpSpider().start()
        Timer(5, self.validateIp).start()

    def spiderIp(self):
        print "开启IP验证"
        IPDao().validateIp()
        # 睡5秒
        Timer(30, self.spiderIp).start()

IpLaunch().start()