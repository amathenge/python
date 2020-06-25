#!/usr/bin/env python

import os

d = os.popen('dir d:\Sony /4 /O-D /-C /S')
l = d.read()
l = l.split('\n')
f = open('out.txt', 'w')

for item in l:
	if "Directory of" in item:
		f.write("{}\n".format(item))
	elif "<DIR>" in item:
		f.write("DIRECTORY: {}\n".format(item))
	else:
		if "/" in item:
			f.write("FILE: {}\n".format(item))
		elif len(item) == 0:
			f.write('BLANK {}\n'.format(item))
		else:
			f.write("UNKNOWN: {}\n".format(item))

f.close()

# 
# some additional analysis on the files
#

f = open('out.txt', 'r')
o = open('output.txt', 'w')

for item in f:
    item = item.strip()
    if len(item) < 10:
        continue
    if item[:4] == 'FILE':
        o.write("{}\n".format(item[42:]))
        
f.close()
o.close()

