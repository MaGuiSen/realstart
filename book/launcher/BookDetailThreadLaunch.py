# -*- coding: utf-8 -*-
import random
import threading

import time

from book.spider.BookDetailSpiderThread import BookDetailSpiderThread

stopCatch = False;


class ThreadMy(threading.Thread):
    def __init__(self, book_id):
        threading.Thread.__init__(self)
        self.book_id = book_id

    def run(self):
        # print u"开始book_id:",self.book_id
        time.sleep(random.randint(1, 2))
        # print u"结束book_id:",self.book_id


class ThreadInput(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        while True:
            msg = raw_input()
            msgUnicode = msg.decode('utf8')
            if msgUnicode == 'stop':
                global stopCatch
                stopCatch = True
                print u'停止'


class BookLaunch(object):
    def __init__(self):
        self.threadList = []
        self.threadMaxSize = 10

    def start(self):
        inputThread = ThreadInput()
        inputThread.start()

        self.spiderBookDetail()
        pass

    def spiderBookDetail(self):
        book_id = 0
        while True:
            self.checkNeedAddThread()
            while not stopCatch and len(self.threadList) <= self.threadMaxSize:
                book_id += 1
                thread_ = ThreadMy(book_id)
                thread_.start()
                print 'add', book_id
                self.threadList.append(thread_)
        pass

    def checkNeedAddThread(self):
        for currThread in self.threadList:
            if not currThread.isAlive():
                print "dead", currThread.book_id
                self.threadList.remove(currThread)
        # 看还需要增加几个
        return self.threadMaxSize - len(self.threadList)


BookLaunch().start()
a = [12, 22, 33]
for i in a:
    print i
a.remove(22)
print len(a)
