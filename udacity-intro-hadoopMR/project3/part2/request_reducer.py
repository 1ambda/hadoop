#!/usr/bin/python

import sys
count = 0

for line in sys.stdin:
    data = line.strip()
    if data == "/assets/js/the-associates.js":
        count += 1

print count
