#!/usr/bin/env python

import sys

lastdate = ""
for line in sys.stdin:
    date, time, rest = line.split(None, 2)
    if date != lastdate:
        print date
        lastdate = date
    print "   ",
    if time != "##:##":
        print time,
    description = rest.rstrip()
    print description

