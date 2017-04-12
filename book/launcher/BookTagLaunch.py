# -*- coding: utf-8 -*-
from book.spider.BookTagSpider import BookTagSpider
from book.Constant import CHANNEL


class BookLaunch(object):
    """
    """

    def start(self):
        self.spiderBookTag()
        pass

    def spiderBookTag(self):
        print "开启BookList抓取"
        BookTagSpider().start()


BookLaunch().start()
