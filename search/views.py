#!/usr/bin/env python
# encoding=utf8
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from django.utils import simplejson

# Create your views here.


def blacklist(request):
    return render_to_response('search/blacklist.html', context_instance=RequestContext(request))
