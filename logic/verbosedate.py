#!/usr/bin/env python

"""
Converts the custom "verbosedate" format into up1 format.
"""

import sys
import datetime


def parselines(linesource):
    for line in linesource:
        if "|" not in line:
            continue
        note = {}
        keepchomping = True
        while keepchomping:
            atom, line = line.split(None, 1)
            if atom == "|":
                note["note"] = line.rstrip()
                keepchomping = False
            else:
                key, kaboom, value = atom.partition("=")
                note[key] = value
        yield note


def match(date, notes):
    for note in notes:
        lookahead = int(note['lookahead']) if ('lookahead' in note) else 0
        dates = (date + datetime.timedelta(d) for d in range(lookahead + 1))
        for d in dates:
            if matches(d, note):
                newnote = dict(note)
                newnote['_matchdate'] = d.isoformat()
                newnote['_matchtime'] = gettime(note)
                yield newnote


def matches(date, note):
    restricted = False
    if 'isodate' in note:
        if date.isoformat() != note['isodate']:
            restricted = True
    if 'weekday' in note:
       if (date.isoweekday() % 7) != int(note['weekday']):
            restricted = True
    return not restricted


def gettime(note):
    if 'isotime' in note:
        return note['isotime']
    return "##:##"


def render(notes):
    for note in notes:
        print " ".join((
            note['_matchdate'],
            note['_matchtime'],
            note['note'],
        ))


def main():
    linesource = sys.stdin
    allnotes = parselines(linesource)
    today = datetime.date.today()
    matching = match(today, allnotes)
    render(matching)


if __name__== '__main__':
    main()

