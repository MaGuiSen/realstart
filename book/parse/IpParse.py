# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from book.db.IPDao import IPDao
from book.util.validator import checkProxyIp_1


class IpParse(object):
    """
    """
    def __init__(self, connector):
        pass
        self.index = 0
        self.ipDao = IPDao(connector)

    def start(self, html):
        page = BeautifulSoup(html, 'lxml')
        ipItem = {}
        ipTrs = page.select('#ip_list tr')
        for ipTr in ipTrs:
            ipTds = ipTr.select('td')
            if len(ipTds) < 8:
                continue
            ipItem['ip'] = ipTds[1].get_text()
            if not ipItem['ip'] or ipItem['ip'] == u'代理IP地址':
                continue
            ipItem['port'] = ipTds[2].get_text()
            ipItem['address'] = ipTds[3].get_text()
            ipItem['ip_type'] = ipTds[5].get_text()
            if ipItem['ip_type'] != u'HTTP':
                continue
            # 验证存在是否
            is_exist = self.ipDao.checkIpExist(ipItem['ip'], ipItem['port'])
            if is_exist:
                continue
            # 验证IP
            is_useful = checkProxyIp_1(ipItem['ip'], ipItem['port'], "http://wwww.baidu.com")
            if not is_useful:
                continue
            # 存到数据库
            print "IpSpider抓取有效IP:", ipItem['ip'], ipItem['port']
            self.ipDao.save(ipItem)
        pass
