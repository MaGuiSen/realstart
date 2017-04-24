# -*- coding: utf-8 -*-
import os

from mysql.connector import MySQLConnection

import book.db.config.configutils as cu


class DBDao(object):
    """
    IP数据库操作
    """
    def __init__(self):
        self.configPath = os.path.join(os.path.dirname(__file__)+"/config/db_config_inner.ini")
        self.dbconfig = cu.read_db_config(self.configPath)
        self.connector = MySQLConnection(charset='utf8', **self.dbconfig)

    def getConnector(self):
        return self.connector