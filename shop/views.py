#!/usr/bin/env python
# encoding=utf8
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse

import json
import urllib
import urllib2
import time
import commands
import md5

from service import utility


# Create your views here.
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
        for address in ('nginx01.shop.sjs', 'nginx01.shop.djt'):
            ip = commands.getoutput('host ' + address).strip().split(' ')[-1]
            print ip
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
    param = {}
    url = ''
    for key in request.POST:
        value = request.POST.get(key)
        if value is None or len(value) == 0:
            continue
        if key == 'host':
            url = 'http://' + value
        else:
            param[key] = value.encode('utf-16-le')
    hashstr = request.POST.get('queryString').encode('utf8')
    param['hash'] = md5.new(hashstr).hexdigest().decode('utf8').encode('utf-16-le')
    paramData = urllib.urlencode(param)
    req = urllib2.urlopen(url, paramData)
    result = req.read()
    return HttpResponse(result, content_type="application/xhtml+xml")
