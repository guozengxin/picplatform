#!/usr/bin/env python
# encoding=utf8

if __name__ == '__main__':
    import sys
    sys.path.append('./')
from search import settings
from blacklist import Blacklist
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol


def init(host, port):
    port = int(port)
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
    transport, client = init(host, port)
    result = client.filter(url, mf, picfilter1)
    close(transport)
    return result


def url2Docid(url):
    host, port = settings.thrift_host, settings.thrift_port
    transport, client = init(host, port)
    docid = client.getdocid(url)
    close(transport)
    return docid


def getVal(line):
    pos = line.find(':')
    result = ''
    if pos >= 0:
        result = line[pos + 1:].strip()
    return result


def getOffsum(url):
    import os
    result = {'picurl': '', 'docid': '', 'mf': '', 'picfilter1': '', 'errinfo': ''}
    if len(url) == 66 and not url.startswith('http'):
        docid = url
    elif url.startswith('http'):
        docid = url2Docid(url)
        result['picurl'] = url
    else:
        result['errinfo'] = '输入串格式错误'
    basedir = '/search/guozengxin/task/picplatform/search/script/'
    cmd = 'cd ' + basedir + ' && ./thrift_reader ' + docid
    targetDir = os.path.join(basedir, 'data')
    cmd += ' ' + targetDir
    os.system(cmd)
    tpageFile = os.path.join(targetDir, docid + '.txt')
    print tpageFile
    if os.path.exists(tpageFile) and os.path.isfile(tpageFile):
        try:
            fp = open(tpageFile, 'r')
            next = False
            for line in fp.readlines():
                if next:
                    result['picurl'] = line.strip()
                    next = False
                    break
                elif line.startswith('mf_id:'):
                    result['mf'] = getVal(line)
                elif line.startswith('pic_filter_1:'):
                    result['picfilter1'] = getVal(line)
                elif line.startswith('T_PIC_URL_'):
                    next = True
            fp.close()
        except:
            result['errinfo'] = '读tpage文件失败'
    else:
        result['errinfo'] = '读取offsum错误'
    result['docid'] = docid
    return result


if __name__ == '__main__':
    # result = blacklist_filter('http://photocdn.sohu.com/20060815/Img244809390.jpg', '0', '0')
    # print result
    url = 'http://a1.att.hudong.com/78/14/01000000000000119081443774978.jpg'
    # print url2Docid(url)
    getOffsum(url)
