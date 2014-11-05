#!/usr/bin/env python
# encoding=utf8
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse

import json
import urllib
import time

from service import encoding
from service import utility

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
    webBase = 'http://www.sogou.com/web?query=%s&forceQuery=on'
    refreshBase = [
        'http://cnc.www.sogou.com.z.sogou-op.org/web?wxc=on&query=%s&forceQuery=on',
        'http://zw.www.sogou.com.z.sogou-op.org/web?wxc=on&query=%s&forceQuery=on',
        'http://sjs.www.sogou.com.z.sogou-op.org/web?wxc=on&query=%s&forceQuery=on']

    query = request.POST.get('query', None)
    query = urllib.quote(query.encode('utf-8'))
    vrurl = vrBase % (query, query)
    weburl = webBase % (query)
    refreshList = [s % (query) for s in refreshBase]

    ret = {'status': True, 'weburl': weburl, 'error': ''}
    try:
        utility.refreshUrl(vrurl)
        print 'refresh %s' % (vrurl)
        time.sleep(1)
        for url in refreshList:
            utility.refreshUrl(url)
            print 'refresh %s' % (url)
    except Exception, e:
        ret['error'] = str(e)
        ret['status'] = False
    return HttpResponse(json.dumps(ret))


def groupnews(request):
    return render_to_response('tool/groupnews.html', context_instance=RequestContext(request))
