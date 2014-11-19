#!/usr/bin/env python
# encoding=utf-8

import MySQLdb
dbinfo = {'host': 'mysql01.sae.djt',
          'user': 'chanpinyunying',
          'passwd': 'm6i1m2a3',
          'db': 'pic_tiny'}


def isurl(query):
    if query.startswith('http://') or query.startswith('https://'):
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
    else:
        result.update(searchKeyword(query, db))
    return result


def searchUrl(url, db):
    # 把URL当做pageurl查询数据
    result = {}
    pageResult = searchPageurl(url, db)
    if len(pageResult['pics']) > 0:
        result[url] = pageResult

    # 把URL当做picurl查询数据
    cur = db.cursor()
    sqlstring = 'select distinct page_url from pic_news_image where ori_pic_src = %s'
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


def searchKeyword(query, db):
    cur = db.cursor()
    cur.execute('set names gbk')
    result = {}
    sqlstring = 'select distinct page_url from pic_news_image where page_title like %s'
    print query.encode('gbk')
    cur.execute(sqlstring, [('%' + query + '%').encode('gbk')])
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
    return s.decode('gbk').encode('utf8')


def searchPageurl(pageurl, db):
    cur = db.cursor()
    cur.execute('set names gbk')
    sqlstring = 'select page_url, page_title, ori_pic_src, deleted, category, pic_title, img_desc, group_mark from pic_news_image where page_url = %s order by group_index'
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
        info['pics'].append(picinfo)
    if len(info['pics']) > 0:
        iObj = info['pics'][0]
        print iObj
        info['title'] = iObj['title']
        info['picurl'] = iObj['picurl']
        info['deleted'] = iObj['deleted']
        info['category'] = iObj['category']
    cur.close()
    return info
