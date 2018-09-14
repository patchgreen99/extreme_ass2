#!/usr/bin/python

import sys
import xml.etree.ElementTree as ET


for line in sys.stdin:
    line = ET.fromstring(line.strip()).attrib
    if line['PostTypeId'] == "1" and 'AcceptedAnswerId' in line.keys(): # Questions
        print "{0}.{1}".format(line['AcceptedAnswerId'],0)
    else: # Answers
        print "{0}.{1}.{2}".format(line['Id'],1,line['OwnerUserId'])