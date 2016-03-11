#!/usr/bin/env python
# encoding=utf-8

import MySQLdb
import re
dbinfo = {'host': 'pic01.ss.mysql.db.sogou-op.org',
          'user': 'chanpinyunying',
          'passwd': 'm6i1m2a3',
          'db': 'pic_tiny'}

table = 'pic_news_image'


def isurl(query):
    if query.startswith('http://') or query.startswith('https://'):
        return True
    else:
        return False


def isUint64(query):
    if re.match(r'[0-9a-fA-F]', query) and len(query) == 16:
        return True
    else:
        return False


def substrUTF8(s, length):
    if length > len(s):
        return s
    i = 0
    p = 0

    while True:
        ch = ord(s[i])
        # 1111110x
        if ch >= 252:
            p = p + 6
        # 111110xx
        elif ch >= 248:
            p = p + 5
        # 11110xxx
        elif ch >= 240:
            p = p + 4
        # 1110xxxx
        elif ch >= 224:
            p = p + 3
        # 110xxxxx
        elif ch >= 192:
            p = p + 2
        else:
            p = p + 1

        if p >= length:
            break
        else:
            i = p
    return s[0:i]


def groupnewsSearch(query):
    db = MySQLdb.connect(**dbinfo)
    result = {}
    if isurl(query):
        result.update(searchUrl(query, db))
    elif isUint64(query):
        result.update(searchMulti(query, db, 'group_mark'))
        result.update(searchMulti(query, db, 'img_hash'))
    else:
        result.update(searchMulti(query, db, 'page_title'))
    return result


def searchUrl(url, db):
    # 把URL当做pageurl查询数据
    result = {}
    pageResult = searchPageurl(url, db)
    if len(pageResult['pics']) > 0:
        result[url] = pageResult

    # 把URL当做picurl查询数据
    cur = db.cursor()
    sqlstring = 'select distinct page_url from ' + table + ' where ori_pic_src = %s'
    cur.execute(sqlstring, [url])
    rows = cur.fetchall()
    for r in rows:
        pageurl = r[0]
        if pageurl in result:
            continue
        pageResult = searchPageurl(pageurl, db)
        if len(pageResult['pics']) > 0:
            result[pageurl] = pageResult
    return result


def searchMulti(query, db, flag):
    cur = db.cursor()
    cur.execute('set names gbk')
    result = {}
    if flag == 'page_title':
        sqlstring = 'select distinct page_url from ' + table + ' where page_title like \'%s\'' % (('%' + query + '%').encode('gbk'))
    elif flag == 'group_mark':
        sqlstring = 'select distinct page_url from ' + table + ' where group_mark = \'%s\'' % (query)
    elif flag == 'img_hash':
        sqlstring = 'select distinct page_url from ' + table + ' where img_hash = \'%s\'' % (query)
    else:
        return result

    cur.execute(sqlstring)
    rows = cur.fetchall()
    for r in rows:
        pageurl = r[0]
        if pageurl in result:
            continue
        pageResult = searchPageurl(pageurl, db)
        if len(pageResult['pics']) > 0:
            result[pageurl] = pageResult
    return result


def gbk2utf8(s):
    return s.decode('gb18030').encode('utf8')


def searchPageurl(pageurl, db):
    cur = db.cursor()
    cur.execute('set names gbk')
    sqlstring = 'select page_url, page_title, ori_pic_src, deleted, category, pic_title, img_desc, group_mark, img_hash, title_id from ' + table + ' where page_url = %s order by group_index'
    cur.execute(sqlstring, [pageurl])
    rows = cur.fetchall()
    info = {}
    info['pageurl'] = pageurl
    info['pics'] = []
    for r in rows:
        picinfo = {}
        picinfo['title'] = gbk2utf8(r[1])
        picinfo['picurl'] = r[2]
        picinfo['deleted'] = r[3]
        picinfo['category'] = gbk2utf8(r[4])
        picinfo['pic_title'] = substrUTF8(gbk2utf8(r[5]), 10)
        picinfo['img_desc'] = substrUTF8(gbk2utf8(r[6]), 30)
        picinfo['group_mark'] = r[7]
        picinfo['img_hash'] = r[8]
        picinfo['title_id'] = gbk2utf8(r[9])
        info['pics'].append(picinfo)
    if len(info['pics']) > 0:
        iObj = info['pics'][0]
        info['title'] = iObj['title']
        info['picurl'] = iObj['picurl']
        info['deleted'] = iObj['deleted']
        info['category'] = iObj['category']
        info['group_mark'] = iObj['group_mark']
    cur.close()
    return info


def operatePageurl(pageurl, op):
    db = MySQLdb.connect(**dbinfo)
    cur = db.cursor()
    cur.execute('set names gbk;')
    deleted = 0
    if op == 'delete':
        deleted = 1
    elif op == 'recover':
        deleted = 0
    else:
        return False
    sqlstring = 'update ' + table + ' set deleted = %s where page_url = %s;'
    ret = cur.execute(sqlstring, [str(deleted), pageurl])
    if ret > 0:
        return True
    else:
        return False
