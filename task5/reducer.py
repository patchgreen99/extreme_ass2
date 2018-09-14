#!/usr/bin/env python

import sys
import random

resevoir = []
line_number = 0

for line in sys.stdin:
    sample, count = line.split("\t")
    line_number += int(count)
    if random.randint(0,line_number-1) < int(count) :
        resevoir = sample

print(resevoir)