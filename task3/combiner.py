#!/usr/bin/python

import sys

prev_userId = ""
prev_postId = ""
post_count = 1
started = False

for line in sys.stdin:  # For ever line in the input from stdin
    line = line.strip()
    userId, postId = line.split("\t", 1)
    userId = userId.strip()
    postId = postId.strip()

    if prev_userId != userId:
        if started:
            print  prev_postId + "\t" + str(post_count)
        started = True

        print userId + "\t",
        post_count = 1
    else:
        print  prev_postId + ", ",
        post_count += 1


    prev_userId = userId
    prev_postId = postId

if userId == prev_userId:
    print  prev_postId + "\t" + str(post_count)
