#!/usr/bin/env python

import sys
import collections
from operator import itemgetter
import math


class Bucket:
    def __init__(self,label, support, error):
        self.label = label
        self.support = support
        self.error = error
        self.bucket = {}

    def append(self, item):
        try:
            self.bucket[item][0] += 1
        except:
            self.bucket[item] = []
            self.bucket[item].append(1) # frequency
            self.bucket[item].append(self.label -1) # error

    def discard(self):
        # already ordered by decreasing error
        for item in self.bucket.keys():
            values = self.bucket[item]
            if values[0] + values[1] < self.support:
                del values


s = 0.01
e = s/10
started = False

# Every line
for idx, line in enumerate(sys.stdin):

    band = idx % math.ceil(1.0/e)
    # Every window
    if band == 0:
        if started:
            # switch to new bucket
            started = True

            # all entries with f+delta < label are removed
            bucket.discard()

        else:
            bucket = Bucket(band, s, e)

        bucket.append(line)
    else:
        bucket.append(line)

for item in collections.OrderedDict(sorted(bucket.bucket.items(), key=lambda x: -( x[0] + x[1] ) )):
    if item[0] + item[1] > s:
        print item
    else:
        break



