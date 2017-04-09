# -*- coding: utf-8 -*-
from book.ExceptionSelf import NeedNextUrl


class BookListParse(object):
    """
    书籍列表解析
    """

    def __init__(self):
        pass

    def start(self, html):
        if True:
            raise NeedNextUrl("出错啦")
        pass

dd = BookListParse()
try:
    print dd.start("")
except NeedNextUrl,e:
    print e