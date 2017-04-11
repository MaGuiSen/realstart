# -*- coding: utf-8 -*-
import random
import requests
import time

from book import Global, Constant
from book.db.IPDao import IPDao
from book.parse.BookListParse import BookListParse
from book.ExceptionSelf import NeedNextUrl
from book.log.Log import Log


class BookListSpider(object):
    def __init__(self):
        self.needNextUrl = False
        self.ipValid = None
        self.currPage = 0
        self.ipDao = IPDao()
        self.log = Log()
        self.needChangeParams = True  # 是否需要更换参数，在服务器异常的时候不需要更换，保持原有参数
        pass

    def start(self, urls):
        # urls = ["https://book.douban.com/tag/轻小说"]
        for url in urls:
            # 重置参数
            print "重置"
            self.log.saveBookListLog({"urlBase":url})
            self.needNextUrl = False
            self.currPage = 0
            while not self.needNextUrl:
                try:
                    # 组装参数
                    urlWithParams = url + "?start={}&type=T".format(str(self.currPage * 20))
                    self.log.saveBookListLog({"urlBase": url, "urlParams": urlWithParams, "currPage": self.currPage})
                    print "新的请求+组装参数:"
                    print urlWithParams
                    self.request(urlWithParams)
                    # 请求完 +1
                    if self.needChangeParams:
                        self.currPage += 1
                    self.needChangeParams = True  # 用完记住复原
                    # 随机睡眠
                    time.sleep(int(format(random.randint(0, 9))))
                except NeedNextUrl, e:
                    print "捕获到" + e.message
                    self.needNextUrl = True
        print "抓取结束啦"

    def request(self, url):
        user_agent = random.choice(Constant.USER_AGENTS)
        response = None
        try:
            self.checkIP()
            if self.ipValid:
                proxies = {"http": "http://%s:%s" % self.ipValid, "https": "http://%s:%s" % self.ipValid}
                print proxies
                response = requests.get(url, proxies=proxies,
                                        headers={"User-Agent": user_agent},
                                        timeout=5)
                req_code = response.status_code
                req_msg = response.reason
                print "返回状态 ", req_code, " 返回状态消息 ", req_msg
                if req_code >= 400:
                    print "返回状态错误", req_code
                    self.exceptionOperate_1()
                else:
                    print "开始解析"
                    # 解析文档
                    BookListParse().start(url, response.text)
            else:
                print "没有ip了，等", "不改变参数"
                raise requests.exceptions.ProxyError("")
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
        else:
            print "请求通过"

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
            self.ipValid = IPDao().getOneIp()
            if self.ipValid:
                print "新的ip:", self.ipValid
            else:
                print "数据库中没有新的IP"


#
# book =BookListSpider()
# book.request("https://book.douban.com/tag/小说?start=760&type=T")