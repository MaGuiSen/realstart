# -*- coding: utf-8 -*-
import threading


class BaseSpider(threading.Thread):
    def __init__(self, bookId, connector):
        threading.Thread.__init__(self)

