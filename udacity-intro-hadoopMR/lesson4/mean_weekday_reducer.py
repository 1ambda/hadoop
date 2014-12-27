#!/usr/bin/python
import sys

total = 0.0
count = 0
oldkey = None
weekday = None

for line in sys.stdin:
    data = line.strip().split("\t")

    if len(data) != 2:
        continue

    weekday, cost = data

    if oldkey is not None and oldkey != weekday:
        print "weekday: {0}, mean: {1}".format(weekday, total / count)
        count = 0
        total = 0.0

    oldkey = weekday
    count += 1
    total += float(cost)

print "weekday: {0}, mean: {1}".format(weekday, total / count)
