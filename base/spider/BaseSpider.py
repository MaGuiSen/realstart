# -*- coding: utf-8 -*-
import threading


class BaseSpider(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.needNextUrl = False
        self.ipValid = None
        self.canOverCatch = True  # 是否需要更换参数，在服务器异常的时候不需要更换，保持原有参数
        self.getIpFromXici = GetIpFromXici()
        self.bookCatchRecordDao = BookCatchRecordDao(connector)
        self.bookId = bookId
        self.isIpWayChange = False
        self.connector = connector
        self.isException = False

    def run(self):
        print 'aaaa'
