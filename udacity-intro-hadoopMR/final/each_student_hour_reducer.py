#!/usr/bin/python

import sys


# test command:
# > cat small_forum.csv | sed 1d | python mapper.py | python header.py
def padding(hour):
    h = str(hour)
    if len(h) == 1:
        return "0" + h
    else:
        return h


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
            mostActiveHour = hours.index(max(hours))
            print "{0}\t{1}".format(author_id, padding(mostActiveHour))
            hours = [0] * 24

        prev_id = author_id
        hours[hour] += 1

    if prev_id:
        mostActiveHour = hours.index(max(hours))
        print "{0}\t{1}".format(author_id, padding(mostActiveHour))


def main():
    reducer()

if __name__ == '__main__':
    main()
