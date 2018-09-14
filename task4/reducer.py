#!/usr/bin/python

import sys

accepted = False
postId = ""
prev_postId = ""
userId = ""

for line in sys.stdin:
    input = line.split(".")
    postId = input[0].strip()
    if len(input) > 2:
        if postId == prev_postId:
            if accepted:
                userId = input[2].strip()
                print "{0} {1}".format(userId, postId)
        else:
            accepted = False

    else:
        accepted = True

    prev_postId = postId
