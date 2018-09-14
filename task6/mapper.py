#!/usr/bin/env python

import sys
import random

line_number = 0
k = int(sys.argv[1])
sample = 0
resevoir = []
i = 0

for line in sys.stdin:

    # initially fill with probability of zero
    if i < k:
        resevoir.append(line)

    else:
        j = random.randint(0, i)
        if j < k:
            resevoir[j] = line

    i += 1

print resevoir

