# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup

from book.ExceptionSelf import NeedNextUrl
from book.db.BookTagDao import BookTagDao


class BookTagParse(object):
    """
    书籍列表解析
    """

    def __init__(self):
        pass
        self.bookTagDao = BookTagDao()
        self.index = 0

    def start(self, html):
        document = BeautifulSoup(html, "lxml")
        subject_list = document.select("div.tags-list a")
        print len(subject_list)
        if subject_list and len(subject_list) > 0:
            for subject_item in subject_list:
                tag_name = subject_item.get_text()
                item = {}
                item['tag_name'] = tag_name
                item['already_catch'] = 0
                print tag_name
                if tag_name and "/" not in tag_name and not self.bookTagDao.checkExist(tag_name):
                    print "抓取保存的tag数据:", tag_name
                    self.bookTagDao.save(item)