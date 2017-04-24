# -*- coding: utf-8 -*-
import random
import threading
import time

import mysql
import requests

from book import Constant
from book import Global
from book.db.BookCatchRecordDao import BookCatchRecordDao
from book.db.IPDao import IPDao
from book.log.Log import Log
from book.parse.BookDetailParse import BookDetailParse
from book.util.GetIpFromXici import GetIpFromXici


class BookDetailSpiderThread(threading.Thread):
    def __init__(self, bookId):
        threading.Thread.__init__(self)
        self.needNextUrl = False
        self.ipValid = None
        self.currPage = 0
        self.ipDao = IPDao()
        self.log = Log()
        self.canOverCatch = True  # 是否需要更换参数，在服务器异常的时候不需要更换，保持原有参数
        self.bookDetailDao = BookDetailParse()
        self.getIpFromXici = GetIpFromXici()
        self.bookCatchRecordDao = BookCatchRecordDao()
        self.bookId = bookId
        self.isIpWayChange = False;
        pass

    def run(self):
        while not Global.consoleToStopCatch:
            # 记录抓第几条
            url = "https://book.douban.com/subject/%s/" % (self.bookId,)
            catchRecordItem = {
                'book_id': self.bookId,
                'url': url,
                'catch_status': 'catching',
            }
            print str(self.bookId) + ">" + url
            if not self.bookCatchRecordDao.checkExist(self.bookId):
                self.bookCatchRecordDao.save(catchRecordItem)
            self.request(url, self.bookId)
            time.sleep(int(format(random.randint(0, 1))))
            if self.canOverCatch:
                # 说明成功了，就需要跳出
                # 删除数据库 记录
                self.bookCatchRecordDao.deleteById(self.bookId)
                break
            self.canOverCatch = True
        print "success>" + str(self.bookId) + ">" + url

    def request(self, url, book_id):
        user_agent = random.choice(Constant.USER_AGENTS)
        try:
            self.checkIP()
            if self.ipValid and len(self.ipValid) >= 2:
                proxies = {"http": "http://%s:%s" % self.ipValid, "https": "http://%s:%s" % self.ipValid}
                print str(book_id) + u">代理" + str(proxies)
                response = requests.get(url, proxies=proxies,
                                        headers={"User-Agent": user_agent},
                                        timeout=10)
                req_code = response.status_code
                req_msg = response.reason
                if req_code >= 400:
                    if req_code == 404:
                        print str(book_id) + ">" + u"状态:" + str(req_code) + "," + u"消息:" + req_msg + "," + u"没有本页资源"
                        print
                    else:
                        print str(book_id) + ">" + u"状态:" + str(req_code) + "," + u"消息:" + req_msg + "," + u"返回状态错误"
                        self.exceptionOperate_1()
                else:
                    print str(book_id) + ">" + u"状态:" + str(req_code) + "," + u"消息:" + req_msg + "," + u"开始解析"
                    # 解析文档
                    self.bookDetailDao.start(response.text, url, book_id)
            else:
                print str(book_id) + u">消息:没有ip了,不改变参数",""
                self.ipValid = None;
                raise requests.exceptions.ProxyError("")
        except mysql.connector.errors.InterfaceError, e:
            print str(book_id) + ">" + u"消息:数据库连接出问题,不改变参数"
            self.exceptionOperate_1()
        except requests.exceptions.ConnectTimeout, e:
            print str(book_id) + ">" + u"消息:服务器连接超时,不改变参数"
            self.exceptionOperate_1()
        except requests.exceptions.ProxyError, e:
            print str(book_id) + ">" + u"消息:代理服务器有问题,不改变参数"
            self.exceptionOperate_1()
        except requests.exceptions.ConnectionError, e:
            print str(book_id) + ">" + u"消息:链接出错,不改变参数"
            self.exceptionOperate_1()
        except requests.exceptions.ReadTimeout, e:
            print str(book_id) + ">" + u"消息:读取超时,不改变参数"
            self.exceptionOperate_1()
        except requests.exceptions.Timeout, e:
            print str(book_id) + ">" + u"消息:读取超时,不改变参数"
            self.exceptionOperate_1()
        except requests.exceptions.HTTPError, e:
            print str(book_id) + ">" + u"消息:读取超时,不改变参数"
            self.exceptionOperate_1()

    def exceptionOperate_1(self):
        """
        处理异常情况1
        :return:
        """
        self.canOverCatch = False
        if self.ipValid:
            ip, port = self.ipValid
            self.ipDao.deleteIpUnUseful(ip, port)
            self.ipValid = None

    def checkIP(self):
        if not self.ipValid:
            # 从数据库取出IP
            # 先判断是否需要代理 一个字段
            # TODO 这里的IpDao使用对象的形式，不懂为什么会出现缓存问题，就是一直select都是空数组
            # self.ipValid = IPDao().getOneIp()
            # if self.ipValid:
            #     print "新的ip:", self.ipValid
            # else:
            #     print "数据库中没有新的IP"
            if self.isIpWayChange:
                self.isIpWayChange = False;
                self.ipValid = self.getIpFromXici.getIp()
            else:
                self.isIpWayChange = True;
                self.ipValid = IPDao().getOneIp()

            if self.ipValid and len(self.ipValid) >= 2:
                print str(self.bookId) + u">新的ip:", self.ipValid
            else:
                self.ipValid = None
                print str(self.bookId) + u">没有新的IP"
