# -*- coding: utf-8 -*-
import os

import book.db.config.configutils as cu
from mysql.connector import MySQLConnection


class IPDao(object):
    """
    IP数据库操作
    """

    def __init__(self):
        self.configPath = os.path.join(os.path.dirname(__file__)+"/config/db_config_inner.ini")
        self.dbconfig = cu.read_db_config(self.configPath)
        self.connector = MySQLConnection(charset='utf8', **self.dbconfig)

    def getOneIp(self):
        cursor = self.connector.cursor()
        sql_query = 'select ip,port from ip_address order by id desc limit 1'
        cursor.execute(sql_query)
        results = cursor.fetchall()
        if results and len(results) > 0:
            return results[0]
        else:
            return None
