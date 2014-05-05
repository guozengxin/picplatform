#!/usr/bin/env python
# encoding=utf8
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from service import thrift_service, file_service
import json

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
    return HttpResponse(json.dumps(response))


def docid2url(request):
    return render_to_response('search/docid2url.html', context_instance=RequestContext(request))


def findSep(s):
    sep = '\r\n'
    if s.find('\r\n') >= 0:
        sep = '\r\n'
    elif s.find('\r') >= 0:
        sep = '\r'
    elif s.find('\n') >= 0:
        sep = '\n'
    return sep


def docid_trans(request):
    transType = request.POST.get('transtype')
    inputType = request.POST.get('inputtype')
    responseData = {}
    responseData['transtype'] = transType
    responseData['inputtype'] = inputType
    if transType == 'docid2url' and inputType == 'direct-input':
        oriDocid = request.POST.get('inputtext')
        sep = findSep(oriDocid)
        docidArr = oriDocid.split()
        urlArr = thrift_service.docid2url(docidArr)
        responseData['tip'] = '输入数目%d，转换成功%d' % (len(docidArr), len(urlArr))
        responseData['result'] = sep.join(urlArr)
    elif transType == 'url2docid' and inputType == 'direct-input':
        oriUrl = request.POST.get('inputtext')
        sep = findSep(oriUrl)
        urlArr = oriUrl.split()
        docidArr = thrift_service.url2Docid(urlArr)
        responseData['tip'] = '输入数目%d，转换成功%d' % (len(urlArr), len(docidArr))
        responseData['result'] = sep.join(docidArr)
    elif transType == 'docid2url' and inputType == 'file':
        if request.FILES and request.FILES.get('inputfile'):
            f = request.FILES.get('inputfile')
            docidArr = []
            for docid in f.readlines():
                docidArr.append(docid.strip())
            urlArr = thrift_service.docid2url(docidArr)
            destUrl = file_service.saveFile(urlArr, 'url')
            responseData['tip'] = '输入数目%d，转换成功%d' % (len(docidArr), len(urlArr))
            responseData['result'] = destUrl
        else:
            responseData['tip'] = '输入文件错误，请检查或者联系开发人员'
            responseData['result'] = None
    elif transType == 'url2docid' and inputType == 'file':
        if request.FILES and request.FILES.get('inputfile'):
            f = request.FILES.get('inputfile')
            urlArr = []
            for url in f.readlines():
                urlArr.append(url.strip())
            docidArr = thrift_service.url2Docid(urlArr)
            destUrl = file_service.saveFile(docidArr, 'docid')
            responseData['tip'] = '输入数目%d，转换成功%d' % (len(urlArr), len(docidArr))
            responseData['result'] = destUrl
        else:
            responseData['tip'] = '输入文件错误，请检查或者联系开发人员'
            responseData['result'] = None
    return HttpResponse(json.dumps(responseData))
