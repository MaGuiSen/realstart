# -*- coding: utf-8 -*-
import requests


class GetIpFromXici(object):
    def getIp(self):
        response = requests.get("http://tvp.daxiangdaili.com/ip/?tid=555317239529077&num=1&operator=1&delay=1&filter=on&sortby=time")
        if response.status_code == 200:
            return tuple(response.content.split(":"))