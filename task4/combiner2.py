#!/usr/bin/python

import sys


#!/usr/bin/python

import sys

answercount = 0
postId = ""
prev_postId = ""
userId = ""
prev_userId = ""

for line in sys.stdin:
    userId, postId = line.split(" ")

    if userId == prev_userId:
        print ", " + postId.strip(),
        answercount+=1
    else:
        if prev_userId:
            print "=" + str(answercount)

        print userId.strip() + "=" + postId.strip(),
        answercount = 1


    prev_userId = userId

print "=" + str(answercount)