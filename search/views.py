#!/usr/bin/env python
# encoding=utf8
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from django.utils import simplejson
from service import thrift_service

# Create your views here.


def blacklist(request):
    return render_to_response('search/blacklist.html', context_instance=RequestContext(request))


def bl_search(request):
    url = request.POST.get('url')
    url = url.strip()
    response = thrift_service.getOffsum(url)
    hitBlacklist = thrift_service.blacklist_filter(response['picurl'], response['mf'], response['picfilter1'])
    hitItem = hitBlacklist.strip().split()
    hitDesc = ''
    for it in hitItem:
        if it == 'url':
            hitDesc += '命中url黑名单 '
        elif it == 'site':
            hitDesc += '命中site黑名单 '
        elif it == 'domain':
            hitDesc += '命中domain黑名单 '
        elif it == 'mf':
            hitDesc += '命中mf黑名单 '
        elif it == 'picfilter1':
            hitDesc += '命中picfilter1黑名单 '
    if len(hitDesc) == 0:
        hitDesc = '没有命中黑名单'
    response['hit_desc'] = hitDesc
    if len(response['errinfo']) == 0:
        response['errinfo'] = '查询成功'
    return HttpResponse(simplejson.dumps(response))
