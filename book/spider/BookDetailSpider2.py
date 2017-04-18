# -*- coding: utf-8 -*-
import random
import time

import mysql
import requests

from book import Constant
from book.db.IPDao import IPDao
from book.log.Log import Log
from book.parse.BookDetailParse import BookDetailParse
from book.util.GetIpFromXici import GetIpFromXici


class BookDetailSpider2(object):
    def __init__(self):
        self.needNextUrl = False
        self.ipValid = None
        self.currPage = 0
        self.ipDao = IPDao()
        self.log = Log()
        self.needChangeParams = True  # 是否需要更换参数，在服务器异常的时候不需要更换，保持原有参数
        self.bookDetailDao = BookDetailParse()
        self.getIpFromXici = GetIpFromXici()
        pass

    def start(self):
        detailIndexLogDict = self.log.getBookDetailIndexLog2() or {}
        index = detailIndexLogDict['detailIndex'] or 2000001
        while True:
            print "-----------------当前第", index, "条----------------------"
            if index >= 3000001:
                print "-----------------到达第", 3000001, "条----------------------"
                break
            self.log.saveBookDetailIndexLog2(index)
            url = "https://book.douban.com/subject/%s/" % (index, )
            print url
            self.request(url, index)
            time.sleep(int(format(random.randint(0, 1))))
            if self.needChangeParams:
                index += 1
            self.needChangeParams = True

    def request(self, url, book_id):
        user_agent = random.choice(Constant.USER_AGENTS)
        try:
            self.checkIP()
            if self.ipValid:
                proxies = {"http": "http://%s:%s" % self.ipValid, "https": "http://%s:%s" % self.ipValid}
                print proxies
                response = requests.get(url, proxies=proxies,
                                        headers={"User-Agent": user_agent},
                                        timeout=10)
                req_code = response.status_code
                req_msg = response.reason
                print "返回状态 ", req_code, " 返回状态消息 ", req_msg
                if req_code >= 400:
                    if req_code == 404:
                        print "没有本页资源"
                    else:
                        print "返回状态错误", req_code
                        self.exceptionOperate_1()
                else:
                    print "请求通过"
                    print "开始解析"
                    # 解析文档
                    self.bookDetailDao.start(response.text,url,book_id)
            else:
                print "没有ip了，等", "不改变参数"
                raise requests.exceptions.ProxyError("")
        except mysql.connector.errors.InterfaceError, e:
            print "数据库连接出问题", "不改变参数"
            self.exceptionOperate_1()
        except requests.exceptions.ConnectTimeout, e:
            print "服务器连接超时", "不改变参数"
            self.exceptionOperate_1()
        except requests.exceptions.ProxyError, e:
            print "代理服务器有问题", "不改变参数"
            self.exceptionOperate_1()
        except requests.exceptions.ConnectionError, e:
            print "链接出错", "不改变参数"
            self.exceptionOperate_1()
        except requests.exceptions.ReadTimeout, e:
            print "读取超时", "不改变参数"
            self.exceptionOperate_1()
        except requests.exceptions.Timeout, e:
            print "读取超时", "不改变参数"
            self.exceptionOperate_1()
        except requests.exceptions.HTTPError, e:
            print "读取超时", "不改变参数"
            self.exceptionOperate_1()

    def exceptionOperate_1(self):
        """
        处理异常情况1
        :return:
        """
        self.needChangeParams = False
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
            self.ipValid = self.getIpFromXici.getIp()
            if self.ipValid:
                print "新的ip:", self.ipValid
            else:
                print "没有新的IP"


#
# book =BookListSpider()
# book.request("https://book.douban.com/tag/小说?start=760&type=T")