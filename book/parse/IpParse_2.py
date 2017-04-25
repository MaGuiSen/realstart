# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from book.db.IPDao import IPDao
from book.util.validator import checkProxyIp_1


class IpParse_2(object):
    """
    """
    def __init__(self, connector):
        pass
        self.index = 0
        self.ipDao = IPDao(connector)

    def start(self, html):
        page = BeautifulSoup(html, 'lxml')
        ipItem = {}
        ipTrs = page.select('tbody#target tr')
        print len(ipTrs)
        for ipTr in ipTrs:
            ipTds = ipTr.select('td')
            ipItem['ip'] = ipTds[0].get_text()
            ipItem['port'] = ipTds[1].get_text()
            ipItem['address'] = ipTds[5].get_text()
            ipItem['ip_type'] = ipTds[3].get_text()
            # 验证存在是否
            is_exist = self.ipDao.checkIpExist(ipItem['ip'], ipItem['port'])
            if is_exist:
                continue
            # 验证IP
            is_useful = checkProxyIp_1(ipItem['ip'], ipItem['port'], "http://wwww.baidu.com")
            if not is_useful:
                continue
            # 存到数据库
            print "IpSpider_2抓取有效IP:", ipItem['ip'], ipItem['port']
            self.ipDao.save(ipItem)
        pass
