#!/usr/bin/python

import sys

total = 0

for line in sys.stdin:
    data = line.strip().split("\t")

    if len(data) != 2:
        continue

    key, id = data

    total += 1

print "Total: ", total
