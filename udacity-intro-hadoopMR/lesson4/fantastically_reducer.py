#!/usr/bin/python

import sys

xs = list()

for line in sys.stdin:
    data = line.strip().split("\t")

    if len(data) != 2:
        continue

    key, id = data

    if 'fantastically' in key:
        xs.append(int(id))

print sorted(xs)
