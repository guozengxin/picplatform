#!/usr/bin/env python
# encoding=utf-8

import MySQLdb
import time

dbName = 'taskmonitor'
host = '127.0.0.1'
user = 'web'
passwd = 'web'


def getByDate(date):
    theResult = []
    timeTuple = time.strptime(date, '%Y-%m-%d')
    timeStr1 = time.strftime('%Y-%m-%d %H:%M:%S', timeTuple)
    timeStr2 = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.mktime(timeTuple) - 86400))
    db = MySQLdb.connect(host, user, passwd, dbName)
    cursor = db.cursor()
    sqlstring = 'select taskname, starttime, endtime, is_succeed, run_info from taskinfo where starttime > %s and starttime < %s;'
    cursor.execute(sqlstring, [timeStr2, timeStr1])
    rows = cursor.fetchall()
    for r in rows:
        one = {}
        one['name'] = r[0]
        if r[1] is not None:
            one['starttime'] = time.strftime('%Y-%m-%d %H:%M:%S', r[1].timetuple())
        else:
            one['starttime'] = '-'
        if r[2] is not None:
            one['endtime'] = time.strftime('%Y-%m-%d %H:%M:%S', r[2].timetuple())
        else:
            one['endtime'] = '-'
        one['is_succeed'] = r[3]
        one['run_info'] = r[4]
        theResult.append(one)
    cursor.close()
    db.close()
    return theResult

if __name__ == '__main__':

    print getByDate('2014-07-27')
