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


@cache_page(60 * 15)
def sitedl(request):
    # get parameters
    pDate = request.GET.get('date')
    pSite = request.GET.get('site')
    pSort = request.GET.get('sort')
    pLimit = request.GET.get('limit')

    # date string
    if pDate is None or len(pDate.strip()) == 0:
        dateObj = datetime.today() - timedelta(1)
    else:
        dateObj = datetime.strptime(pDate.strip(), '%Y-%m-%d')
    datestr = dateObj.strftime('%Y%m%d')

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
        result = ss.searchTop(datestr, pSort, limit)
    else:
        result = ss.searchSite(pSite, datestr, limit)
    showdatestr = dateObj.strftime('%Y-%m-%d')
    print pSort
    response = {'result': result, 'date': showdatestr, 'site': pSite, 'limit': limit, 'sort': pSort, 'sortlist': sortList}
    return render_to_response('show/sitedl.html', response, context_instance=RequestContext(request))
