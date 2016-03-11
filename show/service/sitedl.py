#!/usr/bin/env python

import MySQLdb
dbinfo = {'host': '10.11.215.156',
          'user': 'web',
          'passwd': 'web',
          'db': 'vs_pic_stats'}
table = 'sitedl'
fetchItem = ['date', 'site', 'domain', 'total', 'success', 'successR', 'error', 'errorR', 'loading', 'loadingR', 'daolian', 'daolianR', 'failAll', 'failAllR']


def newConnection():
    db = MySQLdb.connect(**dbinfo)
    cursor = db.cursor()
    return db, cursor


def delConnection(db, cursor):
    cursor.close()
    db.close()


def formatResult(rows):
    result = []
    fmtR = lambda x: '%.2f%%' % (float(x) * 100)
    for row in rows:
        item = {}
        for i in range(len(fetchItem)):
            item[fetchItem[i]] = row[i]
        item['successR'] = fmtR(item['successR'])
        item['errorR'] = fmtR(item['errorR'])
        item['loadingR'] = fmtR(item['loadingR'])
        item['daolianR'] = fmtR(item['daolianR'])
        item['failAllR'] = fmtR(item['failAllR'])
        result.append(item)
    return result


def searchTop(startDate, endDate, sortkey, limit=100):
    db, cursor = newConnection()
    if sortkey != 'total':
        sortkey = sortkey + ' desc, total desc'
    else:
        sortkey = sortkey + ' desc'
    sqlstring = 'select ' + ','.join(fetchItem) + ' from ' + table + ' where date >= \'%s\' and date <= \'%s\' order by %s limit %d;' % (startDate, endDate, sortkey, limit)
    print sqlstring
    cursor.execute(sqlstring)
    rows = cursor.fetchall()
    result = formatResult(rows)
    delConnection(db, cursor)
    return result


def searchSite(site, startDate, endDate, limit=100):
    db, cursor = newConnection()
    site = site.strip()
    sqlstring = 'select ' + ','.join(fetchItem) + ' from ' + table + ' where site = \'%s\' and date >= \'%s\' and date <= \'%s\' order by date desc limit %d;' % (site, startDate, endDate, limit)
    print sqlstring
    cursor.execute(sqlstring)
    rows = cursor.fetchall()
    return formatResult(rows)


def searchDomain(domain, startDate, endDate, limit=100):
    db, cursor = newConnection()
    domain = domain.strip()
    sqlstring = 'select ' + ','.join(fetchItem) + ' from ' + table + ' where domain = \'%s\' and date >= \'%s\' and date <= \'%s\' order by date desc limit %d;' % (domain, startDate, endDate, limit)
    print sqlstring
    cursor.execute(sqlstring)
    rows = cursor.fetchall()
    return formatResult(rows)


if __name__ == '__main__':
    result = searchTop('20141217', 'error')
    print result
