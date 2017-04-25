# -*- coding: utf-8 -*-
import mysql

try:
    try:
        raise Exception()
    except mysql.connector.errors.InterfaceError:
        print 'aaa'
except :
    print 'dddd'