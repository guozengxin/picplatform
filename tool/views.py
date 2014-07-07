#!/usr/bin/env python
# encoding=utf8
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse

import json
import urllib2
import urllib
import time

from service import encoding

# Create your views here.


def urlbase64(request):
    return render_to_response('tool/urlbase64.html', context_instance=RequestContext(request))


def base64_encode(request):
    inStr = request.POST.get('input', None)
    result = encoding.encodeBase64(inStr)
    response = {}
    if result is not None:
        response['status'] = True
        response['info'] = '转换成功'
    else:
        response['status'] = False
        response['info'] = '转换失败'
    response['result'] = result
    return HttpResponse(json.dumps(response))


def base64_decode(request):
    inStr = request.POST.get('input', None)
    result = encoding.decodeBase64(inStr)
    response = {}
    if result is not None:
        response['status'] = True
        response['info'] = '转换成功'
    else:
        response['status'] = False
        response['info'] = '转换失败'
    response['result'] = result
    return HttpResponse(json.dumps(response))


def vr_forcequery(request):
    return render_to_response('tool/vr-forcequery.html', context_instance=RequestContext(request))


def run_force(request):
    vrBase = 'http://cnc.pic.sogou.com.z.sogou-op.org/pics/newxmlvr.jsp?rawQuery=%s&query=%s&forceQuery=on'
    webBase = 'http://www.sogou.com/web?query=%s&ie=utf8&_ast=%d&_asf=null&forceQuery=on'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36'}

    query = request.POST.get('query', None)
    query = urllib.quote(query.encode('utf-8'))
    vrurl = vrBase % (query, query)
    weburl = webBase % (query, int(time.time()))

    ret = {'status': True, 'weburl': weburl, 'error': ''}
    try:
        req = urllib2.Request(vrurl, headers=headers)
        response = urllib2.urlopen(req)
        content = response.read()
        time.sleep(1)
        del content
    except Exception, e:
        ret['error'] = str(e)
        ret['status'] = False
    print ret
    return HttpResponse(json.dumps(ret))
