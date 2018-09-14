#!/usr/bin/python

import sys
import heapq

file = ""
tokencount = ""
token = ""
prev_file = ""
prev_token = ""
prev_tokencount = ""
multiplefiles = 0
started = False
files_out = []

for line in sys.stdin:  # For ever line in the input from stdin
    token, file, tokencount = line.split("\t")
    file = file.strip()
    token = token.strip()
    tokencount = tokencount.strip()

    # Remember that Hadoop sorts map input by key reducer takes these keys sorted
    if prev_token == token:
        if prev_file:
            heapq.heappush(files_out, (prev_file, prev_tokencount))
    else:
        if started:
            if prev_file:
                heapq.heappush(files_out, (prev_file, prev_tokencount))

            print str(multiplefiles) + " : {" + ", ".join([r[0] + r[1] for r in heapq.nsmallest(files_out)]) + "}"
            files_out = []

        started = True

        print token+" :",

        multiplefiles = 1

    prev_token = token
    prev_file = file
    prev_tokencount = tokencount


if file == prev_file:  # Don't forget the last key/value pair
    heapq.heappush(files_out, (prev_file, prev_tokencount))
    print str(multiplefiles) + " : {" + ", ".join([r[0] + r[1] for r in heapq.nsmallest(files_out)])  + "}"
