#!/usr/bin/python

import sys
import csv
import re


def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t')
    header = reader.next() # skip header
    print header
    for row in reader:
        if len(row) != 19:
            continue

        author_id = row[3]  # e.g 100005361 
        added_at  = row[8]  # e.g 2012-02-23 00:28:02.321344+00
        hour = added_at.split()[1].split(':')[0]
        
        print "{0}\t{1}\t{2}".format(author_id, added_at, hour)


def main():
    try:
        mapper()
    except:
        pass

main()

