#!/bin/sh

mkdir -p log/

python manage.py runserver 0.0.0.0:9999 > log/runserver.log 2>&1 &
