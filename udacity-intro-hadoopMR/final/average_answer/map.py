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

        post_id = row[0]
        node_type = row[5] # "question" or "answer"
        body = row[4]

        if node_type == "question":
            print "{0}\t{1}\t{2}".format(post_id, "q", len(body))
        elif node_type == "answer":
            parent_id = row[6]
            print "{0}\t{1}\t{2}".format(parent_id, "a", len(body))

def main():
    try:
        mapper()
    except:
        pass

main()
