# -*- coding: utf-8 -*-
from book.spider.BookListSpider import BookListSpider
from book.Constant import CHANNEL

class BookLaunch(object):
    """
    """
    def start(self):
        self.spiderBookList()
        pass

    def spiderBookList(self):
        print "开启BookList抓取"
        BookListSpider().start(CHANNEL.split())


BookLaunch().start()