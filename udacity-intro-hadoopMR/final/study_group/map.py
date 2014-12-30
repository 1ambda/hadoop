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

        node_type = row[5]
        author_id = row[3]
        id = None

        if node_type == "question":
            id = row[0] # post_id
            print "{0}\t{1}".format(id, author_id)
        elif node_type == "answer" or node_type == "comment":
            id = row[6] # parent_id
            print "{0}\t{1}".format(id, author_id)

def main():
    try:
        mapper()
    except:
        pass

main()
