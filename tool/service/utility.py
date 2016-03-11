#!/usr/bin/env python
# encoding=utf-8

import urllib2


def refreshUrl(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36'}
    req = urllib2.Request(url, headers=headers)
    response = urllib2.urlopen(req)
    content = response.read()
    del content
