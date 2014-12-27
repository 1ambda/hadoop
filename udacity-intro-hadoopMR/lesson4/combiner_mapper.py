#!/usr/bin/python

import sys
from datetime import datetime

def weekday(date):
    dt = datetime.strptime(date, "%Y-%m-%d")
    return dt.weekday()

def mapper():
    for line in sys.stdin:
        data = line.strip().split("\t")

        if len(data) != 6:
            continue

        date, time, store, item, cost, payment = data
        print "{0}\t{1}".format(weekday(date), cost)

def main():
    try:
        mapper()
    except:
        pass

main()
