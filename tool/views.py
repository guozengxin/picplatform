#!/usr/bin/env python
# encoding=utf8
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from django.utils import simplejson

from service import base64_util

# Create your views here.


def urlbase64(request):
    return render_to_response('tool/urlbase64.html', context_instance=RequestContext(request))


def base64_encode(request):
    inStr = request.POST.get('input', None)
    result = base64_util.encode(inStr)
    response = {}
    if result is not None:
        response['status'] = True
        response['info'] = '转换成功'
    else:
        response['status'] = False
        response['info'] = '转换失败'
    response['result'] = result
    return HttpResponse(simplejson.dumps(response))


def base64_decode(request):
    inStr = request.POST.get('input', None)
    result = base64_util.decode(inStr)
    response = {}
    if result is not None:
        response['status'] = True
        response['info'] = '转换成功'
    else:
        response['status'] = False
        response['info'] = '转换失败'
    response['result'] = result
    return HttpResponse(simplejson.dumps(response))
