#!/usr/bin/python

import sys

for line in sys.stdin:
    count, userid, postids = line.strip("\t")
    print "{0}->{1}".format(userid.strip(), postids.strip())
    break
