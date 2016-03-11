#!/usr/bin/env python
# encoding=utf8

import base64
import hashlib


def encodeBase64(inStr):
    if inStr is not None:
        return base64.encodestring(inStr)
    else:
        return None


def decodeBase64(inStr):
    result = None
    if inStr is not None:
        try:
            result = base64.decodestring(inStr)
        except Exception:
            result = None
    return result


def encodeMd5(inStr):
    md5 = hashlib.md5()
    md5.update(inStr)
    return md5.hexdigest()
