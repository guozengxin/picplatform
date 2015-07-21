#!/usr/bin/env python
# encoding=utf8
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse

import json
import urllib
import time
import commands
import md5
import re

from service import utility
from service import cacheRequest


# Create your views here.
def index(request):
    return render_to_response('shop/index.html', context_instance=RequestContext(request))


def shopvr_forcequery(request):
    return render_to_response('shop/vr-forcequery.html', context_instance=RequestContext(request))


def run_shopvr_force(request):
    vrBase = 'http://%s/openapi?queryType=query&queryFrom=shopVr&queryString=%s&forceQuery=1'
    webBase = 'http://www.sogou.com/web?query=%s&forceQuery=on'
    refreshBase = [
        'http://cnc.www.sogou.com.z.sogou-op.org/web?wxc=on&query=%s&forceQuery=on',
        'http://zw.www.sogou.com.z.sogou-op.org/web?wxc=on&query=%s&forceQuery=on',
        'http://sjs.www.sogou.com.z.sogou-op.org/web?wxc=on&query=%s&forceQuery=on']

    query = request.POST.get('query', None)
    query = urllib.quote(query.encode('utf-8'))
    weburl = webBase % (query)
    refreshList = [s % (query) for s in refreshBase]

    ret = {'status': True, 'weburl': weburl, 'error': '', 'info': ''}
    try:
        for address in ('nginx01.shop.sjs', 'nginx01.shop.yf'):
            ip = commands.getoutput('host ' + address).strip().split(' ')[-1]
            vrurl = vrBase % (ip, query)
            utility.refreshUrl(vrurl)
            ret['info'] += '刷新 <a href="%s">%s</a> 成功<br>' % (vrurl, vrurl)
        time.sleep(2)
        for url in refreshList:
            utility.refreshUrl(url)
            ret['info'] += '刷新 <a href="%s">%s</a> 成功<br>' % (url, url)
    except Exception, e:
        ret['error'] = str(e)
        ret['status'] = False
    return HttpResponse(json.dumps(ret))


def cache(request):
    return render_to_response('shop/cache.html', context_instance=RequestContext(request))


def cachepost(request):
    sstype = request.POST.get("sstype")
    host = request.POST.get("host")
    if sstype == "queryLine":
        queryLine = request.POST.get("queryLine")
        result = cacheRequest.sendQueryLine(host, queryLine)
        return HttpResponse(result, content_type="application/xml")
    elif sstype == "queryUpdate":
        groups = ['1', '3', '5', '7', '9', '11', '13', '15', '16', '18', '20']
        param = {}
        enc = "utf-16-le"
        param["hash"] = u'12345'.encode(enc)
        param["queryType"] = u'querydataupdate'.encode(enc)
        for group in groups:
            param["update"] = group.decode('utf8').encode(enc)
            paramData = urllib.urlencode(param)
            result = cacheRequest.sendRequest(host, paramData)
        ret = {'ret': True}
        return HttpResponse(json.dumps(ret))
    else:
        param = {}
        for key in request.POST:
            value = request.POST.get(key)
            if value is None or len(value) == 0:
                continue
            if key == "sstype" or key == "host":
                continue
            param[key] = value.encode('utf-16-le')
        hashstr = request.POST.get('queryString').encode('utf8')
        param['hash'] = md5.new(hashstr).hexdigest().decode('utf8').encode('utf-16-le')
        paramData = urllib.urlencode(param)
        result = cacheRequest.sendRequest(host, paramData)
        return HttpResponse(result, content_type="application/xml")


def searchhub(request):
    return render_to_response('shop/searchhub.html', context_instance=RequestContext(request))


def strQ2B(ustring):
    """把字符串全角转半角"""
    rstring = ""
    for uchar in ustring:
        inside_code = ord(uchar)
        if inside_code == 0x3000:
            inside_code = 0x0020
        else:
            inside_code -= 0xfee0
        if inside_code < 0x0020 or inside_code > 0x7e:      # 转完之后不是半角字符返回原来的字符
            rstring += uchar
        rstring += unichr(inside_code)
    return rstring


def searchhubpost(request):
    host = request.POST.get("host")
    param = {}
    for key in request.POST:
        value = request.POST.get(key)
        if value is None or len(value) == 0:
            continue
        if key == "host":
            continue
        param[key] = value.encode('gbk')
    paramData = urllib.urlencode(param)
    result = cacheRequest.sendRequest(host, paramData)
    result = result.decode('utf-16-le')
    result = result.encode('gb18030')
    result = '<?xml version="1.0" encoding="gb18030"?>\n' + result
    result = re.sub('</DOCUMENT>.*', '</DOCUMENT>', result)
    return HttpResponse(result, content_type="application/xml")


def query(request):
    return render_to_response('shop/query.html', context_instance=RequestContext(request))


def querypost(request):
    host = request.POST.get("host")
    param = {}
    for key in request.POST:
        value = request.POST.get(key)
        if value is None or len(value) == 0:
            continue
        if key == "host":
            continue
        param[key] = value.encode('utf-16-le')
    hashstr = request.POST.get('queryString').encode('utf8')
    param['hash'] = md5.new(hashstr).hexdigest().decode('utf8').encode('utf-16-le')
    paramData = urllib.urlencode(param)
    result = cacheRequest.sendRequest(host, paramData)
    return HttpResponse(result, content_type="application/xml")


def sqo(request):
    return render_to_response('shop/sqo.html', context_instance=RequestContext(request))


def sqopost(request):
    host = request.POST.get("host")
    param = {}
    for key in request.POST:
        value = request.POST.get(key)
        if value is None or len(value) == 0:
            continue
        if key == "host":
            continue
        param[key] = value.encode('utf-16-le')
    paramData = urllib.urlencode(param)
    result = cacheRequest.sendRequest(host, paramData)
    return HttpResponse(result, content_type="application/xml")
