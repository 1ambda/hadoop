#!/usr/bin/python

import sys
import re

regex = re.compile("(?P<host>\S+) (?P<identity>\S+) (?P<username>\S+) \[(?P<time>.+)\] \"(?P<method>.+) (?P<request>.+)"
                   " (?P<protocol>.+)\" (?P<status>[0-9]+) (?P<size>\S+)")

for line in sys.stdin:
    r = regex.search(line)
    if r is not None:
        res = r.groupdict()
        print(res[u'request'])

