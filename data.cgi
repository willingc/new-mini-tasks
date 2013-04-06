#!/usr/bin/python

import csv
import json
import string

def main():
    data = list(csv.DictReader(open('data.csv')))
    for datum in data:
        datum['Required skills'] = map(string.strip, datum['Required skills'].split(','))
    print "Content-type: text/javascript\r\n\r\n"
    print "var example_items =",
    print json.dumps(data),
    print ";"

if __name__ == '__main__':
    main()
