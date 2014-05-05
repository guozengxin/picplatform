#!/usr/bin/env python
# encoding=utf8

import base64


def encode(inStr):
    if inStr is not None:
        return base64.encodestring(inStr)
    else:
        return None


def decode(inStr):
    result = None
    if inStr is not None:
        try:
            result = base64.decodestring(inStr)
        except Exception:
            result = None
    return result
