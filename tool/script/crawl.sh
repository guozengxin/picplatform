#!/bin/sh

export LD_LIBRARY_PATH=lib
url=$1
echo $url > data/service/seeds.txt
./bin/sohu_spider conf/sohu_spider.conf > log/sohu_spider.log 2>&1
./bin/reader conf/reader.conf > log/reader.log 2>&1
line=`grep 'SEND PA  SUCCESS' log/reader.log | grep $url | grep -v grep`
if [ ! -z "$line" ]; then
	echo "发送成功，约10分钟会入sql表。"
else
	echo "发送失败。"
fi
