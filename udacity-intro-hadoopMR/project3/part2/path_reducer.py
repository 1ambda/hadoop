#!/usr/bin/python

import sys
count = 0
current = None

mostPopularPath = None
mostPopularCount = 0

for line in sys.stdin:
    next = line.strip()

    if current is not None and next != current:
        if count > mostPopularCount:
            mostPopularCount = count
            mostPopularPath = current
      
        current = next
        count = 0

    current = next
    count += 1 

if mostPopularPath is not None:
    print "most popular:", mostPopularPath, mostPopularCount
