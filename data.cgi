#!/usr/bin/python

import csv
import json
import string

def get_data():
    data = list(csv.DictReader(open('data.csv')))
    for datum in data:
        datum['Required skills'] = map(string.strip, datum['Required skills'].split(','))
    return 'var example_items = ' + json.dumps(data) + ';\n'

def main():
    print "Content-type: text/javascript\r\n\r\n"
    print get_data()

if __name__ == '__main__':
    main()
