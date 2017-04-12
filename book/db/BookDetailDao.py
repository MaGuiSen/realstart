# -*- coding: utf-8 -*-
import os
from mysql.connector import MySQLConnection
import book.db.config.configutils as cu
from book.util.validator import checkProxyIp_1
from book.Constant import CHANNEL_ALREADY_CATCH


class BookDetailDao(object):
    """
    IP数据库操作
    """

    def __init__(self):
        self.configPath = os.path.join(os.path.dirname(__file__) + "/config/db_config_inner.ini")
        self.dbconfig = cu.read_db_config(self.configPath)
        self.connector = MySQLConnection(charset='utf8', **self.dbconfig)

    def checkExist(self, bookId):
        cursor = self.connector.cursor()
        sql_query = 'select * from book_detail where book_id=%s'
        cursor.execute(sql_query, (bookId,))
        results = cursor.fetchall()
        cursor.close()
        if results and len(results) > 0:
            return True
        else:
            return False

    def save(self, item):
        cursor = self.connector.cursor()
        sql_query = """insert into book_detail
        (main_info,img_douban,img_self,score,mulus,tags,neirongjianjie,zuozhejianjie,congshuxinxi,source_url,book_id)
         values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

        item = (item['main_info'],
        item['img_douban'] ,
        item['img_self'],
        item['score'],
        item['mulus'] ,
        item['tags'],
        item['neirongjianjie'],
        item['zuozhejianjie'],
        item['congshuxinxi'] ,
        item['source_url'],
        item['book_id'])
        cursor.execute(sql_query, item)
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
