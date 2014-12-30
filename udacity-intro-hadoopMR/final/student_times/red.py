#!/usr/bin/python

import sys

# test command:
# > cat small_forum.csv | ./map.py | sort | ./red.py
def maxHours(hours):
    m = max(hours)
    return [h for h, x in enumerate(hours) if x == m]

def reducer():
    prev_id = None
    hours = [0] * 24

    for row in sys.stdin:
        data = row.strip().split("\t")

        if len(data) != 2:
            continue

        author_id, hour = data
        hour = int(hour)

        if prev_id and prev_id != author_id:
            for h in maxHours(hours):
                print "{0}\t{1}".format(prev_id, h)
            hours = [0] * 24

        prev_id = author_id
        hours[hour] += 1

    if prev_id:
        for i in maxHours(hours):
            print "{0}\t{1}".format(author_id, h)

def main():
    reducer()

if __name__ == '__main__':
    main()
