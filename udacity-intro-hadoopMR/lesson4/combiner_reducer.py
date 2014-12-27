#!/usr/bin/env python

import sys

def reducer():
    total = 0.0
    oldkey = None

    for line in sys.stdin:
        data = line.strip().split("\t")

        if len(data) != 2:
            continue

        weekday, cost = data

        if oldkey and oldkey != weekday:
            print "{0}\t{1}".format(oldkey, total)
            total = 0.0

        oldkey = weekday
        total += float(cost)

    if oldkey:
        print "{0}\t{1}".format(oldkey, total)

def main():
    reducer()

if __name__ == '__main__':
        main()
