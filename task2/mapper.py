#!/usr/bin/python

import sys
import heapq
import xml.etree.ElementTree as ET

h = []
counter = 0

for line in sys.stdin:
    line = ET.fromstring(line.strip()).attrib

    if line["PostTypeId"] == "1":
        count = int(line["ViewCount"])

        if counter < 10:
            heapq.heappush(h, (count, line["Id"]))
            counter += 1

        elif heapq.nsmallest(1, h)[0][0] < count:
            heapq.heappushpop(h, (count, line["Id"]))

for frequency,sequence in h:
    print ("{0} {1}".format(frequency,sequence))
