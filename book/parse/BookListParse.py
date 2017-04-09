# -*- coding: utf-8 -*-
from book.ExceptionSelf import NeedNextUrl


class BookListParse(object):
    """
    书籍列表解析
    """

    def __init__(self):
        pass
        self.index = 0

    def start(self, html):
        self.index += 1
        print html
        if self.index > 10:
            self.index = 0
            raise NeedNextUrl("进入下一页")
        pass
