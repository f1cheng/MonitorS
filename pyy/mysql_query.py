#!/usr/bin/env python

#coding=utf-8

import sys
import os
import commands

class QpsTps(object):
    def __init__(self):
        self.QPS = ''
        self.TPS = ''
    def getQps(self):
        (Queries,QPS_result) = commands.getstatusoutput("mysqladmin -uzabbix -pzabbix extended-status | grep 'Queries' | cut -d'|' -f3")
        self.QPS = int(QPS_result)
        return self.QPS
    def getTps(self):
        (Com_commit,cm_result) = commands.getstatusoutput("mysqladmin -uzabbix -pzabbix extended-status | grep 'Com_commit' | cut -d'|' -f3 ")
        (Com_rollback,rb_result) = commands.getstatusoutput("mysqladmin -uzabbix -pzabbix extended-status | grep 'Com_rollback' | cut -d'|' -f3 | awk 'NR==1'")
        self.TPS = int(cm_result) + int(rb_result)
        return self.TPS

class error_out(object):
    def error_print(self):
        print
        print 'Usage : ' + sys.argv[0] + ' MysqlStatusKey '
        print
        sys.exit(1)

class Main(object):
    def main(self):
        if len(sys.argv) == 1:
            error = error_out()
            error.error_print()
        elif sys.argv[1] == 'QPS':
            a = QpsTps()
            print a.getQps()
        elif sys.argv[1] == 'TPS':
            a = QpsTps()
            print a.getTps()

if __name__ == '__main__':
    main_obj = Main()
    main_obj.main()
