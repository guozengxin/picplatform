#!/usr/bin/env python
# encoding=utf8

from search import settings
from blacklist import Blacklist
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol


def open(host, port):
    transport = TSocket.TSocket(host, port)
    transport = TTransport.TBufferedTransport(transport)
    protocol = TBinaryProtocol.TBinaryProtocol(transport)
    client = Blacklist.Client(protocol)
    transport.open()
    return transport, client


def close(transport):
    transport.close()


def blacklist_filter(url, mf, picfilter1):
    host, port = settings.thrift_host, settings.thrift_port
    transport, client = open(host, port)
    result = client.filter(url, mf, picfilter1)
    close(transport)
    return result


if __name__ == '__main__':
    result = blacklist_filter('http://photocdn.sohu.com/20060815/Img244809390.jpg', '0', '0')
    print result
