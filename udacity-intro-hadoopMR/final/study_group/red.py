#!/usr/bin/python

import sys

# test command:
# > cat small_forum.csv | ./map.py | sort | ./red.py
def reducer():
    prev_id = None
    students = []

    for row in sys.stdin:
        data = row.strip().split("\t")

        if len(data) != 2:
            continue

        post_id, author_id = data
        author_id = int(author_id)

        if prev_id and prev_id != post_id:
            print "{0}\t{1}".format(prev_id, students)
            students = []
        
        prev_id = post_id
        students.append(author_id)

    if prev_id:
        print "{0}\t{1}".format(prev_id, students)

def main():
    reducer()

if __name__ == '__main__':
    main()
