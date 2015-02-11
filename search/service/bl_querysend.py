#!/usr/bin/env python
# encoding=utf8

import socket
import sys


def getHostList():
    hostlist = []
    for h in range(1, 129):
        host = 'qs%03d.pic.sjs' % (h)
        for port in (5510, 5520, 6510):
            hostlist.append((host, port))
    for h in range(1, 97):
        host = 'qs%03d.cbir.sjs' % (h)
        for port in (5511, 5512, 5513, 5514):
            hostlist.append((host, port))
    return hostlist


def forbidData(typeInput, dataInput):
    cmd = 'cmd:addblacklist\nparam:%s\nvalue:%s\n\n\n' % (typeInput, dataInput)
    return send2query(cmd)


def unforbidData(typeInput, dataInput):
    cmd = 'cmd:removeblacklist\nparam:%s\nvalue:%s\n\n\n' % (typeInput, dataInput)
    return send2query(cmd)


def send2query(cmd):
    print cmd
    successNum = 0
    for host in getHostList():
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.SOL_TCP)
            # timeval = struct.pack('ll', 1, 0)
            # socket.setsockopt(socket.SOL_SOCKET, socket.SO_SNDTIMEO, timeval)
            socket.setdefaulttimeout(1)
            sock.connect(host)
            sock.sendall(cmd)
            sock.close()
            print 'success send to query %s:%s' % (host[0], host[1])
            successNum += 1
        except socket.error, e:
            print 'fail send to query %s:%s' % (host[0], host[1])
            print str(e)
    print 'forbid count: %s' % (successNum)
    if successNum == 0:
        ret = [False, '封禁失败']
    else:
        ret = [True, '封禁成功']
    sys.stdout.flush()
    return ret


if __name__ == '__main__':
    t = 'url'
    d = 'http://t2.fansimg.com/uploads2007/10/userid136555time20071029071155.jpg'
    getHostList()
