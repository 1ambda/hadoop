#!/usr/bin/python

import sys
import csv


# test command:
# > cat small_forum.csv | sed 1d | python mapper.py | python header.py
def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t')
    for row in reader:
        if len(row) != 19:
            continue

        author_id = row[3]  # e.g 100005361 
        added_at  = row[8]  # e.g 2012-02-23 00:28:02.321344+00
        hour = added_at.split()[1].split(':')[0]

        print "{0}\t{1}".format(author_id, hour)


def main():
    try:
        mapper()
    except:
        pass

main()
