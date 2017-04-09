# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup

from book.ExceptionSelf import NeedNextUrl
from book.db.BookListDao import BookListDao

class BookListParse(object):
    """
    书籍列表解析
    """

    def __init__(self):
        pass
        self.bookListDao = BookListDao()
        self.index = 0

    def start(self, source_url, html):
        document = BeautifulSoup(html, "lxml")
        subject_list = document.select("ul.subject-list li.subject-item")
        if subject_list and len(subject_list) > 0:
            for subject_item in subject_list:
                book_name = ""
                detail_url = ""
                a_items = subject_item.select("div.info h2 a")
                if a_items and len(a_items) > 0:
                    a_item = a_items[0]
                    detail_url = a_item.get("href")
                    book_name = a_item.get("title")
                item = {}
                item['book_name'] = book_name.replace(u" ", "")
                item['detail_url'] = detail_url
                item['source_url'] = source_url
                if detail_url and not self.bookListDao.checkExist(detail_url):
                    print "抓取保存的数据:", book_name, detail_url
                    self.bookListDao.save(item)
        else:
            raise NeedNextUrl("进入下一页")
