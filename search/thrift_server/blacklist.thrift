#!/usr/bin/thrift --gen cpp

namespace cpp blacklist

service Blacklist {
	string filter(1:string inStr, 2:string mf, 3:string picfilter1),
	string getdocid(1:string url)
}
