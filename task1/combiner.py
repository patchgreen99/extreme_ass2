#!/usr/bin/python

import sys

prev_file = ""
file = ""
prev_token = ""
token = ""
identicalfile = 0
multiplefiles = 0
started = False

for line in sys.stdin:  # For ever line in the input from stdin
    token, file, count = line.split("\t")
    file = file.strip()
    token = token.strip()
    count = int(count.strip())

    # Remember that Hadoop sorts map input by key reducer takes these keys sorted
    if prev_token == token:
        if file == prev_file:
            identicalfile += 1
        else:
            if prev_file:
                print  prev_file + "\t" + str(identicalfile),
                identicalfile = count

    else:
        if started:
            if prev_file:
                print prev_file + "\t" + str(identicalfile)
        started = True

        print token.strip() + "\t",

        identicalfile = count

    prev_token = token
    prev_file = file


if file == prev_file:  # Don't forget the last key/value pair
    print prev_file + "\t" + str(identicalfile)

