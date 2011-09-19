#!/usr/bin/env python


import sys
import datetime


def ordinal_suffix(day):
    # stackoverflow.com/questions/739241/python-date-ordinal-output/
    if 4 <= day <= 20 or 24 <= day <= 30:
        suffix = "th"
    else:
        suffix = ["st", "nd", "rd"][day % 10 - 1]
    return suffix



def prettify(datestring):
    date = datetime.date(int(datestring[0:4]), int(datestring[5:7]), int(datestring[8:10]))
    if date == datetime.date.today():
        weekday = "Today"
    else:
        weekday = date.strftime("%A")
    return "".join((
        weekday,
        " (",
        str(date.day),
        ordinal_suffix(date.day),
        " ",
        date.strftime("%b"),
        ")",
    ))


def main():
    lastdate = ""
    for line in sys.stdin:
        date, time, rest = line.split(None, 2)
        if date != lastdate:
            print "%s:" % prettify(date)
            lastdate = date
        print "    -  ",
        if time != "##:##":
            print "(%s)" % time,
        description = rest.rstrip()
        print description


if __name__ == '__main__':
    main()


