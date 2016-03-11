#!/bin/sh

rsync -av rsync.blacklist.pic.cnc.vm::search/odin/task/pic_blacklist_gen/data/service/blacklist_inst ./data/
awk '!a[$0]++' data/blacklist_inst/blacklist_0* > data/blacklist.txt
