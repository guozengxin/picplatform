#!/usr/bin/env python
# encoding=utf-8

import httplib
import urllib


def splitWord(queryLine):
    # split函数可以按照&分解为['a=1', 'b=2', 'c=3']
    paramsSplit = queryLine.split('&')
    paramsDict = {}
    for split in paramsSplit:
        pos = split.find('=')
        paramKey = split[0: pos]
        paramWord = split[pos + 1:]
        paramsDict[paramKey] = paramWord

    return paramsDict


def sendQueryLine(addr, queryLine):
    paramsDict = splitWord(queryLine)
    params = urllib.urlencode(paramsDict)
    params = params.replace('%25', '%')
    return sendRequest(addr, params)


def sendRequest(addr, params):
    headers = {"Content-type": "application/x-www-form-urlencoded", "Connection": "Keep-Alive"}
    conn = httplib.HTTPConnection(addr)
    print params, headers, addr
    conn.request('POST', "/", params, headers)
    response = conn.getresponse()
    result = response.read()
    return result
