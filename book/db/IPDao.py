# -*- coding: utf-8 -*-
import os
from mysql.connector import MySQLConnection
import book.db.config.configutils as cu
from book.util.validator import checkProxyIp_1


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
        cursor.close()
        if results and len(results) > 0:
            return results[0]
        else:
            return None

    def deleteIpUnUseful(self, ip, port):
        cursor = self.connector.cursor()
        sql_del = 'delete from ip_address where ip=%s and port=%s'
        cursor.execute(sql_del, (ip, port))
        self.connector.commit()
        cursor.close()
        print '删除无效的IP', ip, port

    def checkIpExist(self, ip, port):
        cursor = self.connector.cursor()
        sql_query = 'select ip,port from ip_address where ip=%s and port = %s'
        cursor.execute(sql_query,(ip, port))
        results = cursor.fetchall()
        cursor.close()
        if results and len(results) > 0:
            return True
        else:
            return False

    def save(self, item):
        cursor = self.connector.cursor()
        sql_query = 'insert into ip_address (ip,port,address,ip_type) values (%s,%s,%s,%s)'
        cursor.execute(sql_query, (item['ip'], item['port'], item['address'], item['ip_type']))
        cursor.close()
        self.connector.commit()

    def validateIp(self):
        # 从数据库中取出所有IP，正常情况下IP不多
        cursor = self.connector.cursor()
        sql_query = 'select id,ip,port from ip_address'
        cursor.execute(sql_query)
        results = cursor.fetchall()
        for id, ip, port in results:
            # 判断可用性
            is_useful = checkProxyIp_1(ip, port, 'http://wwww.baidu.com')
            if not is_useful:
                # 不可用的需要將对应ip从数据库中剔除
                sql_del = 'delete from ip_address where ip=%s and port=%s'
                cursor.execute(sql_del, (ip, port))
                self.connector.commit()
                print 'delete', ip, port
            else:
                print 'useful', ip, port
        cursor.close()