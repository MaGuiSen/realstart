# -*- coding: utf-8 -*-
import json
import os
import time


class Log(object):
    """
    保存日志
    """
    def save(self,fileName, msgDict):
        with open(os.path.join(os.path.dirname(__file__) + "/file/"+fileName+".json"), "w") as f:
            timeStr = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            json.dump(dict({'time': timeStr}, **msgDict), f)

    def saveBookListLog(self, msgDict):
        """
        :param msgDict: [urlBase,urlParams,currPage]
        :return:
        """
        self.save("bookListSpider", msgDict)

    def saveBookTagPageIndex(self, pageIndex):
        self.save("bookTagPageIndex", {"pageIndex":pageIndex})

    def saveBookDetailIndexLog(self, detailIndex):
        self.save("bookDetailIndex", {"detailIndex": detailIndex})

    def getBookListLog(self):
        with open(os.path.join(os.path.dirname(__file__) + "/file/bookListSpider.json"), 'r') as load_f:
            return json.load(load_f)

    def getBookTagLog(self):
        with open(os.path.join(os.path.dirname(__file__) + "/file/bookTagPageIndex.json"), 'r') as load_f:
            return json.load(load_f)

    def getBookDetailIndexLog(self):
        with open(os.path.join(os.path.dirname(__file__) + "/file/bookDetailIndex.json"), 'r') as load_f:
            return json.load(load_f)