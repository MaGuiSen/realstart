# -*- coding: utf-8 -*-
from threading import Timer

from book.db.IPDao import IPDao
from book.spider.IpSpider_2 import IpSpider_2
from book.spider.IpSpider import IpSpider
from book.spider.IpSpider_3 import IpSpider_3
from book.spider.IpSpider_4 import IpSpider_4
from book.spider.IpSpider_5 import IpSpider_5
from book.spider.IpSpider_6 import IpSpider_6
from book.spider.IpSpider_7 import IpSpider_7
from book.spider.IpSpider_8 import IpSpider_8



class IpLaunch(object):
    """
    """
    def start(self):
        pass
        # 没 10s 抓取一次ip
        Timer(1, self.validateIp).start()
        Timer(1, self.spiderIp).start()
        Timer(1, self.spiderIp_2).start()
        Timer(1, self.spiderIp_3).start()
        Timer(1, self.spiderIp_4).start()
        Timer(1, self.spiderIp_5).start()
        Timer(1, self.spiderIp_6).start()
        Timer(1, self.spiderIp_7).start()
        # Timer(1, self.spiderIp_8).start()

    def spiderIp(self):
        print "开启IP抓取"
        IpSpider().start()
        Timer(30, self.spiderIp).start()

    def spiderIp_2(self):
        print "开启IP2抓取"
        IpSpider_2().start()
        Timer(30, self.spiderIp_2).start()

    def spiderIp_3(self):
        print "开启IP3抓取"
        i = 0
        while i < 10:
            IpSpider_3().start("http://www.ip3366.net/?stype=1&page="+str(i))
            i += 1
        Timer(30, self.spiderIp_3).start()

    def spiderIp_4(self):
        print "开启IP4抓取"
        i = 0
        while i < 10:
            IpSpider_4().start("http://www.66ip.cn/"+str(i)+".html")
            i += 1
        Timer(30, self.spiderIp_4).start()

    def spiderIp_5(self):
        print "开启IP5抓取"
        i = 0
        while i < 2:
            IpSpider_5().start("http://www.yun-daili.com/?page=" + str(i) + "")
            i += 1
        i = 0
        while i < 10:
            IpSpider_5().start("http://www.httpsdaili.com/?page=" + str(i) + "")
            i += 1
        Timer(30, self.spiderIp_5).start()

    def spiderIp_6(self):
        print "开启IP6抓取"
        i = 0
        while i < 40:
            IpSpider_6().start("http://www.nianshao.me/?stype=1&page=" + str(i) + "")
            i += 1
        i = 0
        while i < 40:
            IpSpider_6().start("http://www.nianshao.me/?stype=2&page=" + str(i) + "")
            i += 1
        Timer(30, self.spiderIp_6).start()

    def spiderIp_7(self):
        print "开启IP7抓取"
        IpSpider_7().start("http://www.mimiip.com/")
        Timer(30, self.spiderIp_7).start()

    def spiderIp_8(self):
        print "开启IP8抓取"
        i = 0
        while i <= 10:
            IpSpider_8().start("http://www.swei360.com/?page=" + str(i))
            i += 1
        Timer(30, self.spiderIp_8).start()


    def validateIp(self):
        print "开启IP验证"
        IPDao().validateIp()
        # 睡5秒
        Timer(5, self.validateIp).start()

IpLaunch().start()