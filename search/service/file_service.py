#!/usr/bin/env python
# coding=utf8

from django.conf import settings
from search import settings as search_settings
import time
import os


def saveFile(dataIn, destPrefix):
    app_name = search_settings.app_name
    t = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
    filelocation = os.path.join(app_name, destPrefix + '_' + t + '.txt')
    destFile = os.path.join(settings.MEDIA_ROOT, filelocation)
    destUrl = os.path.join(settings.MEDIA_URL, filelocation)
    fp = open(destFile, 'w')
    if not fp:
        return None
    if type(dataIn) is list:
        for it in dataIn:
            fp.write(it + '\n')
    return destUrl
