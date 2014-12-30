#!/usr/bin/python

import sys
import operator

# test command:
# > cat small_forum.csv | ./map.py | sort | ./red.py
def reducer():
    prev_tag = None
    count = 0 # the number of count
    tags = {}

    for row in sys.stdin:
        data = row.strip().split("\t")

        if len(data) != 2:
            continue

        tag, unused = data

        if prev_tag and prev_tag != tag:
            tags[prev_tag] = count
            count = 0
        
        prev_tag = tag
        count += 1

    if prev_tag:
        tags[prev_tag] = count

    sorted_tags = sorted(tags.items(), key=operator.itemgetter(1), reverse=True)

    # top 10
    for i in range(10):
        k, v = sorted_tags[i]
        print "{0}\t{1}".format(k, v)

def main():
    reducer()

if __name__ == '__main__':
    main()
