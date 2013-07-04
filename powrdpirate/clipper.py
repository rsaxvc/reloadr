#!/usr/bin/python
import sys
try:
	in_file = open(sys.argv[1], "r")
except:
	sys.exit("Usage: " + sys.argv[0] + " html-file")
s = in_file.read()
in_file.close()

import re

s_start = re.escape("<table")
s_end = re.escape("</table>")
rgx = s_start + ".*?" + s_end

table = re.findall(rgx, s, re.I | re.DOTALL )[2]

table = table.replace( "<br>", "" )
table = table.replace( '<td align="center"><h6>', "<th>" )
table = table.replace( "</h6></td>", "</th>" )

#strip out comments
rgx = re.escape('<!--') + ".*?" + re.escape("-->")
comments = re.findall(rgx, table, re.I | re.DOTALL )
for comment in comments:
	table = table.replace( comment, "" )


print table
