# -*- coding: utf-8 -*-
import os
from mysql.connector import MySQLConnection
import book.db.config.configutils as cu
from book.util.validator import checkProxyIp_1


class BookListDao(object):
    """
    IP数据库操作
    """

    def __init__(self):
        self.configPath = os.path.join(os.path.dirname(__file__)+"/config/db_config_inner.ini")
        self.dbconfig = cu.read_db_config(self.configPath)
        self.connector = MySQLConnection(charset='utf8', **self.dbconfig)

    def checkExist(self, detail_url):
        cursor = self.connector.cursor()
        sql_query = 'select * from book_list where detail_url=%s'
        cursor.execute(sql_query,(detail_url, ))
        results = cursor.fetchall()
        cursor.close()
        if results and len(results) > 0:
            return True
        else:
            return False

    def save(self, item):
        cursor = self.connector.cursor()
        sql_query = 'insert into book_list (book_name,source_url,detail_url) values (%s,%s,%s)'
        cursor.execute(sql_query, (item['book_name'], item['source_url'], item['detail_url']))
        cursor.close()
        self.connector.commit()