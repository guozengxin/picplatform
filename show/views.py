#!/usr/bin/env python
# encoding=utf8

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from datetime import datetime
from datetime import timedelta
from django.views.decorators.cache import cache_page
import json

from service import taskMonitor
from service import sitedl as ss


# Create your views here.
def task_monitor(request):
    return render_to_response('show/task-monitor.html', context_instance=RequestContext(request))


def get_result(request):
    date = request.POST.get('date')
    rows = taskMonitor.getByDate(date)
    result = {'status': True, 'data': rows}
    return HttpResponse(json.dumps(result))

sortList = (
    ('failAll', '总异常数'),
    ('error', '失败数'),
    ('success', '成功数'),
    ('loading', '加载中数'),
    ('daolian', '盗链数'),
    ('failAllR', '总异常率'),
    ('errorR', '失败率'),
    ('successR', '成功率'),
    ('loadingR', '加载中率'),
    ('daolianR', '盗链率'),
)


def uniqueResult(result):
    uniqueKey = {}
    ret = []
    for r in result:
        key = (r['site'], r['date'])
        if key in uniqueKey:
            continue
        else:
            ret.append(r)
            uniqueKey[key] = 1
    return ret


@cache_page(60 * 15)
def sitedl(request):
    # get parameters
    startDate = request.GET.get('startdate')
    endDate = request.GET.get('enddate')
    pSite = request.GET.get('site')
    pSort = request.GET.get('sort')
    pLimit = request.GET.get('limit')

    # date string
    if startDate is None or len(startDate.strip()) == 0:
        dateObj = datetime.today() - timedelta(1)
    else:
        dateObj = datetime.strptime(startDate.strip(), '%Y-%m-%d')
    startDateStr = dateObj.strftime('%Y%m%d')
    showStartDateStr = dateObj.strftime('%Y-%m-%d')

    # date string
    if startDate is None or len(endDate.strip()) == 0:
        dateObj = datetime.today() - timedelta(1)
    else:
        dateObj = datetime.strptime(endDate.strip(), '%Y-%m-%d')
    endDateStr = dateObj.strftime('%Y%m%d')
    showEndDateStr = dateObj.strftime('%Y-%m-%d')

    # limit
    if pLimit is None or len(pLimit.strip()) == 0:
        limit = 100
    else:
        limit = len(pLimit)

    # sort
    if pSort is None or len(pSort) == 0:
        pSort = 'failAll'

    # site
    if pSite is None or len(pSite) == 0:
        result = ss.searchTop(startDateStr, endDateStr, pSort, limit)
        pSite = ''
    else:
        result = ss.searchSite(pSite, startDateStr, endDateStr, limit)
        result += ss.searchDomain(pSite, startDateStr, endDateStr, limit)
        result = uniqueResult(result)
    response = {'result': result, 'startdate': showStartDateStr, 'enddate': showEndDateStr, 'site': pSite, 'limit': limit, 'sort': pSort, 'sortlist': sortList}
    return render_to_response('show/sitedl.html', response, context_instance=RequestContext(request))
