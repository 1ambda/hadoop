#!/usr/bin/python

import sys


def reducer():

    prev = None
    count = 0

    for row in sys.stdin:
        data = row.strip().split("\t")

        if len(data) != 3:
            continue

        author_id, added_at, hour = data

        if prev and prev != hour:
            print "{0}\t{1}".format(prev, count)
            count = 0

        prev = hour
        count += 1

    if prev:
        print "{0}\t{1}".format(prev, count)


def main():
    reducer()

if __name__ == '__main__':
    main()
