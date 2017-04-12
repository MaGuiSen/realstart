# -*- coding: utf-8 -*-
import os
from mysql.connector import MySQLConnection
import book.db.config.configutils as cu
from book.util.validator import checkProxyIp_1
from book.Constant import CHANNEL_ALREADY_CATCH


class BookTagDao(object):
    """
    IP数据库操作
    """

    def __init__(self):
        self.configPath = os.path.join(os.path.dirname(__file__) + "/config/db_config_inner.ini")
        self.dbconfig = cu.read_db_config(self.configPath)
        self.connector = MySQLConnection(charset='utf8', **self.dbconfig)

    def getPageTags(self, pageIndex, pageSize):
        cursor = self.connector.cursor()
        sql_query = 'select tag_name,already_catch from book_tag limit %s,%s'
        cursor.execute(sql_query, ((pageIndex - 1)*pageSize, pageSize))
        results = cursor.fetchall()
        cursor.close()
        if results and len(results) > 0:
            return results
        else:
            return []

    def checkExist(self, tagName):
        cursor = self.connector.cursor()
        sql_query = 'select * from book_tag where tag_name=%s'
        cursor.execute(sql_query, (tagName,))
        results = cursor.fetchall()
        cursor.close()
        if results and len(results) > 0:
            return True
        else:
            return False

    def save(self, item):
        cursor = self.connector.cursor()
        sql_query = 'insert into book_tag (tag_name,already_catch) values (%s,%s)'
        cursor.execute(sql_query, (item['tag_name'], item['already_catch']))
        cursor.close()
        self.connector.commit()

# bb = BookTagDao()
# tagUrls = CHANNEL_ALREADY_CATCH.split()
# for tagUrl in tagUrls:
#     tag = tagUrl[len('https://book.douban.com/tag/'):]
#     item = {}
#     item['tag_name'] = tag
#     item['already_catch'] = 1
#     isExist = bb.checkExist(tag)
#     if isExist:
#         continue
#     bb.save(item)
