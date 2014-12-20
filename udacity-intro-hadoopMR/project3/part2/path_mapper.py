#!/usr/bin/python

import sys
import re

regex = re.compile("(?P<host>\S+) (?P<identity>\S+) (?P<username>\S+) \[(?P<time>.+)\] \"(?P<method>.+) (?P<request>.+)"
                   " (?P<protocol>.+)\" (?P<status>[0-9]+) (?P<size>\S+)")
filter = re.compile("http://.*?(/.*)")

for line in sys.stdin:
    r = regex.search(line)
    if r is not None:
        res = r.groupdict()
        req = res[u'request']

        if req.startswith('http'):
            filtered = filter.findall(req)
            if filtered is not None and len(filtered) > 0:
                print filtered[0]
        else:
            print req


        

