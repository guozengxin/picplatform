#!/bin/sh

pid=`ps aux | grep "python manage.py runserver" | grep -v grep | awk '{print $2}'`
kill $pid
sleep 1s

pid=`ps aux | grep "python manage.py runserver" | grep -v grep | awk '{print $2}'`
if [ ! -z $pid ]; then
	kill -9 $pid
fi
