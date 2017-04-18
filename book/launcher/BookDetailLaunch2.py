# -*- coding: utf-8 -*-
from book.spider.BookDetailSpider2 import BookDetailSpider2
class BookLaunch(object):
    """
    """

    def start(self):
        self.spiderBookTag()
        pass

    def spiderBookTag(self):

        #1000001 从这里开始
        print "开启BookDetail抓取"
        BookDetailSpider2().start()


BookLaunch().start()
