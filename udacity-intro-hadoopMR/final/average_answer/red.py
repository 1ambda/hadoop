#!/usr/bin/python

import sys

# test command:
# > cat small_forum.csv | ./map.py | sort | ./red.py
def reducer():
    prev_id = None
    a_len = 0 # total answer len
    q_len = 0 # question len
    a_count = 0 # the number of answer 
    a_avg_len = 0

    for row in sys.stdin:
        data = row.strip().split("\t")

        if len(data) != 3:
            continue

        post_id, post_type, post_len = data
        post_len = int(post_len)

        if prev_id and prev_id != post_id:
            a_avg_len = 0 if a_count == 0 else float(a_len) / a_count
            print "{0}\t{1}\t{2}".format(prev_id, q_len, a_avg_len)
            a_len = 0
            q_len = 0
            a_count = 0
        
        prev_id = post_id
        if post_type == "q":
            q_len = post_len
        elif post_type == "a":
            a_len += post_len
            a_count += 1

    if prev_id:
        a_avg_len = 0 if a_count == 0 else float(a_len) / a_count
        print "{0}\t{1}\t{2}".format(prev_id, q_len, a_avg_len)

def main():
    reducer()

if __name__ == '__main__':
    main()
