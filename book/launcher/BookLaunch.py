# -*- coding: utf-8 -*-
from book.spider.BookListSpider import BookListSpider


class BookLaunch(object):
    """
    """
    def start(self):
        self.spiderBookList()
        pass

    def spiderBookList(self):
        print "开启BookList抓取"
        BookListSpider().start()


BookLaunch().start()