#!/usr/bin/python

import sys
import csv

# test command:
# > cat small_forum.csv | python map.py | sort | python red.py
def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t')
    for row in reader:
        if len(row) != 19:
            continue

        tags = row[2].split()
        node_type = row[5]

        if node_type == "question":
            for t in tags:
                print "{0}\t{1}".format(t, 1)

def main():
    try:
        mapper()
    except:
        pass

main()
