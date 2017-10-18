# -*- coding: utf-8 -*-
import random
import threading

import time

from book import Global
from book.db.DBDao import DBDao
from book.log.Log import Log
from book.spider.TouTiaohaoRead import TouTiaohaoRead


class TouTiaoReadLaunch(object):
    def __init__(self):
        self.threadList = []
        self.threadMaxSize = 50
        self.log = Log()
        # self.connector =

    def start(self):
        thread_ = TouTiaohaoRead(DBDao().getConnector())
        thread_.start()


TouTiaoReadLaunch().start()
