#!/usr/bin/python

import sys
import xml.etree.ElementTree as ET


for line in sys.stdin:
    line = ET.fromstring(line.strip()).attrib
    if line['PostTypeId'] == "2":
        print "{0}\t{1}".format(line['OwnerUserId'],line['Id'])
