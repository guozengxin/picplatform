#! /usr/bin/env python
#coding=GBK

import os
import Queue
import string
import urllib
import urllib2
from urllib2 import URLError
import httplib
import sys
import timeit
import time
import threading
import math

#�����ļ�
config = {}
configName = 'cache_presure_tool.cfg'

ifEndByTotalTime = True


#��ȡ�����ļ������������ļ��е���Ŀд��config
def loadConfig():

    try:
        configFile = open(configName, 'r')
    except IOError, e:
        print '�����ļ�%s��ʧ' % configName
        sys.exit()


    if configFile:

        try:
            configData = configFile.read()
        except IOError, e:
            print '�����ļ�%s��ȡ���ִ���' % configName


        if configData:

            ipStart = configData.find('"IP"')
            ipBegin = configData.find('=', ipStart)
            ipEnd = configData.find('\n', ipBegin+2)
            ip = configData[ipBegin+2: ipEnd-2]

            config['IP'] = ip
            
            print 'IP="%s"' % ip

            #######################################################

            httpTypeStart = configData.find('"HttpType"')
            httpTypeBegin = configData.find('=', httpTypeStart)
            httpTypeEnd = configData.find('\n', httpTypeBegin+2)
            httpType = configData[httpTypeBegin+2: httpTypeEnd-2]

            config['HttpType'] = httpType
            
            print 'HttpType="%s"' % httpType

            #######################################################

            wordListPathAll = ''

            wordListModeStart = configData.find('"WordlistMode"')
            wordListModeBegin = configData.find('=', wordListModeStart)
            wordListModeEnd = configData.find('\n', wordListModeBegin+2)
            wordListMode = configData[wordListModeBegin+2: wordListModeEnd-2]

            wordListPathStart = configData.find('"WordlistPath"')
            wordListPathBegin = configData.find('=', wordListPathStart)
            wordListPathEnd = configData.find('\n', wordListPathBegin+2)
            wordListPath = configData[wordListPathBegin+2: wordListPathEnd-2]


            if wordListMode == 'relative':
                wordListPathAll = os.getcwd() + '/' + wordListPath
            elif wordListMode == 'absolute':
                wordListPathAll = wordListPath

            config['WordlistPath'] = wordListPathAll
            
            print 'WordListMode="%s"' % wordListMode
            print 'WordListPath="%s"' % wordListPathAll

            #######################################################

            connectionNumStart = configData.find('"ConnectionNum"')
            connectionNumBegin = configData.find('=', connectionNumStart)
            connectionNumEnd = configData.find('\n', connectionNumBegin+1)
            connectionNum = configData[connectionNumBegin+1: connectionNumEnd-1]

            config['ConnectionNum'] = string.atoi(connectionNum)

            print 'ConnectionNum="%s"' % connectionNum
            
            #######################################################

            throughoutStart = configData.find('"Throughout"')
            throughoutBegin = configData.find('=', throughoutStart)
            throughoutEnd = configData.find('\n', throughoutBegin+1)
            throughout = configData[throughoutBegin+1: throughoutEnd-1]

            config['Throughout'] = string.atoi(throughout)
            
            print 'Throughout="%s"' % throughout

            #######################################################

            repeatTimeStart = configData.find('"RepeatTime"')
            repeatTimeBegin = configData.find('=', repeatTimeStart)
            repeatTimeEnd = configData.find('\n', repeatTimeBegin+1)
            repeatTime = configData[repeatTimeBegin+1: repeatTimeEnd-1]

            config['RepeatTime'] = string.atoi(repeatTime)

            print 'RepeatTime="%s"' % repeatTime

            #######################################################

            totalTimeStart = configData.find('"TotalTime"')
            totalTimeBegin = configData.find('=', totalTimeStart)
            totalTimeEnd = configData.find('\n', totalTimeBegin+1)
            totalTime = configData[totalTimeBegin+1: totalTimeEnd-1]

            config['TotalTime'] = string.atoi(totalTime)   
            
            print 'TotalTime="%s"' % totalTime

            #######################################################

            endConditionStart = configData.find('"EndCondition"')
            endConditionBegin = configData.find('=', endConditionStart)
            endConditionEnd = configData.find('\n', endConditionBegin+2)
            endCondition = configData[endConditionBegin+2: endConditionEnd-2]

            config['EndCondition'] = endCondition    
            
            print 'EndCondition="%s"' % endCondition
            
    configFile.close()


#��һ������ a=1&b=2&c=3 ���ַ����ֽ�Ϊ {a:1, b:2, c:3} �Ľṹ
def splitWord(queryLine):
    #split�������԰���&�ֽ�Ϊ['a=1', 'b=2', 'c=3']
    paramsSplit = queryLine.split('&')
    paramsDict = {}
    for split in paramsSplit:
        pos = split.find('=')
        paramKey = split[0: pos]
        paramWord = split[pos+1 : ]	

        paramsDict[paramKey] = paramWord

    return paramsDict


#�Ƿ���ֹ�������̵߳ı�־     
killAllThreads = False
#��ǰһ�������˶�����
elapsedLine = 0

#���̴߳�����
def threadHandler(th, queue, onePostTime, httpType):

    global elapsedLine

    conn = httplib.HTTPConnection(config['IP']); 
    headers = {"Content-type": "application/x-www-form-urlencoded","Connection":"Keep-Alive"}
    
    breakWhile = False

    while True:
        #thBeginTime = timeit.default_timer()
        if ifEndByTotalTime:
            #����ʱ�䣬������ֹ����
            if killAllThreads:
                break
        else:
            #���մ��������յ����̷߳�������ֹ�źţ����Ҵ�����������Ѿ�û�����ݴ��ڵ�ʱ�򣬿�����ֹ����
            if killAllThreads and queue.empty():
                break

        #������в�Ϊ�գ���������
        if not queue.empty():
            try:
                queryLine = queue.get_nowait()
            except Queue.Empty:  #Ϊ�˷�ֹ���̶߳�ȡqueue��ʱ����ɵ�if�ж�ͨ�������������Ѿ���ȡ��
                continue

            if queryLine:
                paramsDict = splitWord(queryLine)

                params = urllib.urlencode(paramsDict)
                params = params.replace('%25', '%')
                
                if httpType == 'post':

                    try:
                        conn.request('POST', "/", params, headers)
                        elapsedLine += 1
                    except Exception, e:
                        print '%d���߳� %s����ʧ�ܣ��ȴ������µ�����' % (th, config['IP'])
                        break
    
                    try:
                        response = conn.getresponse()
                        response.read()
                    except Exception, e:
                        print '%d���߳�response��ȡʧ�ܣ��ȴ������µ�����' % th
                        break

                elif httpType == 'get':
                    
                    try:
                        subUrl = queryLine
                        conn.request('GET', '/'+subUrl, '', headers)
                        elapsedLine += 1
                    except Exception, e:
                        print '%d���߳� %s����ʧ�ܣ��ȴ������µ�����' % (th, config['IP'])
                        break
                    
                    try:
                        response = conn.getresponse()
                        response.read()
                    except Exception, e:
                        print '%d���߳�response��ȡʧ�ܣ��ȴ������µ�����' % th
                        break
                
                else:
                    print 'http���ӷ�ʽ�������޸������ļ�'
                    break
                
        else:
            time.sleep(0)
                    
    conn.close()
                    

def main():

    global configName
    if len(sys.argv) == 2:
        configName = sys.argv[1]

    loadConfig()

    try:
        f = open(config['WordlistPath'], 'r')
    except IOError, e:
        print '�б��ļ���ȡ����'
        sys.exit()


    global ifEndByTotalTime
    ifEndByTotalTime = True
    if config['EndCondition'] == 'TotalTime':
        ifEndByTotalTime = True
    else:
        ifEndByTotalTime = False


    threads = []
    queue = Queue.Queue(0)
    #����ÿ�߳�ֹͣʱ��
    onePostTime = float(1) * config['ConnectionNum'] / config['Throughout']

    for th in range(config['ConnectionNum']):
        if config['HttpType'] == 'get' or config['HttpType'] == 'GET':
            thread = threading.Thread(target=threadHandler, args=(th, queue, onePostTime, 'get'))
            threads.append(thread)
        elif config['HttpType'] == 'post' or config['HttpType'] == 'POST':
            thread = threading.Thread(target=threadHandler, args=(th, queue, onePostTime, 'post'))
            threads.append(thread)
        else:
            print 'http���ӷ�ʽ�������޸������ļ�'
            sys.exit()

    for th in range(config['ConnectionNum']):
        threads[th].setDaemon(True)
        threads[th].start()


    startTime = timeit.default_timer()
    queueLinePerSec = 0
    timeLast = 0
    startRepeat = 1
    global killAllThreads
    killAllThreads = False

    if f:
        #���϶�ȡ�ļ�
        while True:
            
            if threading.activeCount() != config['ConnectionNum'] + 1:
                for th in range(config['ConnectionNum']):
                    if not threads[th].isAlive():
                        print '%d���߳����¿���' % th
                        if config['HttpType'] == 'get' or config['HttpType'] == 'GET':
                            threads[th] = threading.Thread(target=threadHandler, args=(th, queue, onePostTime, 'get'))
                        elif config['HttpType'] == 'post' or config['HttpType'] == 'POST':
                            threads[th] = threading.Thread(target=threadHandler, args=(th, queue, onePostTime, 'post'))
                        threads[th].setDaemon(True)
                        threads[th].start()

            elapsedTime = timeit.default_timer() - startTime
            if math.floor(elapsedTime) != timeLast:
                timeLast = math.floor(elapsedTime)
                queueLinePerSec = 0
            else:
                if queueLinePerSec < config['Throughout']:
                    if ifEndByTotalTime:
                        #�ﵽʱ����ֹ����
                        if elapsedTime > config['TotalTime']:
                            #���̴߳ﵽ��ֹ������������ֹ���߳��ź�
                            killAllThreads = True
                            for th in range(config['ConnectionNum']):
                                threads[th].join(1)
                            elapsedTime = timeit.default_timer() - startTime
                            print '����ʱ���ѵ�����ֹ����,������ʱ��%s�룬��ִ�з���%s��' % (elapsedTime, elapsedLine)
                            break
        
                    dataLine = f.readline().strip()
        
                    if len(dataLine):
                        queue.put(dataLine)
                        queueLinePerSec += 1
                            
                    else:
                        startRepeat += 1
                        if not ifEndByTotalTime:
                            #�ﵽ������ֹ����
                            if startRepeat > config['RepeatTime']:
                                #���̴߳ﵽ��ֹ������������ֹ���߳��ź�
                                killAllThreads = True
                                for th in range(config['ConnectionNum']):
                                    threads[th].join(1)
                                elapsedTime = timeit.default_timer() - startTime
                                print '���д����ѵ�����ֹ���У�������ʱ��%s�룬��ִ�з���%s��' % (elapsedTime, elapsedLine)
                                break
        
                        f.close()
                        #�ļ���ȡ��ĩβ�����¶�ȡ
                        try:
                            f = open(config['WordlistPath'], 'r')
                        except IOError, e:
                            print '�б��ļ���ȡ����'
                            sys.exit()    
        
                        continue


if __name__ == '__main__':
    main()
