#!/usr/bin/python

import sys

fin_postCount = 0
fin_userId = ""
fin_postIds = ""

for line in sys.stdin:
    userId, postIds = line.split(" ")
    print "{0} {1}".format(userId.strip(), postIds.strip())