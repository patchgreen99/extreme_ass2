#!/usr/bin/python

import sys


max_accepted = 0
max_userId = ""
max_postIds = ""

for line in sys.stdin:
    userId, postIds, accepted = line.split("=")
    accepted = int(accepted)
    if max_accepted < accepted:
        max_postIds = postIds.strip()
        max_userId = userId.strip()
        max_accepted = accepted

print "{0} -> {1}, {2}".format(max_userId, max_accepted, max_postIds)