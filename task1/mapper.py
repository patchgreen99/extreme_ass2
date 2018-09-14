#!/usr/bin/python

import sys
import os

for line in sys.stdin:
    counts = {}

    line = line.strip()
    file_name = os.environ["mapreduce_map_input_file"]
    tokens = line.split()
    for item in tokens:
        try:
            counts[item] += 1
        except:
            counts[item] = 1

    for key in counts.keys():
        print("{0}\t{1}\t{2}".format(key,os.path.basename(file_name), counts[key]))