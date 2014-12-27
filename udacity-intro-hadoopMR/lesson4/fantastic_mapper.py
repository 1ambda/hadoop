#!/usr/bin/python

import sys
import re
import csv

# SO: python-split-string-with-multiple-delimiters
delimiters = tuple('.,!?:;"()<>[]#$=-/')
pattern = '|'.join(map(re.escape, delimiters))

def split(line):
    return re.split(pattern, line)

# mapper
def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t')
    rgxWord = re.compile(r"fantastic\S*")

    for row in reader:
        id = row[0]
        body = row[4]
        
        sentences = split(body)

        for s in sentences:
            s = s.lower()
            if 'fantastic' in s and \
               'fantastically' not in s:
                print "%s\t%s" % (s, id)

def main():
    try:
        mapper()
    except:
        pass

main()
