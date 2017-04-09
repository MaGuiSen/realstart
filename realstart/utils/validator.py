# -*- coding: utf-8 -*-
from urllib2 import HTTPError

import requests
import telnetlib
import time


def checkProxyIp_1(ip='', port='', connect_url=''):
    """
    检测代理ip可用性 方法1
    :param ip:
    :param port:
    :param connect_url: 测试连接地址
    :return:
    """
    try:
        start_time = time.time()
        requests.get(connect_url, proxies={"http": "http://%s:%s" % (ip, port)}, timeout=5)
        back_time = time.time() - start_time
    except:
        return False
    else:
        return True


def checkProxyIp_2(ip, port):
    """
    检测代理ip可用性 方法2
    :param ip:
    :param port:
    :return:
    """
    try:
        start_time = time.time()
        telnetlib.Telnet(host=ip, port=port, timeout=10)
        back_time = time.time() - start_time
    except:
        return False
    else:
        return True


user_agent = "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)"

try:
    response = requests.get('https://book.douban.co/tag/%E5%B0%8F%E8%AF%B4?start=20&type=T', headers={"User-Agent": user_agent}, timeout=5)
except requests.exceptions.ConnectTimeout,e:
    print "超时"


# 随机user_agent

# 判断代理