#!/usr/bin/python
import sys
try:
	in_file = open(sys.argv[1], "r")
except:
	sys.exit("Usage: " + sys.argv[0] + " raw table file")
s = in_file.read()
in_file.close()

from lxml import etree

table = etree.XML(s)
rows = iter(table)
headers = [col.text for col in next(rows)]
for row in rows:
	values = [col.text for col in row]
#	print values
	print dict(zip(headers, values))

print headers
