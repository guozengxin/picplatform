#!/bin/sh

pid=`ps aux | grep blserver | grep -v grep | awk '{print $2}'`
echo $pid
kill -9 $pid
./blserver server.cfg > log/blserver.log 2>&1 &

