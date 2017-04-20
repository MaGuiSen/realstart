# -*- coding: utf-8 -*-
import random
import threading

import time

from book import Global
from book.log.Log import Log
from book.spider.BookDetailSpiderThread import BookDetailSpiderThread


class ThreadInput(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        while True:
            msg = raw_input()
            msgUnicode = msg.decode('utf8')
            Global.consoleMsgIn = msgUnicode
            if msgUnicode == 'stop':
                Global.consoleToStopCatch = True
                print u'停止'


class BookDetailThreadLaunch(object):
    def __init__(self):
        self.threadList = []
        self.threadMaxSize = 10
        self.log = Log()

    def start(self):
        inputThread = ThreadInput()
        inputThread.start()

        self.spiderBookDetail()
        pass

    def spiderBookDetail(self):
        while True:
            self.checkNeedAddThread()
            while not Global.consoleToStopCatch and len(self.threadList) <= self.threadMaxSize:
                bookDetailJson = self.log.getBookDetailThreadLaunchIndex() or {}
                bookId = bookDetailJson['detailIndex'] or 4000000
                self.log.saveBookDetailThreadLaunchIndex(bookId)
                thread_ = BookDetailSpiderThread("",bookId)
                thread_.start()
                print 'add', bookId
                self.threadList.append(thread_)

    def checkNeedAddThread(self):
        for currThread in self.threadList:
            if not currThread.isAlive():
                print "dead", currThread.bookId
                self.threadList.remove(currThread)
        # 看还需要增加几个
        return self.threadMaxSize - len(self.threadList)


BookDetailThreadLaunch().start()
