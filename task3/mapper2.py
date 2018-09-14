#!/usr/bin/python

import sys

for line in sys.stdin:
    userId, postIds, count = line.split("\t")
    print "{0}\t{1}->{2}".format(count.strip(), userId.strip(), postIds.strip())
