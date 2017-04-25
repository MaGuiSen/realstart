# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from book.db.IPDao import IPDao
from book.util.validator import checkProxyIp_1


class IpParse_4(object):
    """
    """
    def __init__(self, connector):
        pass
        self.index = 0
        self.ipDao = IPDao(connector)

    def start(self, html):
        page = BeautifulSoup(html, 'lxml')
        ipItem = {}
        ipTrs = page.select('#main tbody tr')
        for ipTr in ipTrs:
            ipTds = ipTr.select('td')
            ipItem['ip'] = ipTds[0].get_text()
            ipItem['port'] = ipTds[1].get_text()
            ipItem['address'] = ipTds[2].get_text()
            ipItem['ip_type'] = "http"
            if ipItem['ip'] == "ip":
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
            print "开启IpSpider_4抓取抓取有效IP:", ipItem['ip'], ipItem['port']
            self.ipDao.save(ipItem)
        pass
