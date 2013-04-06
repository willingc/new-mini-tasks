#!/bin/sh
echo 'Content-type: text/plain'
echo ''
wget -q 'https://docs.google.com/spreadsheet/ccc?key=0AoHP1ey91UqPdC1EUFV4aXBETmY3bFBzTFhpdG1ISEE&output=csv' -O data.csv
echo 'done'
