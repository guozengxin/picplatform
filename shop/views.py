#!/usr/bin/env python
# encoding=utf8
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse

import json
import urllib
import time
import commands

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
