#!/usr/bin/env python
# encoding=utf8

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
import json

from service import taskMonitor


# Create your views here.
def task_monitor(request):
    return render_to_response('show/task-monitor.html', context_instance=RequestContext(request))


def get_result(request):
    date = request.POST.get('date')
    rows = taskMonitor.getByDate(date)
    result = {'status': True, 'data': rows}
    return HttpResponse(json.dumps(result))
