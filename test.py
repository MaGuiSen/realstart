# -*- coding: utf-8 -*-
import random

import requests
import time
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from book import Constant

dcap = dict(DesiredCapabilities.PHANTOMJS)

dcap["phantomjs.page.settings.userAgent"] = (

    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0"

)
driver = webdriver.PhantomJS(desired_capabilities=dcap)
# browser = webdriver.Firefox()
# browser.get("http://www.xdaili.cn/freeproxy.html")
# html_source = browser.page_source
# print html_source
#
driver.get("http://www.xdaili.cn/freeproxy.html")
data = driver.page_source
print data

# response = requests.get("http://www.66ip.cn/3.html",timeout=5)
# print response.text