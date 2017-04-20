# -*- coding: utf-8 -*-
import os
from mysql.connector import MySQLConnection
import book.db.config.configutils as cu
from book.util.validator import checkProxyIp_1


class BookCatchRecordDao(object):
    """
    IP数据库操作
    """

    def __init__(self):
        self.configPath = os.path.join(os.path.dirname(__file__)+"/config/db_config_inner.ini")
        self.dbconfig = cu.read_db_config(self.configPath)
        self.connector = MySQLConnection(charset='utf8', **self.dbconfig)

    def getPageTags(self, pageIndex, pageSize):
        cursor = self.connector.cursor()
        sql_query = 'select book_id,url,catch_status from book_catch_record limit %s,%s'
        cursor.execute(sql_query, ((pageIndex - 1)*pageSize, pageSize))
        results = cursor.fetchall()
        cursor.close()
        if results and len(results) > 0:
            return results
        else:
            return []

    def checkExist(self, bookId):
        cursor = self.connector.cursor()
        sql_query = 'select * from book_catch_record where book_id=%s'
        cursor.execute(sql_query, (bookId,))
        results = cursor.fetchall()
        cursor.close()
        if results and len(results) > 0:
            return True
        else:
            return False

    def save(self, item):
        cursor = self.connector.cursor()
        sql_query = 'insert into book_catch_record (book_id,url,catch_status) values (%s,%s,%s)'
        cursor.execute(sql_query, (item['book_id'], item['url'], item['catch_status']))
        cursor.close()
        self.connector.commit()

    def update(self, item):
        cursor = self.connector.cursor()
        sql_query = 'update book_catch_record set book_id=%s,url=%s,catch_status=%s'
        cursor.execute(sql_query, (item['book_id'], item['url'], item['catch_status']))
        cursor.close()
        self.connector.commit()

    def deleteById(self, bookId):
        cursor = self.connector.cursor()
        sql_del = 'delete from book_catch_record where book_id=%s'
        cursor.execute(sql_del, (bookId, ))
        self.connector.commit()
        cursor.close()
        print u'删除抓取状态的bookId:', bookId

    def deleteByUrl(self, url):
        cursor = self.connector.cursor()
        sql_del = 'delete from book_catch_record where url=%s'
        cursor.execute(sql_del, (url, ))
        self.connector.commit()
        cursor.close()
        print u'删除抓取状态的url:', url